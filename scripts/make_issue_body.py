# -*- coding: utf-8 -*-
"""把 pending.json 里最近新增的条目渲染成 issue 正文（供 GitHub Action 用）。

    python3 scripts/make_issue_body.py --limit 40 > body.md
"""
from __future__ import print_function
import argparse
import datetime as dt
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=40)
    args = ap.parse_args()

    pending = common.load_json(common.PENDING, [])
    taxonomy = common.load_config("taxonomy")
    display = {k: d for k, d, _s, _kw in common.all_categories(taxonomy)}

    pending.sort(key=lambda x: x["date"], reverse=True)
    shown = pending[:args.limit]

    print("Crawled on %s. **%d** papers are waiting for triage; the %d newest are listed below."
          % (dt.date.today().isoformat(), len(pending), len(shown)))
    print()
    print("Triage locally with `python3 scripts/triage.py`, or just comment here with "
          "`+ <arxiv-id> <category>` / `- <arxiv-id>` and it will be picked up on the next pass.")
    print()

    by_cat = {}
    for p in shown:
        by_cat.setdefault(p.get("suggested_category") or "unsorted", []).append(p)

    for cat, items in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
        print("### %s <sub>%d</sub>\n" % (display.get(cat, "未分类 / unsorted"), len(items)))
        for p in items:
            print("- [ ] **[%s](%s)** — `%s` %s" % (p["title"], p["url"], p["id"], p["date"]))
        print()

    if len(pending) > len(shown):
        print("<sub>… and %d older entries in `data/pending.json`.</sub>" % (len(pending) - len(shown)))


if __name__ == "__main__":
    main()
