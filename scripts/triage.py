# -*- coding: utf-8 -*-
"""交互式筛选 data/pending.json：一篇一个按键，决定收录 / 丢弃 / 跳过。

    python3 scripts/triage.py            # 从最新的开始
    python3 scripts/triage.py --oldest   # 从最旧的开始
    python3 scripts/triage.py --cat rlvr # 只看建议分类为 rlvr 的

按键：
    y  收录（用建议分类）      Y  收录并写一句话点评
    数字 收录到指定分类         n  丢弃（记进 rejected，以后不再出现）
    s  跳过（下次还会出现）     a  展开完整摘要
    o  浏览器打开              u  撤销上一步
    q  保存并退出
"""
from __future__ import print_function
import argparse
import datetime as dt
import subprocess
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import common

BOLD, DIM, CYAN, GREEN, RED, YELLOW, RESET = (
    "\033[1m", "\033[2m", "\033[36m", "\033[32m", "\033[31m", "\033[33m", "\033[0m")


def show(p, idx, total, cats, full_abstract=False):
    print("\n" + "=" * 78)
    print("%s[%d/%d]%s  %s  %s%s%s" % (BOLD, idx, total, RESET, p["date"],
                                       DIM, p.get("primary_category", ""), RESET))
    print("%s%s%s" % (CYAN + BOLD, p["title"], RESET))
    au = p.get("authors", [])
    if au:
        shown = ", ".join(au[:4]) + (" (+%d)" % (len(au) - 4) if len(au) > 4 else "")
        print("%s%s%s" % (DIM, shown, RESET))
    print("%s%s" % (DIM, p["url"] + RESET))
    if p.get("comment"):
        print("%s备注: %s%s" % (YELLOW, p["comment"][:110], RESET))
    abstract = p["abstract"] if full_abstract else p["abstract"][:420] + (
        "..." if len(p["abstract"]) > 420 else "")
    print("\n" + abstract + "\n")

    sug = p.get("suggested_category", "")
    keys = [c[0] for c in cats]
    for i, (key, display, section, _kw) in enumerate(cats, 1):
        mark = GREEN + " ←建议" + RESET if key == sug else ""
        print("  %s%2d%s %-26s %s%s%s%s" % (BOLD, i, RESET, display, DIM, section, RESET, mark))
    return keys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oldest", action="store_true")
    ap.add_argument("--cat", help="只筛建议分类为该 key 的")
    args = ap.parse_args()

    taxonomy = common.load_config("taxonomy")
    cats = common.all_categories(taxonomy)
    cat_keys = [c[0] for c in cats]

    pending = common.load_json(common.PENDING, [])
    papers = common.load_json(common.PAPERS, [])
    rejected = common.load_json(common.REJECTED, [])

    queue = [p for p in pending if not args.cat or p.get("suggested_category") == args.cat]
    queue.sort(key=lambda x: x["date"], reverse=not args.oldest)
    if not queue:
        print("没有待筛的论文。先跑 python3 scripts/fetch_arxiv.py")
        return

    remaining = {p["id"]: p for p in pending}
    history = []
    today = dt.date.today().isoformat()
    n_add = n_rej = 0
    i = 0
    full = False

    while i < len(queue):
        p = queue[i]
        if p["id"] not in remaining:      # 已经处理过（撤销后重放的情况）
            i += 1
            continue
        show(p, i + 1, len(queue), cats, full)
        full = False
        try:
            cmd = input("%s> %s" % (BOLD, RESET)).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n中断，保存进度…")
            break

        if cmd == "q":
            break
        if cmd == "s":
            i += 1
            continue
        if cmd == "a":
            full = True
            continue
        if cmd == "o":
            subprocess.call(["open", p["url"]])
            continue
        if cmd == "u":
            if not history:
                print("没有可撤销的。")
                continue
            act, item = history.pop()
            if act == "add":
                papers = [x for x in papers if x["id"] != item["id"]]
                n_add -= 1
            else:
                rejected = [x for x in rejected if x != item["id"]]
                n_rej -= 1
            remaining[item["id"]] = item
            i = max(0, i - 1)
            print("%s已撤销：%s%s" % (YELLOW, item["title"][:60], RESET))
            continue
        if cmd == "n":
            rejected.append(p["id"])
            del remaining[p["id"]]
            history.append(("rej", p))
            n_rej += 1
            i += 1
            continue

        cat = None
        note = ""
        if cmd in ("y", "Y"):
            cat = p.get("suggested_category")
            if not cat:
                print("%s没有建议分类，请输入编号。%s" % (RED, RESET))
                continue
            if cmd == "Y":
                note = input("一句话点评（可留空）: ").strip()
        elif cmd.isdigit() and 1 <= int(cmd) <= len(cats):
            cat = cat_keys[int(cmd) - 1]
        else:
            print("%s无效输入。y/Y/数字/n/s/a/o/u/q%s" % (RED, RESET))
            continue

        papers.append({
            "id": p["id"], "title": p["title"], "authors": p.get("authors", []),
            "date": p["date"], "url": p["url"], "category": cat,
            "code": "", "venue": "", "note": note, "tags": [], "added": today,
        })
        del remaining[p["id"]]
        history.append(("add", p))
        n_add += 1
        print("%s✓ 收录到 %s%s" % (GREEN, cat, RESET))
        i += 1

    papers.sort(key=lambda x: x["date"], reverse=True)
    common.save_json(common.PAPERS, papers)
    common.save_json(common.PENDING, sorted(remaining.values(),
                                            key=lambda x: x["date"], reverse=True))
    common.save_json(common.REJECTED, rejected)
    print("\n本次收录 %d 篇，丢弃 %d 篇。库内共 %d 篇，待筛还剩 %d 篇。"
          % (n_add, n_rej, len(papers), len(remaining)))
    print("下一步：python3 scripts/build_readme.py")


if __name__ == "__main__":
    main()
