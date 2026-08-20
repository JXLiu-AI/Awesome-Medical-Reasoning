<div align="center">

# Awesome Medical Reasoning

**A continuously maintained reading list for reasoning in medical LLMs and MLLMs.**

医学大模型「推理」方向的持续维护论文列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-0-blue)
![Last commit](https://img.shields.io/github/last-commit/USERNAME/Awesome-Medical-Reasoning)
![Updated weekly](https://img.shields.io/badge/updated-weekly-brightgreen)

</div>

---

**0** papers indexed so far — the list is being seeded from a 0-paper triage queue. 仓库刚起步，正在筛选中。

**Last updated: 2026-08-20.** New arXiv papers are crawled daily by a GitHub Action and land in a
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

- [🏋️ Training-Time Methods](#training-time-methods--训练期方法) <sub>0</sub>
- [🧭 Test-Time Methods](#test-time-methods--测试期方法) <sub>0</sub>
- [🖼️ Multimodal Medical Reasoning](#multimodal-medical-reasoning--多模态医学推理) <sub>0</sub>
- [🩺 Agentic Diagnostic Reasoning](#agentic-diagnostic-reasoning--智能体式诊断推理) <sub>0</sub>
- [📊 Evaluation, Benchmarks & Trustworthiness](#evaluation-benchmarks--trustworthiness--评测基准与可信度) <sub>0</sub>
- [📚 Surveys & Position Papers](#surveys--position-papers--综述与立场文章) <sub>0</sub>

- [Scope](#scope)
- [Contributing](#contributing)

---

## 🏋️ Training-Time Methods · 训练期方法

> Baking reasoning into the weights: SFT, CoT distillation, and RL.  
> <sub>把推理能力写进权重：监督微调、推理链蒸馏、强化学习。</sub>

### SFT & Reasoning-Chain Distillation · SFT 与推理链蒸馏 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### RL with Verifiable Rewards (RLVR / GRPO) · 强化学习与可验证奖励（RLVR / GRPO） <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Process Rewards & Step-Level Supervision · 过程奖励与步骤级监督 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

## 🧭 Test-Time Methods · 测试期方法

> No weight updates — think harder at inference: prompting structures, search and scaling, external knowledge.  
> <sub>不改权重，在推理时把答案想得更对：提示结构、搜索与扩展、外部知识。</sub>

### Prompting & Thought Structures · 提示与思维结构 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Test-Time Scaling & Search · 测试期扩展与搜索 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Knowledge-Grounded Reasoning (RAG / KG) · 知识增强推理（RAG / 知识图谱） <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

## 🖼️ Multimodal Medical Reasoning · 多模态医学推理

> Reasoning chains that must land on pixels, slides, and waveforms — not just text.  
> <sub>推理链要落在像素、切片、波形上，而不只是文本。</sub>

### Imaging VLM Reasoning · 影像推理 VLM <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Pathology & Whole-Slide Reasoning · 病理与全切片推理 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Cross-Modal Fusion & Modality Generalization · 跨模态融合与模态泛化 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

## 🩺 Agentic Diagnostic Reasoning · 智能体式诊断推理

> Multi-turn, multi-role, tool-using diagnostic reasoning. Only works with a novel reasoning mechanism — plain pipeline orchestration is out of scope.  
> <sub>多轮、多角色、可调用工具的诊断推理。只收推理机制有创新的工作，纯流程编排不收。</sub>

### Interactive & Proactive Diagnostic Reasoning · 交互式与主动式诊断推理 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

## 📊 Evaluation, Benchmarks & Trustworthiness · 评测、基准与可信度

> Is the reasoning gain real? The section this list most wants to get right.  
> <sub>推理增益是真的吗？这一节是本仓库最想做扎实的部分。</sub>

### Reasoning Benchmarks & Datasets · 推理基准与数据集 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Faithfulness, Hallucination & Shortcut Learning · 忠实性、幻觉与捷径学习 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

### Clinical Alignment & Human-AI Evaluation · 临床对齐与人机协同评估 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*

## 📚 Surveys & Position Papers · 综述与立场文章

### Surveys & Positions · 综述与立场 <sub>0</sub>

*Nothing yet — PRs welcome. 暂无收录，欢迎 PR。*


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
