<div align="center">

# Awesome Medical Reasoning

**Papers on reasoning in medical LLMs and MLLMs.**

医学大模型推理方向的论文列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-303-blue)
![Last commit](https://img.shields.io/github/last-commit/JXLiu-AI/Awesome-Medical-Reasoning)

</div>

---

**303** papers indexed (2023: 1 · 2024: 46 · 2025: 180 · 2026: 76) across 6 sections / 14 categories. 1051 more under consideration.

Last updated: 2026-08-20.

## Contents

- [🏋️ Training-Time Methods](#training-time-methods--训练期方法) <sub>42</sub>
- [🧭 Test-Time Methods](#test-time-methods--测试期方法) <sub>54</sub>
- [🖼️ Multimodal Medical Reasoning](#multimodal-medical-reasoning--多模态医学推理) <sub>75</sub>
- [🩺 Agentic Diagnostic Reasoning](#agentic-diagnostic-reasoning--智能体式诊断推理) <sub>23</sub>
- [📊 Evaluation, Benchmarks & Trustworthiness](#evaluation-benchmarks--trustworthiness--评测基准与可信度) <sub>100</sub>
- [📚 Surveys & Position Papers](#surveys--position-papers--综述与立场文章) <sub>9</sub>

- [Selection criteria](#selection-criteria)
- [Related lists](#related-lists)
- [Contributing](#contributing)

---

## 🏋️ Training-Time Methods · 训练期方法

> Baking reasoning into the weights: SFT, CoT distillation, and RL.  
> <sub>把推理能力写进权重：监督微调、推理链蒸馏、强化学习。</sub>

### SFT & Reasoning-Chain Distillation · SFT 与推理链蒸馏 <sub>10</sub>

- **[A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.25947)** — 2026-07 · 1 cites · *unreviewed*
- **[PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation](https://arxiv.org/abs/2606.17199)** — 2026-06 · 3 cites · *unreviewed*
- **[Stable On-Policy Distillation through Adaptive Target Reformulation](https://arxiv.org/abs/2601.07155)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 35 cites · *unreviewed*
- **[Knowledge Graph Augmented Large Language Models for Disease Prediction](https://arxiv.org/abs/2512.01210)** — 2025-12 · **AMIA Joint Summits on Translational Science proceedings. AMIA Joint Summits on Translational Science** · 3 cites · *unreviewed*
- **[Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains](https://arxiv.org/abs/2506.02126)** — 2025-06 · 14 cites · *unreviewed*
- **[Beyond Distillation: Pushing the Limits of Medical LLM Reasoning with Minimalist Rule-Based RL](https://arxiv.org/abs/2505.17952)** — 2025-05 · 33 cites · *unreviewed*
- **[TrialMatchAI: An End-to-End AI-powered Clinical Trial Recommendation System to Streamline Patient-to-Trial Matching](https://arxiv.org/abs/2505.08508)** — 2025-05 · **Nature Communications** · 10 cites · *unreviewed*
- **[X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains](https://arxiv.org/abs/2505.03981)** — 2025-05 · 30 cites · *unreviewed*
- **[O1 Replication Journey -- Part 3: Inference-time Scaling for Medical Reasoning](https://arxiv.org/abs/2501.06458)** — 2025-01 · 38 cites · *unreviewed*
- **[MedThink: Explaining Medical Visual Question Answering via Multimodal Decision-Making Rationale](https://arxiv.org/abs/2404.12372)** — 2024-04 · **LREC-COLING 2024**
  <sub>Supervises Med-VQA with multimodal decision rationales, so the explanation and the answer share a source instead of being rationalized after the fact.</sub>

### RL with Verifiable Rewards (RLVR / GRPO) · 强化学习与可验证奖励（RLVR / GRPO） <sub>29</sub>

- **[Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models](https://arxiv.org/abs/2607.02983)** — 2026-07 · 1 cites · *unreviewed*
- **[RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation](https://arxiv.org/abs/2606.11709)** — 2026-06 · 15 cites · *unreviewed*
- **[Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943)** — 2026-05 · 4 cites · *unreviewed*
- **[Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning](https://arxiv.org/abs/2605.02913)** — 2026-04 · 6 cites · *unreviewed*
- **[Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning](https://arxiv.org/abs/2603.03437)** — 2026-03 · 7 cites · *unreviewed*
- **[Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420)** — 2026-02 · 7 cites · *unreviewed*
- **[Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://arxiv.org/abs/2601.17223)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 11 cites · *unreviewed*
- **[CURE-Med: Curriculum-Informed Reinforcement Learning for Multilingual Medical Reasoning](https://arxiv.org/abs/2601.13262)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 8 cites · *unreviewed*
- **[MedEyes: Learning Dynamic Visual Focus for Medical Progressive Diagnosis](https://arxiv.org/abs/2511.22018)** — 2025-11 · **AAAI Conference on Artificial Intelligence** · 34 cites · *unreviewed*
- **[Exploiting Tree Structure for Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2509.18314)** — 2025-09 · 24 cites · *unreviewed*
- **[Reward Hacking Mitigation using Verifiable Composite Rewards](https://arxiv.org/abs/2509.15557)** — 2025-09 · **ACM International Conference on Bioinformatics, Computational Biology and Biomedicine** · 8 cites · *unreviewed*
- **[Dream-Coder 7B: An Open Diffusion Language Model for Code](https://arxiv.org/abs/2509.01142)** — 2025-09 · 71 cites · *unreviewed*
- **[MedGR$^2$: Breaking the Data Barrier for Medical Reasoning via Generative Reward Learning](https://arxiv.org/abs/2508.20549)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 9 cites · *unreviewed*
- **[MedResearcher-R1: Expert-Level Medical Deep Researcher via A Knowledge-Informed Trajectory Synthesis Framework](https://arxiv.org/abs/2508.14880)** — 2025-08 · 21 cites · *unreviewed*
- **[DocThinker: Explainable Multimodal Large Language Models with Rule-based Reinforcement Learning for Document Understanding](https://arxiv.org/abs/2508.08589)** — 2025-08 · **IEEE International Conference on Computer Vision** · 15 cites · *unreviewed*
- **[MedVLThinker: Simple Baselines for Multimodal Medical Reasoning](https://arxiv.org/abs/2508.02669)** — 2025-08 · 28 cites · *unreviewed*
- **[CX-Mind: A Pioneering Multimodal Large Language Model for Interleaved Reasoning in Chest X-ray via Curriculum-Guided Reinforcement Learning](https://arxiv.org/abs/2508.03733)** — 2025-07 · **Information Fusion** · 3 cites · *unreviewed*
- **[Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://arxiv.org/abs/2507.17746)** — 2025-07 · 268 cites · *unreviewed*
- **[MedGround-R1: Advancing Medical Image Grounding via Spatial-Semantic Rewarded Group Relative Policy Optimization](https://arxiv.org/abs/2507.02994)** — 2025-07 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 20 cites · *unreviewed*
- **[GEMeX-RMCoT: An Enhanced Med-VQA Dataset for Region-Aware Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2506.17939)** — 2025-06 · **ACM Multimedia** · 5 cites · *unreviewed*
- **[Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](https://arxiv.org/abs/2506.12323)** — 2025-06 · **Advances in Neural Information Processing Systems 38** · 12 cites · *unreviewed*
- **[QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](https://arxiv.org/abs/2506.00711)** — 2025-05 · **Neural Information Processing Systems** · 42 cites · *unreviewed*
- **[Training LLMs for EHR-Based Reasoning Tasks via Reinforcement Learning](https://arxiv.org/abs/2505.24105)** — 2025-05 · 12 cites · *unreviewed*
- **[Improving Medical Reasoning with Curriculum-Aware Reinforcement Learning](https://arxiv.org/abs/2505.19213)** — 2025-05 · 17 cites · *unreviewed*
- **[Patho-R1: A Multimodal Reinforcement Learning-Based Pathology Expert Reasoner](https://arxiv.org/abs/2505.11404)** — 2025-05 · **AAAI Conference on Artificial Intelligence** · 35 cites · *unreviewed*
- **[GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886)** — 2025-04 · 31 cites · *unreviewed*
- **[Med-R1: Reinforcement Learning for Generalizable Medical Reasoning in Vision-Language Models](https://arxiv.org/abs/2503.13939)** — 2025-03 · **IEEE Transactions on Medical Imaging** · 146 cites · *unreviewed*
- **[Med-RLVR: Emerging Medical Reasoning from a 3B base model via reinforcement Learning](https://arxiv.org/abs/2502.19655)** — 2025-02 · 38 cites · *unreviewed*
- **[HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs](https://arxiv.org/abs/2412.18925)** — 2024-12 · 270 cites · *unreviewed*

### Process Rewards & Step-Level Supervision · 过程奖励与步骤级监督 <sub>3</sub>

- **[Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards](https://arxiv.org/abs/2506.11474)** — 2025-06 · **Conference on Empirical Methods in Natural Language Processing** · 26 cites · *unreviewed*
- **[ChestX-Reasoner: Advancing Radiology Foundation Models with Reasoning through Step-by-Step Verification](https://arxiv.org/abs/2504.20930)** — 2025-04 · 33 cites · *unreviewed*
- **[Bridging Stepwise Lab-Informed Pretraining and Knowledge-Guided Learning for Diagnostic Reasoning](https://arxiv.org/abs/2410.19955)** — 2024-10 · **IEEE journal of biomedical and health informatics** · 4 cites · *unreviewed*

## 🧭 Test-Time Methods · 测试期方法

> No weight updates — think harder at inference: prompting structures, search and scaling, external knowledge.  
> <sub>不改权重，在推理时把答案想得更对：提示结构、搜索与扩展、外部知识。</sub>

### Prompting & Thought Structures · 提示与思维结构 <sub>30</sub>

- **[HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179)** — 2026-06 · 6 cites · *unreviewed*
- **[COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion](https://arxiv.org/abs/2605.15016)** — 2026-05 · 3 cites · *unreviewed*
- **[MedSynapse-V: Bridging Visual Perception and Clinical Intuition via Latent Memory Evolution](https://arxiv.org/abs/2604.26283)** — 2026-04 · 16 cites · *unreviewed*
- **[TARSE: Test-Time Adaptation via Retrieval of Skills and Experience for Reasoning Agents](https://arxiv.org/abs/2603.01241)** — 2026-03 · 5 cites · *unreviewed*
- **[DEEPMED: Building a Medical DeepResearch Agent via Multi-hop Med-Search Data and Turn-Controlled Agentic Training & Inference](https://arxiv.org/abs/2601.18496)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 5 cites · *unreviewed*
- **[OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data](https://arxiv.org/abs/2510.02410)** — 2025-10 · 22 cites · *unreviewed*
- **[MuSLR: Multimodal Symbolic Logical Reasoning](https://arxiv.org/abs/2509.25851)** — 2025-09 · **Neural Information Processing Systems** · 4 cites · *unreviewed*
- **[MedCoT-RAG: Causal Chain-of-Thought RAG for Medical Question Answering](https://arxiv.org/abs/2508.15849)** — 2025-08 · **International Conference on Wearable and Implantable Body Sensor Networks** · 10 cites · *unreviewed*
- **[Affective-ROPTester: Capability and Bias Analysis of LLMs in Predicting Retinopathy of Prematurity](https://arxiv.org/abs/2507.05816)** — 2025-07 · **IEEE Transactions on Affective Computing** · 13 cites · *unreviewed*
- **[Conformal Information Pursuit for Interactively Guiding Large Language Models](https://arxiv.org/abs/2507.03279)** — 2025-07 · **Neural Information Processing Systems** · 8 cites · *unreviewed*
- **[VAP-Diffusion: Enriching Descriptions with MLLMs for Enhanced Medical Image Generation](https://arxiv.org/abs/2506.23641)** — 2025-06 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 3 cites · *unreviewed*
- **[PPMI: Privacy-Preserving LLM Interaction with Socratic Chain-of-Thought Reasoning and Homomorphically Encrypted Vector Databases](https://arxiv.org/abs/2506.17336)** — 2025-06 · 10 cites · *unreviewed*
- **[Instruction Tuning and CoT Prompting for Contextual Medical QA with LLMs](https://arxiv.org/abs/2506.12182)** — 2025-06 · **2025 International Conference on Artificial Intelligence, Human-Computer Interaction and Natural Language Processing (ICAHN)** · 14 cites · *unreviewed*
- **[MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning](https://arxiv.org/abs/2505.20096)** — 2025-05 · 39 cites · *unreviewed*
- **[Detecting PTSD in Clinical Interviews: A Comparative Analysis of NLP Methods and Large Language Models](https://arxiv.org/abs/2504.01216)** — 2025-04 · **Pacific Symposium on Biocomputing. Pacific Symposium on Biocomputing** · 7 cites · *unreviewed*
- **[AutoMedPrompt: A New Framework for Optimizing LLM Medical Prompts Using Textual Gradients](https://arxiv.org/abs/2502.15944)** — 2025-02 · 14 cites · *unreviewed*
- **[Enhancing Depression Detection with Chain-of-Thought Prompting: From Emotion to Reasoning Using Large Language Models](https://arxiv.org/abs/2502.05879)** — 2025-02 · **Annual International Conference of the IEEE Engineering in Medicine and Biology Society** · 14 cites · *unreviewed*
- **[Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction](https://arxiv.org/abs/2501.18724)** — 2025-01 · **Conference on Empirical Methods in Natural Language Processing** · 17 cites · *unreviewed*
- **[Layered Chain-of-Thought Prompting for Multi-Agent LLM Systems: A Comprehensive Approach to Explainable Large Language Models](https://arxiv.org/abs/2501.18645)** — 2025-01 · 19 cites · *unreviewed*
- **[Benchmarking Generative AI for Scoring Medical Student Interviews in Objective Structured Clinical Examinations (OSCEs)](https://arxiv.org/abs/2501.13957)** — 2025-01 · **International Conference on Artificial Intelligence in Education** · 17 cites · *unreviewed*
- **[MedCoT: Medical Chain of Thought via Hierarchical Expert](https://arxiv.org/abs/2412.13736)** — 2024-12 · **EMNLP 2024**
  <sub>Hierarchical experts generate and cross-verify the reasoning chain, rather than one model walking a single chain end to end.</sub>
- **[Synthetic Data Generation with LLM for Improved Depression Prediction](https://arxiv.org/abs/2411.17672)** — 2024-11 · 26 cites · *unreviewed*
- **[From Medprompt to o1: Exploration of Run-Time Strategies for Medical Challenge Problems and Beyond](https://arxiv.org/abs/2411.03590)** — 2024-11 · 36 cites · *unreviewed*
- **[Large Language Models for Medical OSCE Assessment: A Novel Approach to Transcript Analysis](https://arxiv.org/abs/2410.12858)** — 2024-10 · 11 cites · *unreviewed*
- **[PASS:Test-Time Prompting to Adapt Styles and Semantic Shapes in Medical Image Segmentation](https://arxiv.org/abs/2410.01573)** — 2024-10 · **IEEE Transactions on Medical Imaging** · 13 cites · *unreviewed*
- **[LLMs are not Zero-Shot Reasoners for Biomedical Information Extraction](https://arxiv.org/abs/2408.12249)** — 2024-08 · **The Sixth Workshop on Insights from Negative Results in NLP** · 21 cites · *unreviewed*
- **[IgnitionInnovators at "Discharge Me!": Chain-of-Thought Instruction Finetuning Large Language Models for Discharge Summaries](https://arxiv.org/abs/2407.17636)** — 2024-07 · **Workshop on Biomedical Natural Language Processing** · 5 cites · *unreviewed*
- **[FZI-WIM at SemEval-2024 Task 2: Self-Consistent CoT for Complex NLI in Biomedical Domain](https://arxiv.org/abs/2406.10040)** — 2024-06 · **International Workshop on Semantic Evaluation** · 3 cites · *unreviewed*
- **[Chain-of-Though (CoT) prompting strategies for medical error detection and correction](https://arxiv.org/abs/2406.09103)** — 2024-06 · **Clinical Natural Language Processing Workshop** · 11 cites · *unreviewed*
- **[A ChatGPT Aided Explainable Framework for Zero-Shot Medical Image Diagnosis](https://arxiv.org/abs/2307.01981)** — 2023-07
  <sub>Early work making the decision process of zero-shot medical image diagnosis explicit and inspectable.</sub>

### Test-Time Scaling & Search · 测试期扩展与搜索 <sub>4</sub>

- **[Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://arxiv.org/abs/2510.18424)** — 2025-10 · **Conference on Empirical Methods in Natural Language Processing** · 3 cites · *unreviewed*
- **[Rethinking Inference-Time Scaling: Efficiency Limits and Linguistic Signals](https://arxiv.org/abs/2504.14047)** — 2025-04 · 21 cites · *unreviewed*
- **[m1: Unleash the Potential of Test-Time Scaling for Medical Reasoning with Large Language Models](https://arxiv.org/abs/2504.00869)** — 2025-04 · 41 cites · *unreviewed*
- **[RARE: Retrieval-Augmented Reasoning Enhancement for Large Language Models](https://arxiv.org/abs/2412.02830)** — 2024-12 · **Annual Meeting of the Association for Computational Linguistics** · 32 cites · *unreviewed*

### Knowledge-Grounded Reasoning (RAG / KG) · 知识增强推理（RAG / 知识图谱） <sub>20</sub>

- **[NeuroGRIP: Retrieval-Augmented Graph Refinement for Knowledge-Grounded EEG Seizure Diagnosis](https://arxiv.org/abs/2607.14314)** — 2026-07 · 1 cites · *unreviewed*
- **[Expert-Guided Prompting and Retrieval-Augmented Generation for Emergency Medical Service Question Answering](https://arxiv.org/abs/2511.10900)** — 2025-11 · **AAAI Conference on Artificial Intelligence** · 4 cites · *unreviewed*
- **[RAR$^2$: Retrieval-Augmented Medical Reasoning via Thought-Driven Retrieval](https://arxiv.org/abs/2509.22713)** — 2025-09 · **Conference on Empirical Methods in Natural Language Processing** · 3 cites · *unreviewed*
- **[MIRAGE: Scaling Test-Time Inference with Parallel Graph-Retrieval-Augmented Reasoning Chains](https://arxiv.org/abs/2508.18260)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 7 cites · *unreviewed*
- **[End-to-End Agentic RAG System Training for Traceable Diagnostic Reasoning](https://arxiv.org/abs/2508.15746)** — 2025-08 · 13 cites · *unreviewed*
- **[HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches](https://arxiv.org/abs/2508.08088)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 7 cites · *unreviewed*
- **[Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning](https://arxiv.org/abs/2508.02258)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 13 cites · *unreviewed*
- **[Multi-step retrieval and reasoning improves radiology question answering with large language models](https://arxiv.org/abs/2508.00743)** — 2025-08 · **npj Digital Medicine** · 18 cites · *unreviewed*
- **[DoctorRAG: Medical RAG Fusing Knowledge with Patient Analogy through Textual Gradients](https://arxiv.org/abs/2505.19538)** — 2025-05 · 10 cites · *unreviewed*
- **[A Multimodal Multi-Agent Framework for Radiology Report Generation](https://arxiv.org/abs/2505.09787)** — 2025-05 · 13 cites · *unreviewed*
- **[Medical Reasoning in LLMs: An In-Depth Analysis of DeepSeek R1](https://arxiv.org/abs/2504.00016)** — 2025-03 · **Frontiers Artif. Intell.** · 50 cites · *unreviewed*
- **[Experience Retrieval-Augmentation with Electronic Health Records Enables Accurate Discharge QA](https://arxiv.org/abs/2503.17933)** — 2025-03 · **Annual Meeting of the Association for Computational Linguistics** · 12 cites · *unreviewed*
- **[Bias Evaluation and Mitigation in Retrieval-Augmented Medical Question-Answering Systems](https://arxiv.org/abs/2503.15454)** — 2025-03 · **AMIA ... Annual Symposium proceedings. AMIA Symposium** · 8 cites · *unreviewed*
- **[Integrating Chain-of-Thought and Retrieval Augmented Generation Enhances Rare Disease Diagnosis from Clinical Notes](https://arxiv.org/abs/2503.12286)** — 2025-03 · **Medicine Bulletin** · 13 cites · *unreviewed*
- **[Towards Conversational AI for Disease Management](https://arxiv.org/abs/2503.06074)** — 2025-03 · 14 cites · *unreviewed*
- **[Causal Graphs Meet Thoughts: Enhancing Complex Reasoning in Graph-Augmented LLMs](https://arxiv.org/abs/2501.14892)** — 2025-01 · 17 cites · *unreviewed*
- **[Tree-based RAG-Agent Recommendation System: A Case Study in Medical Test Data](https://arxiv.org/abs/2501.02727)** — 2025-01 · 12 cites · *unreviewed*
- **[Multi-OphthaLingua: A Multilingual Benchmark for Assessing and Debiasing LLM Ophthalmological QA in LMICs](https://arxiv.org/abs/2412.14304)** — 2024-12 · 15 cites · *unreviewed*
- **[HealthQ: Unveiling Questioning Capabilities of LLM Chains in Healthcare Conversations](https://arxiv.org/abs/2409.19487)** — 2024-09 · **Smart Health** · 49 cites · *unreviewed*
- **[DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://arxiv.org/abs/2408.01933)** — 2024-08 · **Neural Information Processing Systems** · 25 cites · *unreviewed*

## 🖼️ Multimodal Medical Reasoning · 多模态医学推理

> Reasoning chains that must land on pixels, slides, and waveforms — not just text.  
> <sub>推理链要落在像素、切片、波形上，而不只是文本。</sub>

### Imaging VLM Reasoning · 影像推理 VLM <sub>51</sub>

- **[Scaling Up Formal Representation of Clinical Trial Protocols in Ensemble Logic Using LLMs: A Preliminary Study](https://arxiv.org/abs/2607.21307)** — 2026-07 · 1 cites · *unreviewed*
- **[Med-OPD: Improving Medical Vision-Language Models via Evidence-Aware On-Policy Distillation](https://arxiv.org/abs/2607.16303)** — 2026-07 · 1 cites · *unreviewed*
- **[BioMedVR: Confusion-Aware Mixture-of-Prompt Experts for Biomedical Visual Reprogramming](https://arxiv.org/abs/2606.24740)** — 2026-06 · **ECCV 2026**
  <sub>Mixture-of-prompt experts targeted at confusable cases in biomedical visual reasoning.</sub>
- **[Enhancing Pathological VLMs with Cross-scale Reasoning](https://arxiv.org/abs/2606.17412)** — 2026-06 · 2 cites · *unreviewed*
- **[Lost in Volume: The CT-SpatialVQA Benchmark for Evaluating Semantic-Spatial Understanding of 3D Medical Vision-Language Models](https://arxiv.org/abs/2605.08787)** — 2026-05 · 4 cites · *unreviewed*
- **[MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2604.08203)** — 2026-04 · 6 cites · *unreviewed*
- **[A Reasoning-Enabled Vision-Language Foundation Model for Chest X-ray Interpretation](https://arxiv.org/abs/2604.00493)** — 2026-04 · 4 cites · *unreviewed*
- **[CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157)** — 2026-03 · 5 cites · *unreviewed*
- **[MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images](https://arxiv.org/abs/2602.06965)** — 2026-02 · 9 cites · *unreviewed*
- **[MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding](https://arxiv.org/abs/2512.06581)** — 2025-12 · 8 cites · *unreviewed*
- **[Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning](https://arxiv.org/abs/2512.00818)** — 2025-11 · 12 cites · *unreviewed*
- **[S-Chain: Structured Visual Chain-of-Thought For Medicine](https://arxiv.org/abs/2510.22728)** — 2025-10 · 10 cites · *unreviewed*
- **[3DReasonKnee: Advancing Grounded Reasoning in Medical Vision Language Models](https://arxiv.org/abs/2510.20967)** — 2025-10 · **Pacific Symposium on Biocomputing. Pacific Symposium on Biocomputing** · 5 cites · *unreviewed*
- **[MedReason-R1: Learning to Reason for CT Diagnosis with Reinforcement Learning and Local Zoom](https://arxiv.org/abs/2510.19626)** — 2025-10 · **IEEE International Symposium on Biomedical Imaging** · 3 cites · *unreviewed*
- **[Think Twice to See More: Iterative Visual Reasoning in Medical VLMs](https://arxiv.org/abs/2510.10052)** — 2025-10 · 13 cites · *unreviewed*
- **[Hulu-Med: A Transparent Generalist Model towards Holistic Medical Vision-Language Understanding](https://arxiv.org/abs/2510.08668)** — 2025-10 · 90 cites · *unreviewed*
- **[Toward a Vision-Language Foundation Model for Medical Data: Multimodal Dataset and Benchmarks for Vietnamese PET/CT Report Generation](https://arxiv.org/abs/2509.24739)** — 2025-09 · **Neural Information Processing Systems** · 8 cites · *unreviewed*
- **[EditGRPO: Reinforcement Learning with Post-Rollout Edits for Clinically Accurate Chest X-Ray Report Generation](https://arxiv.org/abs/2509.22812)** — 2025-09 · **IJCNLP-AACL** · 11 cites · *unreviewed*
- **[Knowing or Guessing? Robust Medical Visual Question Answering via Joint Consistency and Contrastive Learning](https://arxiv.org/abs/2508.18687)** — 2025-08 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 4 cites · *unreviewed*
- **[DINOv3 with Test-Time Training for Medical Image Registration](https://arxiv.org/abs/2508.14809)** — 2025-08 · **Medical Imaging** · 8 cites · *unreviewed*
- **[Benchmarking GPT-5 for Zero-Shot Multimodal Medical Reasoning in Radiology and Radiation Oncology](https://arxiv.org/abs/2508.13192)** — 2025-08 · **Medical Imaging** · 8 cites · *unreviewed*
- **[Performance of GPT-5 in Brain Tumor MRI Reasoning](https://arxiv.org/abs/2508.10865)** — 2025-08 · **Medical Imaging** · 8 cites · *unreviewed*
- **[MedAtlas: Evaluating LLMs for Multi-Round, Multi-Task Medical Reasoning Across Diverse Imaging Modalities and Clinical Text](https://arxiv.org/abs/2508.10947)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 6 cites · *unreviewed*
- **[MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://arxiv.org/abs/2508.08177)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 9 cites · *unreviewed*
- **[PriorRG: Prior-Guided Contrastive Pre-training and Coarse-to-Fine Decoding for Chest X-ray Report Generation](https://arxiv.org/abs/2508.05353)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 11 cites · *unreviewed*
- **[CLARIFID: Improving Radiology Report Generation by Reinforcing Clinically Accurate Impressions and Enforcing Detailed Findings](https://arxiv.org/abs/2507.17234)** — 2025-07 · **Expert systems with applications** · 3 cites · *unreviewed*
- **[MedGemma Technical Report](https://arxiv.org/abs/2507.05201)** — 2025-07 · 416 cites · *unreviewed*
- **[MOTOR: Multimodal Optimal Transport via Grounded Retrieval in Medical Visual Question Answering](https://arxiv.org/abs/2506.22900)** — 2025-06 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 10 cites · *unreviewed*
- **[Thought Graph Traversal for Test-time Scaling in Chest X-ray VLLMs](https://arxiv.org/abs/2506.11989)** — 2025-06 · **Pattern Recognition** · 5 cites · *unreviewed*
- **[Lingshu: A Generalist Foundation Model for Unified Multimodal Medical Understanding and Reasoning](https://arxiv.org/abs/2506.07044)** — 2025-06 · 212 cites · *unreviewed*
- **[DrVD-Bench: Do Vision-Language Models Reason Like Human Doctors in Medical Image Diagnosis?](https://arxiv.org/abs/2505.24173)** — 2025-05 · **Advances in Neural Information Processing Systems 38** · 12 cites · *unreviewed*
- **[Are Vision Language Models Ready for Clinical Diagnosis? A 3D Medical Benchmark for Tumor-centric Visual Question Answering](https://arxiv.org/abs/2505.18915)** — 2025-05 · 17 cites · *unreviewed*
- **[CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays](https://arxiv.org/abs/2505.18087)** — 2025-05 · **Neural Information Processing Systems** · 5 cites · *unreviewed*
- **[RadZero: Similarity-Based Cross-Attention for Explainable Vision-Language Alignment in Chest X-ray with Zero-Shot Multi-Task Capability](https://arxiv.org/abs/2504.07416)** — 2025-04 · **Neural Information Processing Systems** · 6 cites · *unreviewed*
- **[Med3DVLM: An Efficient Vision-Language Model for 3D Medical Image Analysis](https://arxiv.org/abs/2503.20047)** — 2025-03 · **IEEE journal of biomedical and health informatics** · 60 cites · *unreviewed*
- **[Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://arxiv.org/abs/2503.16616)** — 2025-03 · **IEEE International Conference on Computer Vision** · 4 cites · *unreviewed*
- **[MedVLM-R1: Incentivizing Medical Reasoning Capability of Vision-Language Models (VLMs) via Reinforcement Learning](https://arxiv.org/abs/2502.19634)** — 2025-02 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 204 cites · *unreviewed*
- **[RadAlign: Advancing Radiology Report Generation with Vision-Language Concept Alignment](https://arxiv.org/abs/2501.07525)** — 2025-01 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 23 cites · *unreviewed*
- **[Libra: Leveraging Temporal Images for Biomedical Radiology Analysis](https://arxiv.org/abs/2411.19378)** — 2024-11 · **Annual Meeting of the Association for Computational Linguistics** · 33 cites · *unreviewed*
- **[MAIRA-Seg: Enhancing Radiology Report Generation with Segmentation-Aware Multimodal Large Language Models](https://arxiv.org/abs/2411.11362)** — 2024-11 · **ML4H@NeurIPS** · 11 cites · *unreviewed*
- **[R-LLaVA: Improving Med-VQA Understanding through Visual Region of Interest](https://arxiv.org/abs/2410.20327)** — 2024-10
  <sub>Injects clinician-prior regions of interest into Med-VQA so answers are anchored to specific image regions.</sub>
- **[CheXalign: Preference fine-tuning in chest X-ray interpretation models without human feedback](https://arxiv.org/abs/2410.07025)** — 2024-10 · **Annual Meeting of the Association for Computational Linguistics** · 8 cites · *unreviewed*
- **[MC-CoT: A Modular Collaborative CoT Framework for Zero-shot Medical-VQA with LLM and MLLM Integration](https://arxiv.org/abs/2410.04521)** — 2024-10 · 28 cites · *unreviewed*
- **[An X-Ray Is Worth 15 Features: Sparse Autoencoders for Interpretable Radiology Report Generation](https://arxiv.org/abs/2410.03334)** — 2024-10 · 27 cites · *unreviewed*
- **[KARGEN: Knowledge-enhanced Automated Radiology Report Generation Using Large Language Models](https://arxiv.org/abs/2409.05370)** — 2024-09 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 17 cites · *unreviewed*
- **[M4CXR: Exploring Multi-task Potentials of Multi-modal Large Language Models for Chest X-ray Interpretation](https://arxiv.org/abs/2408.16213)** — 2024-08 · **IEEE Transactions on Neural Networks and Learning Systems** · 24 cites · *unreviewed*
- **[Beyond the Hype: A dispassionate look at vision-language models in medical scenario](https://arxiv.org/abs/2408.08704)** — 2024-08 · **IEEE Transactions on Neural Networks and Learning Systems** · 16 cites · *unreviewed*
- **[GPT-4V Cannot Generate Radiology Reports Yet](https://arxiv.org/abs/2407.12176)** — 2024-07 · **North American Chapter of the Association for Computational Linguistics** · 10 cites · *unreviewed*
- **[CXR-Agent: Vision-language models for chest X-ray interpretation with uncertainty aware radiology reporting](https://arxiv.org/abs/2407.08811)** — 2024-07 · 18 cites · *unreviewed*
- **[Evidential Concept Embedding Models: Towards Reliable Concept Explanations for Skin Disease Diagnosis](https://arxiv.org/abs/2406.19130)** — 2024-06 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 9 cites · *unreviewed*
- **[FPN-IAIA-BL: A Multi-Scale Interpretable Deep Learning Model for Classification of Mass Margins in Digital Mammography](https://arxiv.org/abs/2406.06386)** — 2024-06 · **2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)** · 5 cites · *unreviewed*

### Pathology & Whole-Slide Reasoning · 病理与全切片推理 <sub>17</sub>

- **[PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image](https://arxiv.org/abs/2607.19261)** — 2026-07 · 2 cites · *unreviewed*
- **[ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/abs/2606.17730)** — 2026-06 · 4 cites · *unreviewed*
- **[Learnable Token Sparsification for Efficient Gigapixel Whole Slide Image Reasoning](https://arxiv.org/abs/2606.08641)** — 2026-06 · 2 cites · *unreviewed*
- **[MedGemma 1.5 Technical Report](https://arxiv.org/abs/2604.05081)** — 2026-04 · 23 cites · *unreviewed*
- **[MIRAGE: The Illusion of Visual Understanding](https://arxiv.org/abs/2603.21687)** — 2026-03 · 45 cites · *unreviewed*
- **[Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)** — 2026-03 · 6 cites · *unreviewed*
- **[TC-SSA: Token Compression via Semantic Slot Aggregation for Gigapixel Pathology Reasoning](https://arxiv.org/abs/2603.01143)** — 2026-03 · 16 cites · *unreviewed*
- **[Histopath-C: Towards Realistic Domain Shifts for Histopathology Vision-Language Adaptation](https://arxiv.org/abs/2601.12493)** — 2026-01 · **IEEE Workshop/Winter Conference on Applications of Computer Vision** · 3 cites · *unreviewed*
- **[PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning](https://arxiv.org/abs/2511.17052)** — 2025-11 · 15 cites · *unreviewed*
- **[Augmentation-based Domain Generalization and Joint Training from Multiple Source Domains for Whole Heart Segmentation](https://arxiv.org/abs/2508.04552)** — 2025-08 · **CARE@MICCAI** · 3 cites · *unreviewed*
- **[Evidence-based diagnostic reasoning with multi-agent copilot for human pathology](https://arxiv.org/abs/2506.20964)** — 2025-06 · 26 cites · *unreviewed*
- **[Historical Report Guided Bi-modal Concurrent Learning for Pathology Report Generation](https://arxiv.org/abs/2506.18658)** — 2025-06 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 7 cites · *unreviewed*
- **[RadFabric: Agentic AI System with Reasoning Capability for Radiology](https://arxiv.org/abs/2506.14142)** — 2025-06 · 10 cites · *unreviewed*
- **[PRISM2: Unlocking Multi-Modal General Pathology AI with Clinical Dialogue](https://arxiv.org/abs/2506.13063)** — 2025-06 · 12 cites · *unreviewed*
- **[CoC: Chain-of-Cancer based on Cross-Modal Autoregressive Traction for Survival Prediction](https://arxiv.org/abs/2506.15696)** — 2025-05 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 3 cites · *unreviewed*
- **[CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://arxiv.org/abs/2505.20510)** — 2025-05 · **Neural Information Processing Systems** · 26 cites · *unreviewed*
- **[GRAPHITE: Graph-Based Interpretable Tissue Examination for Enhanced Explainability in Breast Cancer Histopathology](https://arxiv.org/abs/2501.04206)** — 2025-01 · **Comput. Biol. Medicine** · 6 cites · *unreviewed*

### Cross-Modal Fusion & Modality Generalization · 跨模态融合与模态泛化 <sub>7</sub>

- **[Resource-Efficient Iterative LLM-Based NAS with Feedback Memory](https://arxiv.org/abs/2603.12091)** — 2026-03 · 12 cites · *unreviewed*
- **[ECG-R1: Protocol-Guided and Modality-Agnostic MLLM for Reliable ECG Interpretation](https://arxiv.org/abs/2602.04279)** — 2026-02 · 11 cites · *unreviewed*
- **[EEG-VLM: A Hierarchical Vision-Language Model with Multi-Level Feature Alignment and Visually Enhanced Language-Guided Reasoning for EEG Image-Based Sleep Stage Prediction](https://arxiv.org/abs/2511.19155)** — 2025-11 · **IEEE journal of biomedical and health informatics** · 4 cites · *unreviewed*
- **[Constructing Ophthalmic MLLM for Positioning-diagnosis Collaboration Through Clinical Cognitive Chain Reasoning](https://arxiv.org/abs/2507.17539)** — 2025-07 · **IEEE International Conference on Computer Vision** · 9 cites · *unreviewed*
- **[InsertRank: LLMs can reason over BM25 scores to Improve Listwise Reranking](https://arxiv.org/abs/2506.14086)** — 2025-06 · **WSDM Companion** · 4 cites · *unreviewed*
- **[Test-time Adaptation for Foundation Medical Segmentation Model without Parametric Updates](https://arxiv.org/abs/2504.02008)** — 2025-04 · **IEEE International Conference on Computer Vision** · 8 cites · *unreviewed*
- **[MotionTTT: 2D Test-Time-Training Motion Estimation for 3D Motion Corrected MRI](https://arxiv.org/abs/2409.09370)** — 2024-09 · **Neural Information Processing Systems** · 4 cites · *unreviewed*

## 🩺 Agentic Diagnostic Reasoning · 智能体式诊断推理

> Multi-turn, multi-role, tool-using diagnostic reasoning. Only works with a novel reasoning mechanism — plain pipeline orchestration is out of scope.  
> <sub>多轮、多角色、可调用工具的诊断推理。只收推理机制有创新的工作，纯流程编排不收。</sub>

### Interactive & Proactive Diagnostic Reasoning · 交互式与主动式诊断推理 <sub>23</sub>

- **[CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures](https://arxiv.org/abs/2605.25338)** — 2026-05 · 3 cites · *unreviewed*
- **[Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models](https://arxiv.org/abs/2604.08545)** — 2026-04 · 10 cites · *unreviewed*
- **[XrayClaw: Cooperative-Competitive Multi-Agent Alignment for Trustworthy Chest X-ray Diagnosis](https://arxiv.org/abs/2604.02695)** — 2026-04 · 6 cites · *unreviewed*
- **[Meissa: Multi-modal Medical Agentic Intelligence](https://arxiv.org/abs/2603.09018)** — 2026-03 · 5 cites · *unreviewed*
- **[Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search](https://arxiv.org/abs/2603.01692)** — 2026-03 · **Annual Meeting of the Association for Computational Linguistics** · 3 cites · *unreviewed*
- **[Do Mixed-Vendor Multi-Agent LLMs Improve Clinical Diagnosis?](https://arxiv.org/abs/2603.04421)** — 2026-02 · **Proceedings of the 1st Workshop on Linguistic Analysis for Health (HeaLing 2026)** · 3 cites · *unreviewed*
- **[LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis](https://arxiv.org/abs/2602.09379)** — 2026-02 · **Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2** · 5 cites · *unreviewed*
- **[DemMA: Dementia Multi-Turn Dialogue Agent with Expert-Guided Reasoning and Action Simulation](https://arxiv.org/abs/2601.06373)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 3 cites · *unreviewed*
- **[MedDialogRubrics: A Comprehensive Benchmark and Evaluation Framework for Multi-turn Medical Consultations in Large Language Models](https://arxiv.org/abs/2601.03023)** — 2026-01 · 11 cites · *unreviewed*
- **[DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning](https://arxiv.org/abs/2512.07132)** — 2025-12 · **Conference of the European Chapter of the Association for Computational Linguistics** · 4 cites · *unreviewed*
- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)** — 2025-11 · **AAAI Conference on Artificial Intelligence** · 6 cites · *unreviewed*
- **[MedCoAct: Confidence-Aware Multi-Agent Collaboration for Complete Clinical Decision](https://arxiv.org/abs/2510.10461)** — 2025-10 · **IEEE International Conference on Bioinformatics and Biomedicine** · 4 cites · *unreviewed*
- **[MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models](https://arxiv.org/abs/2509.23725)** — 2025-09 · **AAAI Conference on Artificial Intelligence** · 12 cites · *unreviewed*
- **[Automated Clinical Problem Detection from SOAP Notes using a Collaborative Multi-Agent LLM Architecture](https://arxiv.org/abs/2508.21803)** — 2025-08 · **ACM International Conference on Bioinformatics, Computational Biology and Biomedicine** · 5 cites · *unreviewed*
- **[KERAP: A Knowledge-Enhanced Reasoning Approach for Accurate Zero-shot Diagnosis Prediction Using Multi-agent LLMs](https://arxiv.org/abs/2507.02773)** — 2025-07 · **AMIA ... Annual Symposium proceedings. AMIA Symposium** · 15 cites · *unreviewed*
- **[MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555)** — 2025-05 · 42 cites · *unreviewed*
- **[A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law](https://arxiv.org/abs/2505.02665)** — 2025-05 · 20 cites · *unreviewed*
- **[MAGI: Multi-Agent Guided Interview for Psychiatric Assessment](https://arxiv.org/abs/2504.18260)** — 2025-04 · **Annual Meeting of the Association for Computational Linguistics** · 19 cites · *unreviewed*
- **[From Metaphor to Mechanism: How LLMs Decode Traditional Chinese Medicine Symbolic Language for Modern Clinical Relevance](https://arxiv.org/abs/2503.02760)** — 2025-03 · **IEEE International Joint Conference on Neural Network** · 6 cites · *unreviewed*
- **[MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://arxiv.org/abs/2502.19175)** — 2025-02 · **Annual Meeting of the Association for Computational Linguistics** · 26 cites · *unreviewed*
- **[Enhancing Hepatopathy Clinical Trial Efficiency: A Secure, Large Language Model-Powered Pre-Screening Pipeline](https://arxiv.org/abs/2502.18531)** — 2025-02 · **BioData Mining** · 7 cites · *unreviewed*
- **[Nuclear Deployed: Analyzing Catastrophic Risks in Decision-making of Autonomous LLM Agents](https://arxiv.org/abs/2502.11355)** — 2025-02 · **Annual Meeting of the Association for Computational Linguistics** · 31 cites · *unreviewed*
- **[Superhuman performance of a large language model on the reasoning tasks of a physician](https://arxiv.org/abs/2412.10849)** — 2024-12 · 83 cites · *unreviewed*

## 📊 Evaluation, Benchmarks & Trustworthiness · 评测、基准与可信度

> Is the reasoning gain real? The section this list most wants to get right.  
> <sub>推理增益是真的吗？这一节是本仓库最想做扎实的部分。</sub>

### Reasoning Benchmarks & Datasets · 推理基准与数据集 <sub>81</sub>

- **[PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?](https://arxiv.org/abs/2607.28318)** — 2026-07 · 1 cites · *unreviewed*
- **[Can Multimodal Large Language Models Understand OCT?](https://arxiv.org/abs/2607.16609)** — 2026-07 · 2 cites · *unreviewed*
- **[Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)** — 2026-07 · 4 cites · *unreviewed*
- **[TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480)** — 2026-07 · 1 cites · *unreviewed*
- **[Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](https://arxiv.org/abs/2607.10805)** — 2026-07 · 2 cites · *unreviewed*
- **[CLIR-Bench: Benchmarking Multimodal Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.09880)** — 2026-07 · 2 cites · *unreviewed*
- **[OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](https://arxiv.org/abs/2607.08423)** — 2026-07 · 1 cites · *unreviewed*
- **[Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical Reasoning](https://arxiv.org/abs/2607.07761)** — 2026-07 · **Machine Intelligence Research** · 3 cites · *unreviewed*
- **[Overview of the NLPCC 2026 Shared Task 1: Difficulty-Aware Multilingual and Multimodal Medical Instructional Video Understanding Evaluation](https://arxiv.org/abs/2607.06618)** — 2026-07 · 2 cites · *unreviewed*
- **[EHR-Complex: Benchmarking Medical Agents for Complex Clinical Reasoning](https://arxiv.org/abs/2606.23301)** — 2026-06 · 2 cites · *unreviewed*
- **[Watch, Remember, Reason: Human-View Video Understanding with MLLMs](https://arxiv.org/abs/2606.07433)** — 2026-06 · 2 cites · *unreviewed*
- **[Artifact-Bench: Evaluating MLLMs on Detecting and Assessing the Artifacts of AI-Generated Videos](https://arxiv.org/abs/2605.18984)** — 2026-05 · 3 cites · *unreviewed*
- **[VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](https://arxiv.org/abs/2605.08146)** — 2026-05 · 3 cites · *unreviewed*
- **[Reasoning emerges from constrained inference manifolds in large language models](https://arxiv.org/abs/2605.08142)** — 2026-05 · 6 cites · *unreviewed*
- **[Medical thinking with multiple images](https://arxiv.org/abs/2604.16506)** — 2026-04 · 6 cites · *unreviewed*
- **[Finding and Reactivating Post-Trained LLMs' Hidden Safety Mechanisms](https://arxiv.org/abs/2604.00012)** — 2026-03 · **Neural Information Processing Systems** · 3 cites · *unreviewed*
- **[MediX-R1: Open Ended Medical Reinforcement Learning](https://arxiv.org/abs/2602.23363)** — 2026-02 · 6 cites · *unreviewed*
- **[MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955)** — 2026-02
  <sub>MRI brain-tumor benchmark that requires reasoning tied to imaging manifestations, not just the diagnostic label.</sub>
- **[LeafNet: A Large-Scale Dataset and Comprehensive Benchmark for Foundational Vision-Language Understanding of Plant Diseases](https://arxiv.org/abs/2602.13662)** — 2026-02 · 7 cites · *unreviewed*
- **[LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation](https://arxiv.org/abs/2602.10367)** — 2026-02 · 7 cites · *unreviewed*
- **[EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories](https://arxiv.org/abs/2602.03569)** — 2026-02 · 8 cites · *unreviewed*
- **[Who Endorsed It? Measuring Authority Bias Across Expertise Levels in Language Models](https://arxiv.org/abs/2601.13433)** — 2026-01 · **IEEE Games Entertainment Media Conference** · 3 cites · *unreviewed*
- **[Patient-Similarity Cohort Reasoning in Clinical Text-to-SQL](https://arxiv.org/abs/2601.09876)** — 2026-01 · **Conference of the European Chapter of the Association for Computational Linguistics** · 3 cites · *unreviewed*
- **[Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://arxiv.org/abs/2601.08763)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 9 cites · *unreviewed*
- **[OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning](https://arxiv.org/abs/2511.23269)** — 2025-11 · 9 cites · *unreviewed*
- **[OralGPT-Omni: A Versatile Dental Multimodal Large Language Model](https://arxiv.org/abs/2511.22055)** — 2025-11 · 10 cites · *unreviewed*
- **[BioMedSearch: A Multi-Source Biomedical Retrieval Framework Based on LLMs](https://arxiv.org/abs/2510.13926)** — 2025-10 · **IEEE International Conference on Bioinformatics and Biomedicine** · 5 cites · *unreviewed*
- **[Simulating Viva Voce Examinations to Evaluate Clinical Reasoning in Large Language Models](https://arxiv.org/abs/2510.10278)** — 2025-10 · **Neural Information Processing Systems** · 6 cites · *unreviewed*
- **[A Chain-of-thought Reasoning Breast Ultrasound Dataset Covering All Histopathology Categories](https://arxiv.org/abs/2509.17046)** — 2025-09 · **Scientific Data** · 6 cites · *unreviewed*
- **[DischargeSim: A Simulation Benchmark for Educational Doctor-Patient Communication at Discharge](https://arxiv.org/abs/2509.07188)** — 2025-09 · **Conference on Empirical Methods in Natural Language Processing** · 7 cites · *unreviewed*
- **[PsychiatryBench: A Multi-Task Benchmark for LLMs in Psychiatry](https://arxiv.org/abs/2509.09711)** — 2025-09 · **npj Digit. Medicine** · 5 cites · *unreviewed*
- **[Baichuan-M2: Scaling Medical Capability with Large Verifier System](https://arxiv.org/abs/2509.02208)** — 2025-09 · 49 cites · *unreviewed*
- **[Exploring Efficiency Frontiers of Thinking Budget in Medical Reasoning: Scaling Laws between Computational Resources and Reasoning Quality](https://arxiv.org/abs/2508.12140)** — 2025-08 · **Journal of Biomedical Informatics** · 5 cites · *unreviewed*
- **[Capabilities of GPT-5 on Multimodal Medical Reasoning](https://arxiv.org/abs/2508.08224)** — 2025-08 · **Medical Imaging** · 80 cites · *unreviewed*
- **[Neovascularization Segmentation via a Multilateral Interaction-Enhanced Graph Convolutional Network](https://arxiv.org/abs/2508.03197)** — 2025-08 · **IEEE Transactions on Pattern Analysis and Machine Intelligence** · 4 cites · *unreviewed*
- **[ReXGroundingCT: A 3D Chest CT Dataset for Segmentation of Findings from Free-Text Reports](https://arxiv.org/abs/2507.22030)** — 2025-07 · **NEJM AI** · 18 cites · *unreviewed*
- **[Single Image Test-Time Adaptation via Multi-View Co-Training](https://arxiv.org/abs/2506.23705)** — 2025-06 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 4 cites · *unreviewed*
- **[Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search](https://arxiv.org/abs/2506.16962)** — 2025-06 · **Neural Information Processing Systems** · 15 cites · *unreviewed*
- **[Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models](https://arxiv.org/abs/2506.13206)** — 2025-06 · 64 cites · *unreviewed*
- **[Med-U1: Incentivizing Unified Medical Reasoning in LLMs via Large-scale Reinforcement Learning](https://arxiv.org/abs/2506.12307)** — 2025-06 · 11 cites · *unreviewed*
- **[ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://arxiv.org/abs/2506.09513)** — 2025-06 · **Conference on Empirical Methods in Natural Language Processing** · 28 cites · *unreviewed*
- **[3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](https://arxiv.org/abs/2506.11147)** — 2025-06 · **Neural Information Processing Systems** · 23 cites
  <sub>3D radiology Med-VQA dataset with multi-temporal comparison tasks, moving the reasoning load from a single frame to a time series.</sub>
- **[Kvasir-VQA-x1: A Multimodal Dataset for Medical Reasoning and Robust MedVQA in Gastrointestinal Endoscopy](https://arxiv.org/abs/2506.09958)** — 2025-06 · **DEMI@MICCAI** · 18 cites · *unreviewed*
- **[SRPL-SFDA: SAM-Guided Reliable Pseudo-Labels for Source-Free Domain Adaptation in Medical Image Segmentation](https://arxiv.org/abs/2506.09403)** — 2025-06 · **Neurocomputing** · 14 cites · *unreviewed*
- **[Artificial Intelligence Should Genuinely Support Clinical Reasoning and Decision Making To Bridge the Translational Gap](https://arxiv.org/abs/2506.05030)** — 2025-06 · **npj Digital Medicine** · 75 cites · *unreviewed*
- **[ReXVQA: A Large-scale Visual Question Answering Benchmark for Generalist Chest X-ray Understanding](https://arxiv.org/abs/2506.04353)** — 2025-06 · **Pacific Symposium on Biocomputing. Pacific Symposium on Biocomputing** · 23 cites · *unreviewed*
- **[DeepSeek in Healthcare: A Survey of Capabilities, Risks, and Clinical Applications of Open-Source Large Language Models](https://arxiv.org/abs/2506.01257)** — 2025-06 · 14 cites · *unreviewed*
- **[Medical Large Vision Language Models with Multi-Image Visual Ability](https://arxiv.org/abs/2505.19031)** — 2025-05 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 15 cites · *unreviewed*
- **[Point, Detect, Count: Multi-Task Medical Image Understanding with Instruction-Tuned Vision-Language Models](https://arxiv.org/abs/2505.16647)** — 2025-05 · **2025 IEEE 38th International Symposium on Computer-Based Medical Systems (CBMS)** · 3 cites · *unreviewed*
- **[Beyond Empathy: Integrating Diagnostic and Therapeutic Reasoning with Large Language Models for Mental Health Counseling](https://arxiv.org/abs/2505.15715)** — 2025-05 · 21 cites · *unreviewed*
- **[DiagnosisArena: Benchmarking Diagnostic Reasoning for Large Language Models](https://arxiv.org/abs/2505.14107)** — 2025-05 · **Annual Meeting of the Association for Computational Linguistics** · 16 cites · *unreviewed*
- **[NOVA: A Benchmark for Anomaly Localization and Clinical Reasoning in Brain MRI](https://arxiv.org/abs/2505.14064)** — 2025-05 · 16 cites · *unreviewed*
- **[MedCaseReasoning: Evaluating and learning diagnostic reasoning from clinical case reports](https://arxiv.org/abs/2505.11733)** — 2025-05 · 28 cites · *unreviewed*
- **[Disentangling Reasoning and Knowledge in Medical Large Language Models](https://arxiv.org/abs/2505.11462)** — 2025-05 · 17 cites · *unreviewed*
- **[CaReAQA: A Cardiac and Respiratory Audio Question Answering Model for Open-Ended Diagnostic Reasoning](https://arxiv.org/abs/2505.01199)** — 2025-05 · **ACM Conference on Health, Inference, and Learning** · 10 cites · *unreviewed*
- **[LLM Sensitivity Evaluation Framework for Clinical Diagnosis](https://arxiv.org/abs/2504.13475)** — 2025-04 · **International Conference on Computational Linguistics** · 8 cites · *unreviewed*
- **[UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://arxiv.org/abs/2504.06908)** — 2025-04 · **IEEE International Conference on Computer Vision** · 4 cites · *unreviewed*
- **[MedReason: Eliciting Factual Medical Reasoning Steps in LLMs via Knowledge Graphs](https://arxiv.org/abs/2504.00993)** — 2025-04 · 107 cites · *unreviewed*
- **[Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://arxiv.org/abs/2503.22678)** — 2025-03 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 43 cites · *unreviewed*
- **[MDTeamGPT: A Self-Evolving LLM-based Multi-Agent Framework for Multi-Disciplinary Team Medical Consultation](https://arxiv.org/abs/2503.13856)** — 2025-03 · 31 cites · *unreviewed*
- **[Test-Time Domain Generalization via Universe Learning: A Multi-Graph Matching Approach for Medical Image Segmentation](https://arxiv.org/abs/2503.13012)** — 2025-03 · **Computer Vision and Pattern Recognition** · 7 cites · *unreviewed*
- **[SurgRAW: Multi-Agent Workflow with Chain of Thought Reasoning for Robotic Surgical Video Analysis](https://arxiv.org/abs/2503.10265)** — 2025-03 · **IEEE Robotics and Automation Letters** · 18 cites · *unreviewed*
- **[MedicalAgentsBench for Complex Medical Reasoning: Comparing Internalized Reasoning Models versus Externalized Agent-based Frameworks](https://arxiv.org/abs/2503.07459)** — 2025-03 · **Patterns** · 44 cites · *unreviewed*
- **[Citrus: Leveraging Expert Cognitive Pathways in a Medical Language Model for Advanced Medical Decision Support](https://arxiv.org/abs/2502.18274)** — 2025-02 · 16 cites · *unreviewed*
- **[Limitations of Large Language Models in Clinical Problem-Solving Arising from Inflexible Reasoning](https://arxiv.org/abs/2502.04381)** — 2025-02 · **Scientific Reports** · 91 cites · *unreviewed*
- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)** — 2025-02 · **International Conference on Machine Learning** · 68 cites · *unreviewed*
- **[MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://arxiv.org/abs/2501.18362)** — 2025-01 · **International Conference on Machine Learning** · 217 cites · *unreviewed*
- **[FineMedLM-o1: Enhancing Medical Knowledge Reasoning Ability of LLM from Supervised Fine-Tuning to Test-Time Training](https://arxiv.org/abs/2501.09213)** — 2025-01 · 12 cites · *unreviewed*
- **[SAM-DA: Decoder Adapter for Efficient Medical Domain Adaptation](https://arxiv.org/abs/2501.06836)** — 2025-01 · **IEEE Workshop/Winter Conference on Applications of Computer Vision** · 6 cites · *unreviewed*
- **[MedMobile: A mobile-sized language model with clinical capabilities](https://arxiv.org/abs/2410.09019)** — 2024-10 · **BMJ Digital Health &amp; AI** · 7 cites · *unreviewed*
- **[CliMedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models in Clinical Scenarios](https://arxiv.org/abs/2410.03502)** — 2024-10 · **Conference on Empirical Methods in Natural Language Processing** · 18 cites · *unreviewed*
- **[MedViLaM: A multimodal large language model with advanced generalizability and explainability for medical data understanding and generation](https://arxiv.org/abs/2409.19684)** — 2024-09 · 20 cites · *unreviewed*
- **[A Preliminary Study of o1 in Medicine: Are We Closer to an AI Doctor?](https://arxiv.org/abs/2409.15277)** — 2024-09 · 51 cites · *unreviewed*
- **[MAGDA: Multi-agent guideline-driven diagnostic assistance](https://arxiv.org/abs/2409.06351)** — 2024-09 · **MedAGI@MICCAI** · 12 cites · *unreviewed*
- **[Gradient Alignment Improves Test-Time Adaptation for Medical Image Segmentation](https://arxiv.org/abs/2408.07343)** — 2024-08 · **AAAI Conference on Artificial Intelligence** · 17 cites · *unreviewed*
- **[LADDER: Language-Driven Slice Discovery and Error Rectification in Vision Classifiers](https://arxiv.org/abs/2408.07832)** — 2024-07 · **Annual Meeting of the Association for Computational Linguistics** · 7 cites · *unreviewed*
- **[Learning 3D Gaussians for Extremely Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2407.01090)** — 2024-07 · **International Conference on Medical Image Computing and Computer-Assisted Intervention** · 26 cites · *unreviewed*
- **[Test-time generative augmentation for medical image segmentation](https://arxiv.org/abs/2406.17608)** — 2024-06 · **Medical Image Anal.** · 10 cites · *unreviewed*
- **[BayTTA: Uncertainty-aware medical image classification with optimized test-time augmentation using Bayesian model averaging](https://arxiv.org/abs/2406.17640)** — 2024-06 · **Knowledge-Based Systems** · 9 cites · *unreviewed*
- **[Reasoning Like a Doctor: Improving Medical Dialogue Systems via Diagnostic Reasoning Process Alignment](https://arxiv.org/abs/2406.13934)** — 2024-06 · **Annual Meeting of the Association for Computational Linguistics** · 29 cites · *unreviewed*
- **[Comparative Benchmarking of Failure Detection Methods in Medical Image Segmentation: Unveiling the Role of Confidence Aggregation](https://arxiv.org/abs/2406.03323)** — 2024-06 · **Medical Image Anal.** · 23 cites · *unreviewed*

### Faithfulness, Hallucination & Shortcut Learning · 忠实性、幻觉与捷径学习 <sub>9</sub>

- **[Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decoding](https://arxiv.org/abs/2606.27596)** — 2026-06 · 2 cites · *unreviewed*
- **[Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492)** — 2026-05
  <sub>Adversarial benchmark with hierarchical perturbations: tests whether a VLM's answer rests on image evidence or on spurious priors.</sub>
- **[Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance](https://arxiv.org/abs/2508.13579)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 5 cites · *unreviewed*
- **[Reasoning in Computer Vision: Taxonomy, Models, Tasks, and Methodologies](https://arxiv.org/abs/2508.10523)** — 2025-08 · 25 cites · *unreviewed*
- **[Neurosymbolic Reasoning Shortcuts under the Independence Assumption](https://arxiv.org/abs/2507.11357)** — 2025-07 · **International Workshop on Neural-Symbolic Learning and Reasoning** · 3 cites · *unreviewed*
- **[DeVisE: Behavioral Testing of Medical Large Language Models](https://arxiv.org/abs/2506.15339)** — 2025-06 · **Conference of the European Chapter of the Association for Computational Linguistics** · 3 cites · *unreviewed*
- **[Spurious Correlations and Beyond: Understanding and Mitigating Shortcut Learning in SDOH Extraction with Large Language Models](https://arxiv.org/abs/2506.00134)** — 2025-05 · **Annual Meeting of the Association for Computational Linguistics** · 4 cites · *unreviewed*
- **[Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://arxiv.org/abs/2503.06169)** — 2025-03 · **Conference on Empirical Methods in Natural Language Processing** · 32 cites · *unreviewed*
- **[Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://arxiv.org/abs/2410.15460)** — 2024-10 · **Annual Meeting of the Association for Computational Linguistics** · 5 cites · *unreviewed*

### Clinical Alignment & Human-AI Evaluation · 临床对齐与人机协同评估 <sub>10</sub>

- **[Information-seeking failures of large language models in agentic clinical reasoning](https://arxiv.org/abs/2607.10275)** — 2026-07 · 1 cites · *unreviewed*
- **[A prospective clinical feasibility study of a conversational diagnostic AI in an ambulatory primary care clinic](https://arxiv.org/abs/2603.08448)** — 2026-03 · 7 cites · *unreviewed*
- **[Diagnosing and Mitigating Sycophancy and Skepticism in LLM Causal Judgment](https://arxiv.org/abs/2601.08258)** — 2026-01 · **Annual Meeting of the Association for Computational Linguistics** · 10 cites · *unreviewed*
- **[Foundation Models in Biomedical Imaging: Turning Hype into Reality](https://arxiv.org/abs/2512.15808)** — 2025-12 · **Nature Biomedical Engineering** · 7 cites · *unreviewed*
- **[Reliability of Large Language Model Generated Clinical Reasoning in Assisted Reproductive Technology: Blinded Comparative Evaluation Study](https://arxiv.org/abs/2510.16095)** — 2025-10 · **Journal of Medical Internet Research** · 5 cites · *unreviewed*
- **[Leveraging Imperfection with MEDLEY A Multi-Model Approach Harnessing Bias in Medical AI](https://arxiv.org/abs/2508.21648)** — 2025-08 · **Frontiers Artif. Intell.** · 5 cites · *unreviewed*
- **[PASS: Probabilistic Agentic Supernet Sampling for Interpretable and Adaptive Chest X-Ray Reasoning](https://arxiv.org/abs/2508.10501)** — 2025-08 · **AAAI Conference on Artificial Intelligence** · 4 cites · *unreviewed*
- **[Automating Expert-Level Medical Reasoning Evaluation of Large Language Models](https://arxiv.org/abs/2507.07988)** — 2025-07 · **npj Digital Medicine** · 30 cites · *unreviewed*
- **[Medical Hallucinations in Foundation Models and Their Impact on Healthcare](https://arxiv.org/abs/2503.05777)** — 2025-02 · 157 cites · *unreviewed*
- **[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question Answering](https://arxiv.org/abs/2412.17701)** — 2024-12 · **International Conference on Learning Representations** · 3 cites · *unreviewed*

## 📚 Surveys & Position Papers · 综述与立场文章

### Surveys & Positions · 综述与立场 <sub>9</sub>

- **[Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation](https://arxiv.org/abs/2605.27115)** — 2026-05 · 3 cites · *unreviewed*
- **[PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://arxiv.org/abs/2605.02240)** — 2026-05 · 9 cites · *unreviewed*
- **[Prompt-based Adaptation in Large-scale Vision Models: A Survey](https://arxiv.org/abs/2510.13219)** — 2025-10 · **Trans. Mach. Learn. Res.** · 27 cites · *unreviewed*
- **[Reasoning LLMs in the Medical Domain: A Literature Survey](https://arxiv.org/abs/2508.19097)** — 2025-08 · **International Conference on Data Science and Advanced Analytics** · 6 cites · *unreviewed*
- **[Medical Reasoning in the Era of LLMs: A Systematic Review of Enhancement Techniques and Applications](https://arxiv.org/abs/2508.00669)** — 2025-08 · 14 cites · *unreviewed*
- **[Keeping Medical AI Healthy and Trustworthy: A Review of Detection and Correction Methods for System Degradation](https://arxiv.org/abs/2506.17442)** — 2025-06 · **IEEE transactions on bio-medical engineering** · 15 cites · *unreviewed*
- **[MediSee: Reasoning-based Pixel-level Perception in Medical Images](https://arxiv.org/abs/2504.11008)** — 2025-04 · **ACM Multimedia** · 13 cites · *unreviewed*
- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)** — 2025-02 · **Annual Meeting of the Association for Computational Linguistics** · 135 cites · *unreviewed*
- **[Evaluation of OpenAI o1: Opportunities and Challenges of AGI](https://arxiv.org/abs/2409.18486)** — 2024-09 · 172 cites · *unreviewed*


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

**What *unreviewed* means.** Entries carrying that marker cleared the quality bar but have not yet had a
close read; their category is a keyword-based guess and they carry no annotation. Entries without the marker
have been read, placed, and annotated by hand. The distinction is kept visible rather than smoothed over.

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
