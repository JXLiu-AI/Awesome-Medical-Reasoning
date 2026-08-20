<div align="center">

# Awesome Medical Reasoning

**Papers on reasoning in medical LLMs and MLLMs.**

医学大模型推理方向的论文列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-{{COUNT}}-blue)
![Last commit](https://img.shields.io/github/last-commit/JXLiu-AI/Awesome-Medical-Reasoning)

</div>

---

{{STATS}}

Last updated: {{UPDATED}}.

## Contents

{{TOC}}

- [Selection criteria](#selection-criteria)
- [Related lists](#related-lists)
- [Contributing](#contributing)

---

{{SECTIONS}}

---

## Selection criteria

**Scope.** A paper belongs here when *reasoning* is the contribution — the chain, the reward, the search, or
the evaluation of the chain:
reasoning-chain supervision and distillation · RL with verifiable or process rewards · test-time scaling and
search · prompting and thought structures evaluated on medical tasks · knowledge-grounded reasoning ·
multimodal reasoning where the chain is tied to image evidence · benchmarks that probe reasoning quality
rather than final-answer accuracy · faithfulness, shortcut and contamination analyses · agentic diagnosis
where the reasoning mechanism, not the plumbing, is what is new.

Out of scope: medical LLMs reported only as end-task accuracy · pure retrieval or summarization systems ·
clinical deployment studies with no reasoning analysis · agent frameworks that only orchestrate existing
components · general-domain reasoning work with a medical benchmark bolted on as one table row.

**Quality bar.** A paper enters the list on one of three conditions: at least 10 citations, or at least one
citation per month since release, or peer-reviewed publication with at least 3 citations. Work from the last
three months is exempt from the bar — citations have not had time to accumulate — and waits in the queue
instead of being judged early.

**Which entries have been read.** An entry with a note beneath it has been read, placed, and annotated by
hand. An entry without one cleared the quality bar but has not yet had a close read — its category is a
keyword-assigned guess, so treat the placement as provisional. Most of the list is currently in the second
state; the distinction is left visible rather than smoothed over.

**Annotations.** Notes flag what is worth knowing before citing a number: missing compute-matched baselines,
benchmark contamination, evaluation by a judge model from the same family as the system under test, or gains
that disappear on out-of-distribution modalities.

## Related lists

Neighbouring collections, each with a different centre of gravity:

- [Awesome-LLM-Reasoning-on-Medicine](https://github.com/pqpq17/Awesome-LLM-Reasoning-on-Medicine) — organized around Miller's Pyramid, accompanies a survey in *Machine Intelligence Research*.
- [medical-llm-reasoning-survey](https://github.com/zzma2/medical-llm-reasoning-survey) — taxonomy by modality, training-time vs test-time technique, and application.
- [Awesome-Medical-LLM-Agent](https://github.com/yczhou001/Awesome-Medical-LLM-Agent) — centred on single- and multi-agent medical systems.
- [Awesome-Specialized-Medical-LLMs](https://github.com/FreedomIntelligence/Awesome-Specialized-Medical-LLMs) — organized by ICD-10 chapter rather than by method.
- [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — multimodal medical imaging broadly, not reasoning-specific.

## Contributing

- **Open an issue** with the arXiv link — fastest, no setup.
- **Send a PR editing `data/papers.json`** — not `README.md`, which is generated from it. Run
  `python3 scripts/build_readme.py` and commit both files.

Corrections are as welcome as additions. If an annotation misreads your paper, say so in an issue and it will
be fixed or removed.

## Citation

If this list is useful, a star is plenty. If you need to cite it:

```bibtex
@misc{awesome-medical-reasoning,
  title  = {Awesome Medical Reasoning},
  author = {Liu, Jiaxiang},
  year   = {2026},
  url    = {https://github.com/JXLiu-AI/Awesome-Medical-Reasoning}
}
```

## License

[CC0-1.0](LICENSE) — public domain. The papers themselves belong to their authors.
