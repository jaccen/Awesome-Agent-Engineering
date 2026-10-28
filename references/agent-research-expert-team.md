# AI/Agent 论文科研专家团

> 编制日期：2026-10-28 · 用途：Awesome-Agent-Engineering 科研辅导体系
> 与 [`agent-research-areas.md`](agent-research-areas.md) 互补：领域图谱给"16 研究方向骨架"，本文给"科研协作流程 + 期刊论文 + 辅导角色"
> 参照 Awesome-Gaussian-Skills 的 research-expert-team 模式（9 角色 R1-R9），针对 AI/Agent 领域适配

---

## 0. 定位

AI/Agent 是一个横跨感知—认知—行动—学习—治理的全栈研究领域，论文产出速度快、子领域多、跨学科性强。本专家团的作用是：**帮助研究者做出一个经得起检验的下一步决策**——从选题评估到投稿检查，覆盖论文全生命周期。

角色名称用于组织检查项，不暗示独立的人类专家、额外工具或真实同行评审。按需取用，一个简短的 idea 问题不需要九阶段报告。

---

## 1. 科研协作角色体系（R1-R9）

| 角色 | 要回答的问题 | 期望输出 |
|---|---|---|
| **R1 — 选题评估员** | 这能教给我们什么，什么会让它失败？ | 最近相关工作、有界的检索边界、假设、可行性与未解风险 |
| **R2 — 贡献分析员** | 相对最近的方法，究竟改变了什么？ | 一个有界的差异声明 + 一个能反驳它的测试；不做泛化的新颖性排名 |
| **R3 — 批判审稿员** | 草稿支持哪些结论？ | 定位观察、后果、不确定性与可行补救；证据变化时修订异议 |
| **R4 — 学术编辑** | 读者能理解论证吗？ | 更清晰的行文 + 追踪实质性修改；不静默增强 claim |
| **R5 — 出版诚信编辑** | 署名、披露与出处是否准确？ | 一致的引用、匿名化与许可来源清理；保留必要的 AI 使用披露 |
| **R6 — 论证审查员** | claim 与证据是否构成连贯论证？ | claim-证据映射；为本文选择的结构，而非套用成功范例 |
| **R7 — 投稿核查员** | 当前官方要求有哪些？ | 官方 URL、检索日期与要求-草稿矩阵；标注未确认规则 |
| **R8 — 实验规划员** | 哪个实验能区分不同解释？ | 对照、独立实验单元、指标、划分、重复、预算、失败标准与分析计划 |
| **R9 — 结果分析员** | 测量结果支持什么，还剩什么开放？ | 可追溯运行产物、效应量、不确定性、替代解释与局限 |

**建议流程**：scope → related-work check → contribution & test design → measurements → interpretation → drafting → review → revision。纯写作任务可从 R4 开始；已有结果可从 R9 开始。

---

## 2. 证据账本（Evidence Ledger）

对每个关键 claim，记录：

| 字段 | 内容 |
|---|---|
| Claim 与类型 | 精确声明；文献事实/解释/假设/测量/提案 |
| 一手来源 | 论文/会议 URL、数据集发布、运行日志或提供的稿件 |
| 位置 | 页/节/表/图，文件/行，或精确运行产物 |
| 检查范围 | 身份、发表 venue、技术声明、数值结果或复现 |
| 条件 | 数据集/版本/划分、分辨率、硬件、先验/模型、指标实现与重复次数 |
| 评估 | 支持/部分支持/矛盾/未解/不适用 |
| 时间与限制 | 检索日期、版本与未检查项 |

arXiv 标题匹配只检查元数据。它不验证录用、性能声明、因果归因或复现。把词法匹配当候选。目录外的论文不是编造的，有界检索未命中也不构成新颖性证明。

---

## 3. AI/Agent 核心期刊论文（已核实 / 公认）

> 与 `agent-research-areas.md` 的会议论文互补，此处聚焦**期刊正式发表**的 Agent 相关论文。
> 标注：`[核实]` 本轮检索到明确 venue/官方来源；`[公认]` 学界长期公认，正式引用前以 DOI/期刊官网核对

### 3.1 综述与基础

| 论文 | 期刊 | 核实 |
|---|---|---|
| A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation（3DGS 应用综述，含 Agent 相关的分割/编辑/生成） | TPAMI 2026（复旦大数据研究院） | `[核实]` |
| Memory in the Age of AI Agents: A Survey（Agent 记忆综述） | NUS & 人大 & 复旦 & 北大, 2025 | `[核实]` |
| Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills | UIUC, 2026-03 | `[核实]` |
| A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers | 哈工大 SCIR, arXiv:2412.17481, 2024 | `[核实]` |
| Harness for Large Language Model Agents: A Survey（Agent 执行框架综述） | 2026 | `[核实]` |
| Reinforced Intelligence Through Active Interaction in Real World: A Survey on Embodied AI | Springer, 2025 | `[核实]` |
| An Evolutionary Dynamical Analysis of Multi-Agent Learning in Iterated Games | NSTL 收录, 2026 | `[核实]` |

### 3.2 记忆系统

