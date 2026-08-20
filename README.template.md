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

**Scope** — papers where reasoning itself is the contribution: the chain, the reward, the search, or the
evaluation of the chain. Medical LLMs reported only as end-task accuracy, and agent frameworks with no
reasoning mechanism, are out of scope. Entries with a note beneath them have been read and placed by hand;
the rest are categorized by keyword and should be treated as provisional.

## Contents

{{TOC}}

- [Related lists](#related-lists)
- [Contributing](#contributing)

---

{{SECTIONS}}

---

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

## License

[CC0-1.0](LICENSE) — public domain. The papers themselves belong to their authors.
