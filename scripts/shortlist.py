# -*- coding: utf-8 -*-
"""质量门槛：把 pending 里够格的论文自动进入 papers.json（标记 reviewed=false 待你复核），
其余留在 pending。目的是让列表一开始就有分量，而不是 1300 篇未筛的噪声。

    python3 scripts/shortlist.py --dry-run
    python3 scripts/shortlist.py
"""
from __future__ import print_function
import argparse
import datetime as dt
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

TODAY = dt.date.today()


def age_months(date_str):
    y, m, _ = (int(x) for x in date_str.split("-"))
    return max(1, (TODAY.year - y) * 12 + (TODAY.month - m))


def verdict(p, cfg):
    """返回 (是否收录, 理由)。近期论文引用未累积，单独留观察区不误杀。"""
    c = p.get("citations")
    if c is None:
        return False, "无引用数据"
    age = age_months(p["date"])
    if c >= cfg["min_citations"]:
        return True, "引用 %d" % c
    if c / float(age) >= cfg["min_citations_per_month"]:
        return True, "月均引用 %.1f" % (c / float(age))
    if p.get("s2_venue") and c >= cfg["min_citations_with_venue"]:
        return True, "%s + %d 引" % (p["s2_venue"][:28], c)
    if age <= cfg["grace_months"]:
        return False, "太新（%d 个月），留观察区" % age
    return False, "未达门槛（%d 引 / %d 个月）" % (c, age)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-citations", type=int, default=10)
    ap.add_argument("--min-cpm", type=float, default=1.0)
    ap.add_argument("--min-citations-with-venue", type=int, default=3)
    ap.add_argument("--grace-months", type=int, default=3)
    args = ap.parse_args()

    cfg = {"min_citations": args.min_citations,
           "min_citations_per_month": args.min_cpm,
           "min_citations_with_venue": args.min_citations_with_venue,
           "grace_months": args.grace_months}

    pending = common.load_json(common.PENDING, [])
    papers = common.load_json(common.PAPERS, [])
    known = set(p["id"] for p in papers)
    today = TODAY.isoformat()

    promote, keep = [], []
    for p in pending:
        if p["id"] in known:
            continue
        ok, why = verdict(p, cfg)
        if ok and not p.get("suggested_category"):
            ok, why = False, "关键词一个都没命中，多半跑题"
        (promote if ok else keep).append((p, why))

    promote.sort(key=lambda x: -(x[0].get("citations") or 0))
    print("门槛：引用≥%d 或 月均≥%.1f 或（有正式发表 且 引用≥%d）；近 %d 个月的暂不评判"
          % (args.min_citations, args.min_cpm, args.min_citations_with_venue, args.grace_months))
    print("入选 %d 篇，留在待筛 %d 篇\n" % (len(promote), len(keep)))
    for p, why in promote[:20]:
        print("  %5d  %-14s %s" % (p.get("citations", 0),
                                   (p.get("suggested_category") or "?")[:14], p["title"][:62]))
    if len(promote) > 20:
        print("  … 其余 %d 篇" % (len(promote) - 20))

    if args.dry_run:
        print("\n[dry-run] 未写文件")
        return

    for p, why in promote:
        papers.append({
            "id": p["id"], "title": p["title"], "authors": p.get("authors", []),
            "date": p["date"], "url": p["url"],
            "category": p.get("suggested_category") or "",
            "code": "", "venue": p.get("s2_venue", ""), "note": "",
            "tags": [], "citations": p.get("citations", 0),
            "reviewed": False, "shortlist_reason": why, "added": today,
        })
    papers.sort(key=lambda x: (-(x.get("citations") or 0), x["date"]))
    common.save_json(common.PAPERS, papers)
    common.save_json(common.PENDING, [p for p, _ in keep])
    print("\n已写入：papers.json %d 篇，pending.json %d 篇" % (len(papers), len(keep)))


if __name__ == "__main__":
    main()