| 论文 | 期刊 | 核实 |
|---|---|---|
| MemoryBank: Enhancing Large Language Models with Long-Term Memory | AAAI 2024 | `[核实]` |

### 3.3 压缩与高效

| 论文 | 期刊 | 核实 |
|---|---|---|
| CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting | IEEE（动态 4DGS 压缩），2026 | `[核实]` |

### 3.4 意图识别 / 规划 / 推理 / 工具 / 评测 / 安全 / 协议

> 这些方向的代表作以会议为主（见领域图谱），期刊正式发表版持续涌现。以下为已核实或公认的标志工作：

| 论文 | 期刊/会议 | 核实 |
|---|---|---|
| ReAct: Synergizing Reasoning and Acting in Language Models | ICLR 2023 | `[核实]` |
| Reflexion: Language Agents with Verbal Reinforcement Learning | NeurIPS 2023, arXiv:2303.11366 | `[核实]` |
| AgentBench: Evaluating LLMs as Agents | ICLR 2024（清华） | `[核实]` |
| LITMUS: 智能体行为越狱评测基准 | NeurIPS 2026 Oral（南航） | `[核实]` |
| MemoryBank | AAAI 2024 | `[核实]` |
| Generative Agents: Interactive Simulacra of Human Behavior | UIST 2023（Best Paper） | `[公认]` |
| CAMEL: Communicative Agents for "Mind" Exploration | NeurIPS 2023 | `[核实]` |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | NeurIPS 2020 | `[公认]` |

### 3.5 知识工程 / 本体 / RAG

| 论文 | 期刊 | 核实 |
|---|---|---|
| A Survey on Knowledge Graphs: Representation, Acquisition, and Applications（Ji et al.） | IEEE TKDE 2022 | `[公认]` |
| Reasoning over Knowledge Graphs: A Survey（Huang et al.） | IEEE TKDE | `[公认]` |
| LLM Symbolic Reasoning 综述：迈向可验证、可解释、更可信的大模型推理范式 | 2025-12 | `[核实]` |
| Neuro-Symbolic KG Construction via Ontology-grounded Correction | arXiv, 2026-10 | `[核实]` |

### 3.6 通信协议

| 协议 | 来源 | 核实 |
|---|---|---|
| MCP: Model Context Protocol | Anthropic, 2024-11（已移交 Linux 基金会） | `[核实]` |
| A2A Protocol | Google, arXiv:2504.08218, 2025 | `[核实]` |
| A2UI Protocol | arXiv:2503.07666, 2025 | `[核实]` |

---

## 4. Agent 投稿期刊速查（中科院分区 / CCF 分级）

> 以下分区为二手编译参考，**不得直接作为稿件中的权威口径引用**；正式引用须经期刊官网、LetPub、中科院分区表、JCR 一手核实。

### 4.1 顶刊（1 区 / CCF A）

| 期刊 | 全称 | 中科院区 | CCF | Agent 适配子领域 |
|---|---|:---:|:---:|---|
| IEEE TPAMI | IEEE Trans. on Pattern Analysis & Machine Intelligence | 1 | A | 多模态/具身/视觉 Agent 长文 |
| IEEE TKDE | IEEE Trans. on Knowledge & Data Engineering | 1 | A | 知识图谱/语义 Agent/场景图 |
| IEEE TNNLS | IEEE Trans. on Neural Networks & Learning Systems | 1 | B | 前馈/学习类 Agent |
| IJCV | Int'l Journal of Computer Vision | 1 | A | 视觉/具身/3D Agent |
| Information Fusion | Information Fusion | 1 | — | 多模态融合/Cross-Domain Agent |
| Medical Image Analysis | Medical Image Analysis | 1 | — | 医学 Agent |
| JAIR | Journal of AI Research | 4（CCF A） | A | 算法/推理理论 |

### 4.2 系统与应用期刊

| 期刊 | 全称 | 中科院区 | CCF | Agent 适配子领域 |
|---|---|:---:|:---:|---|
| ACM TIST | ACM Trans. on Intelligent Systems & Technology | 3 | B | 系统类/工程落地 Agent |
| Engineering Applications of AI | Engineering Applications of AI | 1 | — | 工业/仿真/具身应用 |
| Expert Systems with Applications | Expert Systems with Applications | 1 | C | 工业/医学应用 |
| Knowledge-Based Systems | Knowledge-Based Systems | 1 | C | 语义/场景图/知识 Agent |
| Neurocomputing | Neurocomputing | 2 | C | 学习类（国人友好） |

### 4.3 Agent 专门期刊

| 期刊 | 全称 | 备注 |
|---|---|---|
| **JAAMAS** | Journal of Autonomous Agents and Multi-Agent Systems | Springer，Agent 专门期刊 |
| **AIJ** | Artificial Intelligence（Elsevier） | AI 基础理论，含 Agent |
| **AAMAS**（会议） | Int'l Conf. on Autonomous Agents and Multi-Agent Systems | Agent 专门会议，论文可扩展为 JAAMAS 期刊版 |

### 4.4 中文核心期刊

