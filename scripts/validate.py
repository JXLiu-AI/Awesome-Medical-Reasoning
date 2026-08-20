# -*- coding: utf-8 -*-
"""校验 data/*.json 与 config/*.json 的结构，CI 用。任何错误 -> 退出码 1。"""
from __future__ import print_function
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

REQUIRED = ["id", "title", "date", "url", "category"]
ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def main():
    errors = []
    taxonomy = common.load_config("taxonomy")
    valid_cats = set(k for k, _d, _s, _kw in common.all_categories(taxonomy))
    if not valid_cats:
        errors.append("taxonomy.json 没有解析出任何分类")

    papers = common.load_json(common.PAPERS, [])
    seen = {}
    for i, p in enumerate(papers):
        where = "papers[%d] %s" % (i, p.get("title", "")[:50])
        for f in REQUIRED:
            if not p.get(f):
                errors.append("%s: 缺字段 %s" % (where, f))
        if p.get("category") and p["category"] not in valid_cats:
            errors.append("%s: 未知分类 %r（taxonomy.json 里没有）" % (where, p["category"]))
        if p.get("date") and not DATE.match(p["date"]):
            errors.append("%s: 日期格式应为 YYYY-MM-DD，实为 %r" % (where, p["date"]))
        if p.get("id"):
            if not ARXIV_ID.match(p["id"]):
                errors.append("%s: arXiv id 格式可疑 %r（应形如 2503.13939）" % (where, p["id"]))
            if p["id"] in seen:
                errors.append("%s: id %s 与 papers[%d] 重复" % (where, p["id"], seen[p["id"]]))
            seen[p["id"]] = i

    pending = common.load_json(common.PENDING, [])
    rejected = common.load_json(common.REJECTED, [])
    overlap = set(seen) & set(common.base_id(p["id"]) for p in pending)
    if overlap:
        errors.append("同一篇同时在 papers 和 pending 里: %s" % ", ".join(sorted(overlap)[:5]))
    overlap2 = set(seen) & set(rejected)
    if overlap2:
        errors.append("同一篇同时在 papers 和 rejected 里: %s" % ", ".join(sorted(overlap2)[:5]))

    if errors:
        print("校验失败，共 %d 处：" % len(errors))
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("校验通过：收录 %d 篇 / 待筛 %d 篇 / 已弃 %d 篇，分类 %d 个"
          % (len(papers), len(pending), len(rejected), len(valid_cats)))


if __name__ == "__main__":
    main()
