# 顶刊论文写作风格指南（基于 6 篇典范论文源码分析）

> 本文由对本目录 `top-paper-samples/` 内 6 篇高影响论文的 LaTeX 源码逐篇分析提炼而成。
> 分析基于官方 arXiv 源码（已核实），非凭记忆转述。样本清单与版权说明见 `top-paper-samples/README.md`。

## 样本总览

| # | 论文 | Venue | 类型 | arXiv |
|---|---|---|---|---|
| 01 | Attention Is All You Need | NeurIPS 2017 | 架构方法 | [1706.03762](https://arxiv.org/abs/1706.03762) |
| 02 | Chain-of-Thought Prompting Elicits Reasoning in LLMs | NeurIPS 2022 | 实证研究 | [2201.11903](https://arxiv.org/abs/2201.11903) |
| 03 | ReAct: Synergizing Reasoning and Acting in LMs | ICLR 2023 | 范式方法 | [2210.03629](https://arxiv.org/abs/2210.03629) |
| 04 | Toolformer: LMs Can Teach Themselves to Use Tools | NeurIPS 2023 | 自监督方法 | [2302.04761](https://arxiv.org/abs/2302.04761) |
| 05 | 3D Gaussian Splatting for Real-Time Radiance Field Rendering | ACM TOG / SIGGRAPH 2023 | 系统方法 | [2308.04079](https://arxiv.org/abs/2308.04079) |
| 06 | Generative Agents: Interactive Simulacra of Human Behavior | UIST 2023 | 系统+HCI | [2304.03442](https://arxiv.org/abs/2304.03442) |

六篇覆盖四种论文类型：架构方法（01）、实证研究（02）、范式方法（03/04）、系统方法（05/06）。下文先逐篇解剖，再给跨论文通用模式。

---

## 一、逐篇解剖

### 01 Attention Is All You Need（极简架构范）

**Abstract 结构（6 句）**
1. 现状：主流序列转导模型基于 RNN/CNN（1 句陈述，无形容词堆砌）
2. 补充现状：最佳模型还连接 attention
3. `We propose` + 命名（Transformer）+ 一句话本质（solely on attention, dispensing with recurrence and convolutions entirely）
4. 实验范围 + 三重优势（quality / parallelizable / training time）
5. **具体数字**：WMT14 En-De 28.4 BLEU，超现有最佳（含 ensemble）2 BLEU
6. **具体数字 + 成本**：En-Fr 41.8 BLEU，8 GPU 训练 3.5 天（"a small fraction of the training costs"）
7. 泛化验证：constituency parsing 大/小数据都成功

**引言逻辑链（4 段，纯散文，无 bullet 贡献）**
1. 现状确立：RNN/LSTM/GRU 是 SOTA + 引用 3 篇
2. 技术本质缺陷：顺序计算 → 无法并行 → 长序列内存限制。关键句式："The fundamental constraint of sequential computation, however, remains."（承认他人改进，但指出根本约束未解）
3. 过渡：attention 已被广泛使用，但除少数例外都依附 RNN
4. 本文方案：`In this work we propose the Transformer`，一句话说清本质，紧跟两个优势

**章节结构**：Introduction → Background → Model Architecture → Why Self-Attention → Training → Results → Conclusion。正文 9 页内结束；Why Self-Attention 单独成节回答"为什么这样做"——这是审稿人必问问题，提前一节正面回答。

**结论写法**：3 句总结（第一个纯 attention 序列转导模型 / 训练显著更快 / 两个 SOTA）+ 3 条具体未来方向（其他模态、局部 attention、更少顺序化）+ 代码链接。**不写空话**，每条 future work 都具体可执行。

**可借鉴**：
- 用 "simple" 当卖点而非缺点（"a new simple network architecture"）
- 摘要放两组对比数字 + 训练成本，审稿人 30 秒建立信心
- 单独一节回答"为什么这个设计"（Why Self-Attention）

### 02 Chain-of-Thought（实证研究范）

**Abstract 结构（4 句）**
1. 探索性问题：如何生成中间推理步骤提升复杂推理
2. 方法命名 + 一句话机制（few-shot exemplars 中给推理链示例）
3. 实验范围（3 个 LLM × 3 类任务）
4. 结果：`The empirical gains can be striking.` + 具体数字（PaLM 540B + 8 个示例 = GSM8K SOTA，超过 finetuned GPT-3 with verifier）

**引言逻辑链（5 段）**
1. 领域背景：LLM 变革 + scaling 的收益
2. 转折：但 scaling 不足以解决推理任务（引用 scaling 论文佐证）
3. 本文动机 = 两个已有 idea：rationale 生成（有先例）+ few-shot prompting（有先例）
4. **两个 idea 各自的关键局限**：rationale 标注成本高；传统 few-shot 在推理任务上差且不随规模改善
5. 结合两者、避免两者局限 → 本文方法

**章节结构**：Introduction → Chain-of-Thought Prompting（方法）→ Arithmetic Reasoning（Setup/Results/Ablation/Robustness 四小节）→ Commonsense Reasoning → Symbolic Reasoning → Discussion → **Related Work（放倒数第二）** → Conclusions。

**附录组织（实证论文的极致）**：NeurIPS Checklist、FAQ 节（"Why does increasing model scale improve..."直接预设审稿人问题）、Reproducibility Statement、计算资源声明、全部数据集许可、正确/错误推理链的全部分类分析、所有 prompt 全文。

**可借鉴**：
- 动机 = "两个好 idea 的组合，各自有局限，组合后互相补足"——组合式创新的标准写法
- 实证论文 Related Work 放后：先让证据说话，再定位文献
- 用 FAQ 附录把审稿人可能的质疑变成展示深度的机会
- robustness 分析含"不同标注者/无 ML 背景标注者/不同示例"三组——证明结论不依赖特定选择

### 03 ReAct（范式方法范）

**Abstract 结构（5 句）**
1. 背景：LLM 推理（CoT）与行动（计划生成）被分开研究
2. 方法：interleaved 生成推理轨迹与任务动作
3. 机制解释（双向）：推理帮助 induce/track/update 计划、处理异常；行动帮助对接外部信息源
4. 实验范围（语言 + 决策任务，超 SOTA 基线 + 可解释性/可信性提升）
5. **两组具体数字**：HotpotQA/Fever 克服幻觉与错误传播；ALFWorld/WebShop 超 IL/RL 方法绝对 34%/10%（仅 1-2 个示例）

**引言逻辑链（4 段）**
1. **人类类比开头**：人类智能的独特性 = 行动与语言推理无缝结合 → 厨房做饭的具体例子（3 条引用口语化内心独白："I don't have salt, so let me use soy sauce"）
2. 现有两条线及其缺陷：CoT 是 static black box（不接地外部世界 → 幻觉、错误传播）；action-only 缺推理
3. 本文方案 + Figure 1 范式对比图
4. 实验预告 + 数字 + 附加收益（可解释、可信、可诊断）

**章节结构**：Introduction → ReAct（方法）→ Related Work → Knowledge-Intensive Reasoning Tasks（QA+Fever 合一节）→ Decision Making Tasks（ALFWorld+WebShop 合一节）→ Conclusion。实验两大节按任务性质分，每节内部 Setup/Methods/Results and Observations。

**可借鉴**：
- Figure 1 用"四种范式对比"（Standard / CoT / Act-only / ReAct）一眼说清定位——范式类论文的标配图
- 开头人类类比要具体到对话级（不是"人类很擅长推理"这种空话）
- 实验叙述用编号观察（Observation 1/2/3），每个观察一条可引用的结论句
- "34% and 10%" 是绝对提升——绝对数字比相对百分比更有冲击力，两者并用

### 04 Toolformer（自监督方法范）

**Abstract 结构（5 句）**
1. **悖论开头**：LLM 强大（few-shot）"but, paradoxically" 基础功能（算术、事实查询）反而不如小模型
2. 方案：LM 可以 self-supervised 学会用外部工具
3. 方法四要素：决定 which APIs / when / what arguments / how to incorporate results
4. 自监督，只需每个 API 少量演示；5 种工具列举
5. 结果：zero-shot 大幅提升 + 常与更大模型竞争 + 不牺牲语言建模能力

**引言逻辑链（5 段）**
1. LLM 强 + 5 条固有局限（每条带引用：时效、幻觉、低资源语言、数学、时间感知）
2. 思路：给外部工具。但现有方法两个问题：依赖大量人工标注 / 限死在任务特定设置
3. **desiderata 式贡献**：`we propose Toolformer, which fulfills the following desiderata:` + bullet（自监督无需大量标注 / 不损失通用性、模型自主决定何时用哪个工具）
4. 方法概述（Figure 2 四步流程图：sample → execute → filter → finetune）
5. 结果预告

**章节结构**：Introduction → Approach（按流水线 5 小节：Sampling API Calls / Executing / Filtering / Model Finetuning / Inference）→ Tools（5 小节每工具一节）→ Experiments（Setup / Downstream Tasks / Language Modeling / Scaling Laws）→ Analysis（Decoding Strategy / Data Quality）→ Related Work → **Limitations（单独成节）** → Conclusion。

**可借鉴**：
- 悖论式开头制造张力（强与弱的对立）比平铺直叙更抓人
- desiderata 写法：先列"好方法应满足什么"，再声明本文方法全部满足——比直接列贡献更有说服力结构
- Approach 按数据流水线步骤分小节，读者可逐步复现
- **单独 Limitations 节**（诚实列出失败模式）是 NeurIPS 加分项
- Filtering 数据质量有 Analysis 节专门交代（自监督方法的可信度关键）

### 05 3DGS（系统方法/顶刊范）

**Abstract 结构（5 句）**
1. 领域背景：Radiance Field 革命了 novel-view synthesis
2. 矛盾：高质量需要贵网络；近期快的方法牺牲质量；**无人做到无界完整场景 1080p 实时**
3. `We introduce three key elements` + 三点预告（表示 / 优化+密度控制 / 渲染算法），每点一句话讲清"是什么+为什么重要"
4. 结果声明：SOTA 视觉质量 + 竞争训练时间 + 高质量实时渲染
5. 一句验证：在多个公开数据集上证明

**引言逻辑链（5 段）**
1. 两类表示的对照：meshes/points（显式、GPU 光栅化友好）vs NeRF（连续、优化好但采样贵有噪）
2. `We introduce a new approach that combines the best of both worlds` + 一句话同时给质量与速度承诺
3. 目标声明（实时渲染 + 优化时间与最快方法相当）
4. 现有方法两难的具体化：快的训练快但质量差；Mip-NeRF360 质量好但要 48 小时；交互式 10-15 fps 不够实时（≥30 fps）
5. 三组件逐一展开（每组件 2-3 句：输入是什么、做了什么、得到什么）
6. 末尾 bullet 三点贡献（表示 / 优化方法 / 渲染方法）

**贡献 bullet（三点式，每条 = 名词短语 + 定语从句说明性质）**
- The introduction of anisotropic 3D Gaussians as a high-quality, unstructured representation of radiance fields.
- An optimization method of 3D Gaussian properties, interleaved with adaptive density control that creates high-quality representations...
- A fast, differentiable rendering approach for the GPU, which is visibility-aware, allows anisotropic splatting and fast backpropagation...

**章节结构**：Introduction → **Overview（先给全景）** → Related Work（3 小节按技术脉络）→ Differentiable 3D Gaussian Splatting（表示与渲染）→ Optimization with Adaptive Density Control → Implementation, results and evaluation（Implementation / Results and Evaluation〔含 Real-World、Synthetic、Compactness 小节〕/ Ablations〔5 项各一小节〕/ **Limitations 小节**）→ Discussion and Conclusions。

**结论写法特点**：结论里坦诚工程成本（"The majority (~80%) of our training time is spent in Python code"）+ 可预期的改进路径（全部移植 CUDA）+ "contrary to widely accepted opinion" 的认知修正声明 + 一个具体有趣的可探索方向（Gaussian → mesh 重建）。

**可借鉴**：
- Overview 节：先给全景再深入细节，TOG/SIGGRAPH 类系统论文标配
- 消融 5 项各起小标题（Initialization from SfM / Densification / Unlimited depth complexity / Anisotropic Covariance / Spherical Harmonics）——每项设计选择都有单独证据
- Limitations 放在实验节内、结论前——承认边界但不自我否定
- 摘要中 "no current method can achieve real-time display rates" 划定无人区，"first"声明留给结论（"the first approach that truly allows real-time..."），措辞可辩护
- 用具体 fps/分辨率（≥30 fps @ 1080p）定义"实时"——术语操作化

### 06 Generative Agents（系统+HCI 范）

**Abstract 结构（6 句）**
1. 应用愿景：believable proxies 赋能的应用（沉浸环境/排练空间/原型工具）
2. 定义：generative agents = 模拟可信人类行为的软件 agent
3. **画面感场景句**（独家写法）："Generative agents wake up, cook breakfast, and head to work; artists paint, while authors write; they form opinions, notice each other, and initiate conversations..."
4. 架构三要素：自然语言存储完整经验 / 随时间合成高层反思 / 动态检索规划行为
5. 实例化：Smallville（The Sims 风格沙箱，25 个 agent）+ 涌现案例（情人节派对自主传播邀请、结识、约会、准时到场）
6. 消融结论：观察/规划/反思三组件各自对 believability 关键

**引言逻辑链（4 段）**
1. **研究问题开头**："How might we craft an interactive artificial society that reflects believable human behavior?"
2. 40 年愿景回顾（从 The Sims 到认知模型）+ 潜在应用面
3. 挑战：行为空间大而复杂；单时间点模拟 ≠ 长期一致性；需要管理持续增长的记忆与级联社会动态
4. 成功三要求（retrieve 长期事件 / reflect 泛化推理 / plan 当下与长期一致）→ 本文引入 generative agents + 两类评估预告

**章节结构**：Introduction → **Related Work（第 2 节，HCI 惯例）** → Generative Agent Sandbox（环境先行）→ Generative Agent Architecture（Memory and Retrieval / Reflection / Planning and Reacting 三小节）→ Controlled Evaluation（Procedure / Conditions / Human Evaluators / Analysis / Results）→ End-User Evaluation → Discussion（Applications / **Future Work and Limitations** / **Ethics and Societal Impact**）→ Conclusion。

**可借鉴**：
- 系统论文先立环境（Sandbox 节）再讲架构——读者先看到系统长什么样
- **双评估设计**：受控评估（证明组件因果作用）+ 端到端评估（证明整体体验）——HCI/Agent 系统论文的黄金结构
- 涌现行为用叙事化案例呈现（情人节派对）——比纯表格更能传达"可信行为"
- Ethics and Societal Impact 单独成节：UIST/CHI 类 venue 硬要求，给出可操作缓解（防准社会关系/深伪/说服滥用）
- Abstract 用具体行为画面代替抽象描述——读者 10 秒建立直觉

---

## 二、跨论文通用模式

### 2.1 Abstract 五句模板（四类变体）

| 槽位 | 功能 | 例子 |
|---|---|---|
| S1 现状/张力 | 让读者定位问题 | Attention: 现有模型基于 RNN/CNN；Toolformer: 强但悖论式地基础差；3DGS: 质量与速度无人兼得 |
| S2 缺口 | 现有方法做不到什么 | 3DGS: "no current method can achieve real-time display rates"；ReAct: 推理与行动被分开研究 |
| S3 方法 | We propose/introduce + 命名 + 一句话本质 | 全部 6 篇都有明确命名（Transformer/ReAct/Toolformer/generative agents），方法本质一句话说清 |
| S4 数字结果 | 具体数字 + 对比对象 | Attention: 28.4/41.8 BLEU + 训练成本；ReAct: 34%/10% 绝对提升；CoT: 8 个示例超 finetuned GPT-3 |
| S5 意义/泛化 | 更广影响或验证 | Attention: 泛化到 parsing；GenAgents: 架构与交互模式 |

写法纪律：
- 数字必须进摘要（6/6 篇都有至少一个具体数字或量化对比）
- 方法一句话说清本质，机制细节留给正文
- 不用"具有重要意义""取得良好效果"这类空话；用"surpassing even finetuned GPT-3 with a verifier"这种可查证的比较

### 2.2 引言逻辑链（三种驱动方式）

| 驱动 | 结构 | 适用 | 样本 |
|---|---|---|---|
| **缺陷驱动** | 现状 SOTA → 技术本质缺陷（承认增量改进但根本约束未解）→ 本文方案 | 有明确技术瓶颈的架构/方法 | Attention |
| **张力驱动** | 两难对比（快 vs 好、强 vs 弱）→ 无人区划定 → 三组件方案 | 系统/工程方法 | 3DGS、Toolformer |
| **愿景/类比驱动** | 人类类比或研究问题开头 → 愿景与挑战 → 成功三要求 → 方案 | 范式/系统/HCI | ReAct、GenAgents |

共同骨架（无论哪种驱动）：
1. 定位段（读者为什么关心）
2. 缺口段（现有方法差在哪，每条带引用）
3. 方案段（We propose + 命名 + 本质一句话）
4. 机制段（方法如何工作，常配 Figure 1/2）
5. 证据预告段（实验范围 + 头部数字）
6. 收束段（附加收益：可解释性/成本/泛化）

**贡献声明三格式**：
- **bullet 三/四点式**（3DGS 三点、GenAgents 四点）：每条 = 名词短语 + that/which 从句说明性质与作用。最通用。
- **desiderata 式**（Toolformer）：先列"好方案应满足什么"再声明全部满足。适合自监督/自动化类方法。
- **纯散文式**（Attention、ReAct）：适合极短引言或贡献单一明确的论文。

### 2.3 方法部分组织（三模式）

| 模式 | 结构 | 适用 | 样本 |
|---|---|---|---|
| 流水线步骤式 | 按数据处理顺序分小节（sample→execute→filter→finetune→inference） | 训练流程复杂、需复现 | Toolformer |
| 组件分节式 | 每个架构组件一节（表示/优化/渲染；记忆/反思/规划） | 多组件系统 | 3DGS、GenAgents |
| 一体式 | 方法一节讲完 + 实验按任务域分节 | 方法简单、重点在实证 | CoT、ReAct |

纪律：每小节开头一句定位句（本小节解决什么）；符号系统首次出现即定义；每个设计选择要么给理由要么指向消融。

### 2.4 实验呈现规范

- **主表**：最优加粗；对比基线覆盖"最新 SOTA + 经典方法 + 消融变体"三类；表注自包含
- **消融**：3DGS 每项设计一小节并命名；CoT 的 robustness 三组（标注者/背景/示例）；GenAgents 消融直接支撑架构三组件——**消融结构必须镜像方法结构**
- **观察式叙述**（ReAct）：Results and Observations，编号观察句，每条一句话可独立引用
- **分析节**（Toolformer）：数据质量、解码策略等"为什么有效"的深挖，单列 Analysis
- **Limitations 位置三选一**：单独节（Toolformer，NeurIPS 风格）/ 实验节内小节（3DGS）/ Discussion 内合并（GenAgents）——位置不关键，**存在且具体**才关键（写失败模式与适用边界，不写"我们方法很完美只有些许不足"）

### 2.5 Related Work 位置决策

| 位置 | 理由 | 样本 |
|---|---|---|
| 第 2 节（引言后） | 系统/HCI 论文，需先建立文献地图再读系统 | GenAgents |
| 方法后 | 范式论文，先说清新东西再对照旧工作 | ReAct、3DGS |
| 倒数第二 | 实证论文，先给证据再定位文献 | CoT |
| Limitations 前 | 方法论文惯例，顺带对比差异化 | Toolformer |

内容组织按**技术脉络**分小节（3DGS：传统重建 → 神经渲染 → 点基渲染），每小节末尾一句"与本文的差异"。

### 2.6 语言风格清单

- 第一人称复数主动语态（we propose / we show / we demonstrate）——6/6 篇
- "simple" 是美德不是缺陷（Attention: "a new simple network architecture"）
- claim 强度三档：proven（数字支撑）/ suggested（实验观察）/ speculated（future work）——不越档
- "first" 声明要可辩护：留给结论且加限定（"the first approach that truly allows real-time, high-quality radiance field rendering"）
- 对比数字用绝对值+相对值并用（ReAct: absolute 34%）
- 具体定义术语（3DGS: 实时 = ≥30 fps @ 1080p）
- 坦诚工程细节反而加分（3DGS: 80% 训练时间在 Python）
- 禁止：宣传性形容词堆砌、无出处的"研究表明"、破折号当论证用

### 2.7 图表设计规律

- **Figure 1 是门面**：范式对比（ReAct 四分格）/ 方法总览（Toolformer 四步）/ 效果 teaser（GenAgents 沙箱截图）。30 秒内让读者明白"问题-方法-效果"
- **Figure 2 通常是方法细节图**（Toolformer 数据流水线）
- 表格自包含：表注写清评测设置、指标定义、最优加粗说明
- 附录承载：全部 prompt（CoT/ReAct 把 prompt 全文放附录——可复现性的关键）、错误案例分析、扩展相关工作

### 2.8 论文类型写作模板速查

| 类型 | 引言驱动 | 方法组织 | Related Work 位置 | Limitations | 样本 |
|---|---|---|---|---|---|
| 架构方法 | 缺陷驱动 | 组件分节 | 中后 | 简短带过（当时惯例，现建议单独节） | 01 |
| 实证研究 | 组合动机 | 实验按任务域 | 倒数第二 | FAQ/鲁棒性分析代替 | 02 |
| 范式方法 | 类比驱动 | 一体式+任务分节 | 方法后 | 结论内展望 | 03 |
| 自监督方法 | 悖论驱动 | 流水线步骤 | Limitations 前 | **单独节** | 04 |
| 系统方法(3D) | 张力驱动 | Overview+组件分节 | 方法前 | 实验节内小节 | 05 |
| 系统+HCI | 愿景驱动 | 环境先行+组件分节 | 第 2 节 | Discussion 专节+伦理 | 06 |

---

## 三、使用方式

1. **写 Abstract 前**：读 2.1 表，先填五槽位，S4 必须有数字
2. **搭引言前**：从 2.2 选驱动方式，按六段骨架填内容
3. **组织方法前**：从 2.3 选组织模式，方法结构与消融结构镜像设计
4. **投稿前**：对照 2.6 语言清单逐条自检
5. **需要范本时**：直接读 `top-paper-samples/<论文>/source/*.tex` 源码（含原始 LaTeX 排版技巧），PDF 用于看最终排版效果

## 四、本指南边界

- 样本为 2017–2023 年英文顶会/顶刊论文；中文核心期刊（计算机学报/软件学报等）写作规范另见 venue 要求，本指南不覆盖
- 分析基于 arXiv 版源码，与最终会议版可能存在差异（页数限制、附录取舍）
- 引用影响力以 Google Scholar 实时数据为准，本指南不做具体引用数断言
- 版权：样本论文版权归原作者，仅限本仓库内部写作研究使用