- 计算机学报、软件学报、计算机研究与发展、自动化学报（Agent 综述/系统/应用）
- 中国图象图形学报、图形学学报（视觉/具身/3D Agent 交叉）

---

## 5. 顶会投稿速查（Agent 论文主要去向）

| 会议 | 全称 | CCF | 页数 | 截稿 | Agent 侧重 |
|---|---|:---:|---|---|---|
| NeurIPS | Neural Information Processing Systems | A | 正文8页 | 5月 | 推理/学习/多智能体主战场 |
| ICLR | Int'l Conf. on Learning Representations | — | 9页 | 9月 | 架构/规划/工具学习 |
| ICML | Int'l Conf. on Machine Learning | A | 8页 | 1月 | 学习/世界模型 |
| ACL/EMNLP/NAACL | 计算语言学会议 | A/B | 8页 | 滚动 | 意图/记忆/对话/工具 |
| AAAI | Association for the Advancement of AI | A | 7页 | 8月 | 记忆/多智能体 |
| CVPR/ICCV/ECCV | 计算机视觉会议 | A | 8/14页 | 11/3月 | 具身/多模态/世界模型 |
| AAMAS | Autonomous Agents & Multi-Agent Systems | B | 12页 | 10月 | **Agent 专门会议** |
| IJCAI | Int'l Joint Conf. on AI | A | 7页 | 1月 | Agent 综合 |
| KDD | Knowledge Discovery & Data Mining | A | 8页 | 2月 | Agent+数据 |

> 会议扩展为期刊版的合规路径：需 30% 以上实质性增量（非简单拼接）。

---

## 6. 科研辅导工作流

### 6.1 选题评估（R1）
1. 明确研究问题、贡献类型、可用证据、当前阶段
2. 查询 `data/methods.json`（280 条 Agent 方法）定位最近相关工作
3. 检索一手来源找最接近的竞争方法与新工作
4. 全程区分观察、文献陈述、假设、拟做实验、测量结果与编辑建议

### 6.2 实验设计（R8）
1. 明确假设：本文要验证什么
2. 实验矩阵：数据集、基线、指标（成功率/Pass@k/PSNR/FPS/Token成本）、消融
3. 消融设计：每个组件逐一去除，明确验证的假设
4. 控制变量：训练配置、随机种子、硬件一致
5. 预估工作量，划分优先级（必做/加分项）
6. 输出实验计划表

### 6.3 论文写作（R4/R6）
1. 明确目标会议/期刊与当前阶段
2. 对应投稿规范：结构、格式、引用风格
3. 分步推进：Abstract → Intro → Related Work → Method → Experiments → Conclusion
4. 写作规范（老板偏好）：
   - 用领域标准术语（Agent/LLM/Tool/RAG/Memory 等），避免口语化
   - 结论须有数据支撑
   - 去 AI 痕迹：不用排比/破折号/金句，讲清问题-做法-后果
   - 事实底线：不编造结果与引用；不确定明确说"不知道"
   - 引用格式：arXiv ID `arXiv:XXXX.XXXXX`
5. 多身份复核：以审稿人、领域研究员、Agent 专家三方交叉审查

### 6.4 投稿检查（R7）
1. 检索目标 venue 官方要求（页数、格式、截稿、匿名化）
2. 建立 要求-草稿 矩阵，逐项核对
3. 标注未确认规则，不凭记忆
4. 检查引用一致性、AI 使用披露、署名

---

## 7. 引用核实与使用约定

1. **`[核实]`**：2026-10-28 经检索确认 venue/官方来源，可直接引用，仍建议附 DOI/arXiv 链接核对
2. **`[公认]`**：学界长期公认的标志性工作，venue 稳定；正式投稿前以期刊/会议官网核对
3. 本专家团不包含任何编造引用；凡无法核实的一律不列入
4. 期刊分区为二手参考，不得直接作为稿件权威口径引用
5. 项目 `data/methods.json`（280 条 Agent 方法）与本专家团互补：方法库给"方法实例"，专家团给"科研流程"

---

## 8. 与老板研究主线的交汇

- **意图识别 + 记忆** → 国数通"边聊边办"与四层记忆的研究基础；R1 选题评估可锚定"Agent 意图识别"空白点
- **知识工程/本体/RAG** → 专著《AI 落地工程》第 7 章本体驱动的学术对应；R6 论证审查可校验本体-LLM 互增强的 claim
- **通信协议（MCP/A2A/A2UI）** → 国数通协议工作的学术对应；R7 投稿核查可对齐协议标准化论文的 venue
- **具身 + 世界模型 + 空间智能** → 与 3DGS 主线交汇，第二增长曲线；R8 实验规划可设计 3DGS-Agent 交叉实验
- **Agent 工程化与部署** → FDE 方法论的学术支撑；R3 批判审稿可校验工程 claim 的证据强度
- **评估与基准** → 国数通质量评测中心对标；R9 结果分析可规范评测论文的报告

> 本专家团与 Awesome-Gaussian-Skills 的 `research-expert-team` 技能同源异域：流程框架一致（R1-R9 + 证据账本），知识底座切换为 AI/Agent 领域（280 方法库 + 16 领域图谱）。
