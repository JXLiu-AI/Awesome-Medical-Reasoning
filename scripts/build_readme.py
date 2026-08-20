# -*- coding: utf-8 -*-
"""data/papers.json + README.template.md -> README.md

    python3 scripts/build_readme.py
    python3 scripts/build_readme.py --check   # 只校验是否同步（CI 用）
"""
from __future__ import print_function
import argparse
import datetime as dt
import os
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

TEMPLATE = os.path.join(common.ROOT, "README.template.md")
OUTPUT = os.path.join(common.ROOT, "README.md")


_VENUES = None
_DISPLAY = None


def is_new(p):
    """baseline_date 之后、且在 days 窗口内加入的条目算新增。
    首批入库的不算，否则整页都会挂满徽章。"""
    global _DISPLAY
    if _DISPLAY is None:
        _DISPLAY = common.load_config("display")
    cfg = (_DISPLAY or {}).get("new_badge", {})
    if not cfg.get("enabled"):
        return False
    added = p.get("added", "")
    if not added or added <= cfg.get("baseline_date", ""):
        return False
    cutoff = (dt.date.today() - dt.timedelta(days=cfg.get("days", 21))).isoformat()
    return added >= cutoff


def new_badge():
    cfg = (_DISPLAY or common.load_config("display")).get("new_badge", {})
    return "![%s](https://img.shields.io/badge/%s-%s)" % (
        cfg.get("label", "new"), cfg.get("label", "new"), cfg.get("color", "ffc9d4"))


def short_venue(name):
    """把 S2 的全称换成通行简称；未收录的原样显示，超长截断。"""
    global _VENUES
    if _VENUES is None:
        _VENUES = common.load_config("venues")
    if not name:
        return ""
    exact = {k.lower(): v for k, v in _VENUES.get("exact", {}).items()}
    hit = exact.get(name.strip().lower())
    if hit:
        return hit
    for needle, short in _VENUES.get("contains", []):
        if needle.lower() in name.lower():
            return short
    cap = _VENUES.get("max_length", 38)
    return name if len(name) <= cap else name[:cap - 1].rstrip() + "…"


def slug(title):
    """GitHub 的标题锚点规则：小写、去标点、空格转连字符（中文字符保留）。"""
    s = title.lower()
    s = re.sub(r"[^\w\s一-鿿-]", "", s)
    return s.strip().replace(" ", "-")


def fmt_paper(p):
    """一行一篇。发表处用正文字号加粗，让已正式发表的和预印本一眼分得开；
    日期与引用数用 <sub> 下沉。有注释行的表示已逐篇读过。"""
    bits = ["- [%s](%s)" % (p["title"].replace("|", "\\|"), p["url"])]
    if p.get("venue"):
        bits.append("— **%s**" % short_venue(p["venue"]))
    meta = [p["date"][:7]]
    c = p.get("citations") or 0
    if c:
        meta.append("%d citation%s" % (c, "" if c == 1 else "s"))
    meta.extend(t for t in (p.get("tags") or []) if t != "ours")
    bits.append("<sub>%s</sub>" % " · ".join(meta))
    if is_new(p):
        bits.append(new_badge())
    line = " ".join(bits)
    if p.get("note"):
        line += "\n  <sub>%s</sub>" % p["note"]
    return line


def build_sections(papers, taxonomy):
    by_cat = {}
    for p in papers:
        by_cat.setdefault(p.get("category", ""), []).append(p)
    for v in by_cat.values():
        v.sort(key=lambda x: x["date"], reverse=True)

    out, toc = [], []
    for sec in taxonomy["sections"]:
        cats = sec.get("categories", [])
        n_sec = sum(len(by_cat.get(c["key"], [])) for c in cats)
        title = "%s %s · %s" % (sec.get("emoji", ""),
                                sec.get("name_en", sec["name"]), sec["name"])
        toc.append("- [%s %s](#%s) <sub>%d</sub>"
                   % (sec.get("emoji", ""), sec.get("name_en", sec["name"]),
                      slug(title), n_sec))
        out.append("## %s\n" % title)
        if sec.get("intro_en") or sec.get("intro"):
            out.append("> %s  \n> <sub>%s</sub>\n"
                       % (sec.get("intro_en", ""), sec.get("intro", "")))
        for c in cats:
            items = by_cat.get(c["key"], [])
            out.append("### %s · %s <sub>%d</sub>\n"
                       % (c.get("display_en", c["display"]), c["display"], len(items)))
            if items:
                out.append("\n".join(fmt_paper(p) for p in items) + "\n")
            else:
                out.append("*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*\n")

    uncat = by_cat.get("", [])
    if uncat:
        out.append("## ❓ Uncategorized · 待分类\n")
        out.append("\n".join(fmt_paper(p) for p in uncat) + "\n")
    return "\n".join(out), "\n".join(toc)


def build_stats(papers, pending, taxonomy):
    n_cat = len(common.all_categories(taxonomy))
    if not papers:
        return "**0** papers indexed so far; %d more under consideration." % len(pending)
    years = {}
    for p in papers:
        years[p["date"][:4]] = years.get(p["date"][:4], 0) + 1
    span = " · ".join("%s: %d" % (y, n) for y, n in sorted(years.items()))
    line = ("**%d** papers indexed (%s) across %d sections / %d categories. "
            "%d more under consideration."
            % (len(papers), span, len(taxonomy["sections"]), n_cat, len(pending)))
    fresh = [p for p in papers if is_new(p)]
    if fresh:
        since = min(p.get("added", "") for p in fresh)
        line += ("\n\n%s **%d** added since %s."
                 % (new_badge(), len(fresh), since))
    return line


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    taxonomy = common.load_config("taxonomy")
    papers = common.load_json(common.PAPERS, [])
    pending = common.load_json(common.PENDING, [])

    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    sections, toc = build_sections(papers, taxonomy)
    rendered = (tpl
                .replace("{{SECTIONS}}", sections)
                .replace("{{TOC}}", toc)
                .replace("{{STATS}}", build_stats(papers, pending, taxonomy))
                .replace("{{COUNT}}", str(len(papers)))
                .replace("{{PENDING}}", str(len(pending)))
                .replace("{{UPDATED}}", dt.date.today().isoformat()))

    if args.check:
        current = open(OUTPUT, encoding="utf-8").read() if os.path.exists(OUTPUT) else ""
        norm = lambda s: "\n".join(l for l in s.split("\n") if "Last updated" not in l)
        if norm(current) != norm(rendered):
            print("README.md 与 papers.json 不同步，请跑 build_readme.py")
            sys.exit(1)
        print("README.md 已同步")
        return

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(rendered)
    print("已生成 README.md：%d 篇论文，%d 个小类" % (len(papers), len(common.all_categories(taxonomy))))


if __name__ == "__main__":
    main()
