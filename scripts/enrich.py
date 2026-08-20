# -*- coding: utf-8 -*-
"""用 Semantic Scholar 批量接口给 pending.json 补引用数与发表 venue，
使人工筛选可以按影响力排序，而不是被日期顺序淹没。

    python3 scripts/enrich.py            # 只补还没补过的
    python3 scripts/enrich.py --refresh  # 全部重新拉一遍
"""
from __future__ import print_function
import argparse
import json
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

API = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,venue,publicationVenue,year"
BATCH = 100          # S2 无 key 时限流很紧，批次不宜大


def fetch_batch(ids):
    body = json.dumps({"ids": ["ARXIV:" + i for i in ids]}).encode("utf-8")
    req = urllib.request.Request(API, data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "Awesome-Medical-Reasoning/1.0"})
    for attempt in range(6):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=90).read())
        except urllib.error.HTTPError as e:
            if e.code == 429:                      # 限流：指数退避，起步就退得狠一点
                wait = 30 * (attempt + 1)
            else:
                wait = 10 * (attempt + 1)
            print("  ! HTTP %d，%d 秒后重试" % (e.code, wait), file=sys.stderr)
            time.sleep(wait)
        except Exception as e:
            # 限流时服务端会直接断连，表现为各种 SSL 错误，同样按退避处理
            wait = 20 * (attempt + 1)
            print("  ! %s，%d 秒后重试" % (e, wait), file=sys.stderr)
            time.sleep(wait)
    print("  ! 该批次放弃，%d 篇留待下次" % len(ids), file=sys.stderr)
    return [None] * len(ids)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--target", default="pending", choices=["pending", "papers"])
    args = ap.parse_args()

    path = common.PENDING if args.target == "pending" else common.PAPERS
    items = common.load_json(path, [])
    todo = [p for p in items if args.refresh or "citations" not in p]
    print("共 %d 篇，需要补的 %d 篇" % (len(items), len(todo)))

    index = {p["id"]: p for p in items}
    done = 0
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        res = fetch_batch([p["id"] for p in chunk])
        for p, r in zip(chunk, res):
            if not r:
                continue   # 没拿到就不写字段，下次还会重试
            p["citations"] = r.get("citationCount") or 0
            pv = r.get("publicationVenue") or {}
            name = pv.get("name") or r.get("venue") or ""
            # arXiv 自身不算 venue
            p["s2_venue"] = "" if name.lower().startswith("arxiv") else name
        done += len(chunk)
        print("  %d/%d" % (done, len(todo)))
        common.save_json(path, items)   # 边拉边存，中断了也不白跑
        time.sleep(5)

    have = [p for p in items if p.get("citations")]
    have.sort(key=lambda x: -x["citations"])
    print("\n引用数最高的 12 篇：")
    for p in have[:12]:
        print("  %5d  %s  %s" % (p["citations"], p["date"], p["title"][:66]))
    common.save_json(path, items)


if __name__ == "__main__":
    main()
