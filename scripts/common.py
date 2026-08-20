# -*- coding: utf-8 -*-
"""共用的加载/存盘/匹配逻辑。只用标准库，GitHub Action 不需要装任何依赖。"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(ROOT, "config")
DATA_DIR = os.path.join(ROOT, "data")

PAPERS = os.path.join(DATA_DIR, "papers.json")      # 人工确认收录的，唯一真相源
PENDING = os.path.join(DATA_DIR, "pending.json")    # 自动抓到、待筛
REJECTED = os.path.join(DATA_DIR, "rejected.json")  # 筛掉的，只存 id，防止反复出现


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return default
    return json.loads(content)


def save_json(path, obj):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")


def load_config(name):
    return load_json(os.path.join(CONFIG_DIR, name + ".json"), {})


def all_categories(taxonomy):
    """返回 [(key, display, section_name, keywords), ...]，顺序即 README 顺序。"""
    out = []
    for sec in taxonomy.get("sections", []):
        for cat in sec.get("categories", []):
            out.append((cat["key"], cat["display"], sec["name"], cat.get("keywords", [])))
    return out


def base_id(arxiv_id):
    """2503.13939v2 -> 2503.13939，用于跨版本去重。"""
    return re.sub(r"v\d+$", "", (arxiv_id or "").strip())


_PAT_CACHE = {}


def _pattern(term):
    """词首边界匹配：'CT' 不会命中 'correct'，但 'diagnos' 仍能命中 'diagnostic'。
    只加前边界不加后边界，是为了让 filters 里的前缀写法（radiolog / patholog）继续生效。"""
    if term not in _PAT_CACHE:
        _PAT_CACHE[term] = re.compile(r"(?<!\w)" + re.escape(term), re.IGNORECASE)
    return _PAT_CACHE[term]


def hits(text, terms):
    """返回命中的词表。"""
    return [t for t in terms if _pattern(t).search(text)]


def guess_category(text, taxonomy):
    """按关键词命中数给分类打分，返回 (best_key, score, 排序后的候选)。"""
    scores = []
    for key, display, section, keywords in all_categories(taxonomy):
        matched = hits(text, keywords)
        # 按关键词表长度归一，否则词表长的类目（如影像）会无脑吃掉所有论文
        score = len(matched) / (len(keywords) ** 0.5) if keywords else 0.0
        scores.append((round(score, 3), key, display, section, matched))
    scores.sort(key=lambda x: -x[0])
    best = scores[0]
    return (best[1] if best[0] > 0 else "", best[0], scores)
