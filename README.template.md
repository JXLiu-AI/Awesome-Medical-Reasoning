<div align="center">

# Awesome Medical Reasoning

**A continuously maintained reading list for reasoning in medical LLMs and MLLMs.**

医学大模型「推理」方向的持续维护论文列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-{{COUNT}}-blue)
![Last commit](https://img.shields.io/github/last-commit/USERNAME/Awesome-Medical-Reasoning)
![Updated weekly](https://img.shields.io/badge/updated-weekly-brightgreen)

</div>

---

{{STATS}}

**Last updated: {{UPDATED}}.** New arXiv papers are crawled daily by a GitHub Action and land in a
[triage issue](../../issues?q=label%3Atriage); every entry in this list has been read and placed by a human.

## Why another list?

Medical-AI reading lists are plentiful; ones that stay alive are not. The three closest lists to this one
([Awesome-LLM-Reasoning-on-Medicine](https://github.com/pqpq17/Awesome-LLM-Reasoning-on-Medicine),
[medical-llm-reasoning-survey](https://github.com/zzma2/medical-llm-reasoning-survey),
[Awesome-Medical-LLM-Agent](https://github.com/yczhou001/Awesome-Medical-LLM-Agent))
were each published alongside a survey and stopped updating once the survey was out. This one is built the other
way round: an automated crawler feeds a human triage queue, so keeping it current costs ~10 minutes a week.

Three commitments:

1. **Reasoning only.** A paper is in scope when *reasoning* is the contribution — the chain, the reward, the
   search, the evaluation of the chain. Medical LLMs that merely report an accuracy number are out of scope,
   as is agent-pipeline engineering with no reasoning mechanism. See the [scope rules](#scope).
2. **Every entry is human-read.** The crawler proposes; a person disposes. Nothing is auto-merged into the list.
3. **Claims get annotated, not repeated.** Where a paper's reasoning gain is confounded (no non-reasoning
   baseline at matched compute, test-set contamination, judge-model overlap), the entry says so.

## Contents

{{TOC}}

- [Scope](#scope)
- [Contributing](#contributing)

---

{{SECTIONS}}

---

## Scope

**In scope** — the contribution is the reasoning itself:
reasoning-chain supervision and distillation · RL with verifiable or process rewards · test-time scaling and
search · prompting and thought structures evaluated on medical tasks · knowledge-grounded reasoning ·
multimodal reasoning where the chain is tied to image evidence · benchmarks that probe reasoning quality
rather than final-answer accuracy · faithfulness, shortcut and contamination analyses · agentic diagnosis
where the reasoning mechanism (not the plumbing) is novel.

**Out of scope:**
medical LLMs reported only as end-task accuracy · pure retrieval or summarization systems · clinical
deployment studies with no reasoning analysis · agent frameworks that only orchestrate existing components ·
general-domain reasoning work with a medical benchmark bolted on as one table row.

**Annotation conventions.** `note` fields flag things worth knowing before citing a number: missing
compute-matched baselines, benchmark contamination, evaluation by a judge model from the same family as the
system under test, or gains that vanish on out-of-distribution modalities.

## Contributing

Adding a paper takes one of three routes:

- **Open an issue** with the arXiv link — fastest, no setup.
- **Comment on the weekly [triage issue](../../issues?q=label%3Atriage)** if the paper is already listed there.
- **Send a PR editing `data/papers.json`** (not `README.md` — it is generated). Then run
  `python3 scripts/build_readme.py` and commit both files.

Corrections are as welcome as additions. If an annotation misreads your paper, say so in an issue and it
will be fixed or removed.

## Citation

If this list helps your work, a star is plenty. If you need to cite it:

```bibtex
@misc{awesome-medical-reasoning,
  title  = {Awesome Medical Reasoning: A Continuously Maintained Reading List},
  author = {USERNAME},
  year   = {2026},
  url    = {https://github.com/USERNAME/Awesome-Medical-Reasoning}
}
```

## License

[CC0-1.0](LICENSE) — public domain. The papers themselves belong to their authors.
