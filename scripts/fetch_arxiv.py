# -*- coding: utf-8 -*-
"""抓 arXiv -> 本地规则过滤 -> 去重 -> 写 data/pending.json。

用法:
    python3 scripts/fetch_arxiv.py                 # 增量：抓 filters.default_since 之后的
    python3 scripts/fetch_arxiv.py --since 2025-01-01
    python3 scripts/fetch_arxiv.py --days 7        # 只看最近 7 天（每日 Action 用这个）
    python3 scripts/fetch_arxiv.py --dry-run       # 只打印，不写文件
"""
from __future__ import print_function
import argparse
import datetime as dt
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

API = "https://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
UA = "Awesome-Medical-Reasoning/1.0 (paper list curation; contact via GitHub issues)"


def fetch_query(query, cats, max_results, page_size=100):
    """一条检索式，分页拉取，返回 entry 列表。"""
    cat_clause = " OR ".join("cat:" + c for c in cats)
    full = "(%s) AND (%s)" % (query, cat_clause)
    entries = []
    start = 0
    while start < max_results:
        params = {
            "search_query": full,
            "start": start,
            "max_results": min(page_size, max_results - start),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = API + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        for attempt in range(3):
            try:
                raw = urllib.request.urlopen(req, timeout=60).read()
                break
            except Exception as e:
                if attempt == 2:
                    print("  ! 请求失败，跳过: %s" % e, file=sys.stderr)
                    return entries
                time.sleep(5 * (attempt + 1))
        root = ET.fromstring(raw)
        batch = root.findall("a:entry", NS)
        entries.extend(batch)
        if len(batch) < params["max_results"]:
            break
        start += len(batch)
        time.sleep(3)  # arXiv 要求的礼貌间隔
    return entries


def parse_entry(e):
    def txt(node):
        return " ".join(node.text.split()) if node is not None and node.text else ""

    raw_id = txt(e.find("a:id", NS)).rsplit("/abs/", 1)[-1]
    authors = [txt(a.find("a:name", NS)) for a in e.findall("a:author", NS)]
    comment = txt(e.find("arxiv:comment", NS))
    prim = e.find("arxiv:primary_category", NS)
    return {
        "id": common.base_id(raw_id),
        "version_id": raw_id,
        "title": txt(e.find("a:title", NS)),
        "abstract": txt(e.find("a:summary", NS)),
        "authors": authors,
        "date": txt(e.find("a:published", NS))[:10],
        "updated": txt(e.find("a:updated", NS))[:10],
        "url": "https://arxiv.org/abs/" + common.base_id(raw_id),
        "primary_category": prim.get("term") if prim is not None else "",
        "comment": comment,
    }


def passes(paper, filters):
    text = paper["title"] + " " + paper["abstract"]
    if len(paper["abstract"]) < filters.get("min_abstract_chars", 0):
        return False, "摘要过短"
    if common.hits(text, filters.get("exclude", [])):
        return False, "命中排除词"
    if not common.hits(text, filters.get("reasoning_terms", [])):
        return False, "无推理相关词"
    if not common.hits(text, filters.get("medical_terms", [])):
        return False, "无医学相关词"
    return True, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", help="YYYY-MM-DD，只保留该日期之后提交的")
    ap.add_argument("--days", type=int, help="只看最近 N 天（覆盖 --since）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    filters = common.load_config("filters")
    taxonomy = common.load_config("taxonomy")

    since = args.since or filters.get("default_since", "2024-01-01")
    if args.days:
        since = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()

    papers = common.load_json(common.PAPERS, [])
    pending = common.load_json(common.PENDING, [])
    rejected = common.load_json(common.REJECTED, [])

    known = set(common.base_id(p["id"]) for p in papers)
    known |= set(common.base_id(p["id"]) for p in pending)
    known |= set(common.base_id(x if isinstance(x, str) else x["id"]) for x in rejected)

    print("检索起始日期: %s | 已知条目: %d 篇（收录 %d / 待筛 %d / 已弃 %d）"
          % (since, len(known), len(papers), len(pending), len(rejected)))

    seen_this_run = {}
    for i, q in enumerate(filters["queries"], 1):
        print("[%d/%d] %s" % (i, len(filters["queries"]), q))
        entries = fetch_query(q, filters["arxiv_categories"],
                              filters.get("max_results_per_query", 200))
        kept = 0
        for e in entries:
            p = parse_entry(e)
            if p["date"] < since:
                continue
            if p["id"] in known or p["id"] in seen_this_run:
                continue
            ok, _why = passes(p, filters)
            if not ok:
                continue
            cat, score, _ = common.guess_category(p["title"] + " " + p["abstract"], taxonomy)
            p["suggested_category"] = cat
            p["suggest_score"] = score
            seen_this_run[p["id"]] = p
            kept += 1
        print("    抓到 %d 篇，新增通过 %d 篇" % (len(entries), kept))
        time.sleep(3)

    new = sorted(seen_this_run.values(), key=lambda x: x["date"], reverse=True)
    print("\n本次新增待筛: %d 篇" % len(new))
    for p in new[:15]:
        print("  %s  %-14s  %s" % (p["date"], p.get("suggested_category", "?"), p["title"][:80]))
    if len(new) > 15:
        print("  ... 其余 %d 篇见 data/pending.json" % (len(new) - 15))

    if args.dry_run:
        print("\n[dry-run] 未写文件")
        return

    merged = new + pending
    merged.sort(key=lambda x: x["date"], reverse=True)
    common.save_json(common.PENDING, merged)
    print("\n已写入 %s（共 %d 篇待筛）" % (common.PENDING, len(merged)))


if __name__ == "__main__":
    main()
