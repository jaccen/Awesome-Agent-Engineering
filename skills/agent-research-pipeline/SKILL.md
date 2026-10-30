---
name: agent-research-pipeline
description: >-
  AI/Agent 领域科研全流程辅导技能：选题评估、论文骨架、文献检索、实验设计、
  绘图制表、数据分析、润色去AI味、审稿自查、返修改稿。覆盖论文全生命周期8阶段，
  挂接 Awesome-Agent-Engineering 知识库（280方法+58框架+41基准+1039论文）。
  用于 AI/Agent 论文写作辅导、研究规划、实验设计、审稿预审、idea生成。
license: Apache-2.0
metadata:
  version: 1.1.0
  created: '2026-10-28'
  updated: '2026-10-30'
  domain: AI/Agent
  knowledge_base: data/methods.json (280), data/frameworks.json (58), data/benchmarks.json (41), data/papers.json (1039)
---

# Agent Research Pipeline — AI/Agent 科研全流程辅导

面向 AI/Agent 领域的一站式科研辅导技能。覆盖论文全生命周期 8 阶段，每阶段有明确的流程、检查项与输出规范。挂接本仓库知识库保证答案有据可查。

## 任务路由

收到请求后先分类，再路由到对应流程：

| 请求特征 | 阶段 | 路由 |
|---|---|---|
| "帮我评估这个idea"、"XX方向值得做吗" | 阶段1·选题 | 选题评估流程 |
| "帮我搭论文骨架"、"论文结构怎么组织" | 阶段2·骨架 | 骨架构建流程 |
| "帮我找文献"、"相关工作怎么写" | 阶段3·文献 | 文献检索流程 |
| "帮我画图"、"架构图怎么画" | 阶段4·绘图 | 绘图制表流程 |
| "帮我设计实验"、"消融怎么安排" | 阶段5·实验 | 实验设计流程 |
| "帮我分析结果"、"数据怎么呈现" | 阶段6·分析 | 数据分析流程 |
| "帮我润色"、"去AI味" | 阶段7·润色 | 润色流程 |
| "帮我审稿"、"投稿前自查" | 阶段7·审稿 | 审稿自查流程 |
| "审稿意见怎么回复"、"返修" | 阶段8·返修 | 返修流程 |

---

## 阶段1·选题评估（Idea Evaluation）

### 流程
1. **明确研究定位**：领域、问题空间、最终场景
2. **五维评估**（参照 idea-evaluator 框架）：
   - Higher（更高的性能/质量）
   - Faster（更快的速度/效率）
   - Stronger（更强的泛化/鲁棒性）
   - Cheaper（更低的成本/资源）
   - Broader（更广的适用范围）
3. **致命伤审计**：逐项检查是否命中以下任一 → 若命中则建议放弃或转向
   - 已有方法已解决该问题（无增量）
   - 依赖不存在的数据/算力（不可行）
   - 与现有工作差异无法量化（不可验证）
   - 范式转移探针：是否只是"换个基座重跑"
4. **可行性评估**：数据可得性、算力、基线对照、时间窗口
5. **输出**：选题评估报告（五维雷达 + 致命伤审计 + 可行性 + 建议）

### 检查项
- [ ] 最近相关工作是否已定位（查 `data/methods.json`）
- [ ] 差异声明是否有界（可量化、可反驳）
- [ ] 数据集是否可得
- [ ] 算力是否匹配（GPU 类型和数量）
- [ ] 时间窗口是否合理

---

## 阶段2·论文骨架（Skeleton）

### 流程
1. **思维模板七格**（参照 tech-paper-template）：

| 格 | 内容 | 关键问题 |
|---|---|---|
| 研究背景 | 领域现状与趋势 | 读者为什么要关心 |
| 现有局限 | 已有方法的不足 | 痛点是什么 |
| 核心思想/目标 | 本文要做什么 | 一句话能否说清 |
| 关键挑战 | 为什么难做 | 技术障碍在哪 |
| 方法模块 | 怎么解决的 | 每个模块解决什么 |
| 贡献 | 做成了什么 | 量化、可验证 |
| 定位 | Technique 还是 New Problem/Setting | 论文类型 |

2. **四点自洽检查**：
   - 贡献是否对应挑战（每条贡献回溯到一个挑战）
   - 方法是否对应核心思想（每个模块回溯到核心思想）
   - 实验是否验证贡献（每条贡献有对应实验）
   - 定位是否与 venue 匹配（Technique 投方法类会议，New Problem 投新方向类）

3. **输出**：论文骨架表 + 自洽检查结果 + 建议投稿 venue

### 写作范本（顶刊风格指南）

搭骨架前先查阅 [`references/writing-style-guide.md`](references/writing-style-guide.md)（基于 6 篇高影响论文源码分析）：
- Abstract 五句模板（现状/缺口/方法/数字/意义，数字必进摘要）
- 引言三驱动方式（缺陷驱动/张力驱动/愿景驱动）+ 六段骨架
- 贡献声明三格式（bullet 三点式 / desiderata 式 / 纯散文式）
- 四种论文类型的完整写作模板速查表

需要看原文写法时，读 [`references/top-paper-samples/`](references/top-paper-samples/) 内论文的 LaTeX 源码。

### 投稿定位
- **Technique**（方法论文）：投 CVPR/NeurIPS/ICLR/AAAI/ACL 等方法类会议
- **New Problem/Setting**（新问题/新设定）：投 NeurIPS Datasets&Benchmarks、ICLR、新方向 workshop
- **Benchmark/Evaluation**：投 NeurIPS D&B、ICLR，参照 benchmark-paper-template 五柱框架

---

## 阶段3·文献检索（Literature）

### 流程
1. **关键词扩展**：从用户给定的关键词出发，扩展同义词、上位词、下位词
2. **多源检索**：
   - arXiv（最新预印本，arXiv API 核实 ID）
   - Semantic Scholar / Google Scholar（引用网络）
   - GitHub（代码与项目）
   - HuggingFace（模型与数据集）
3. **本仓库知识库查询**：
   - `data/methods.json`（280 条 Agent 方法，12 类别）
   - `data/frameworks.json`（58 个框架）
   - `data/benchmarks.json`（41 个基准）
   - [`../../references/agent-research-areas.md`](../../references/agent-research-areas.md)（16 领域图谱，位于项目根）
4. **核实纪律**（红线）：
   - arXiv ID 必须能 resolve（用 arXiv API 或 https://arxiv.org/abs/XXXX.XXXXX 验证）
   - 不凭记忆编造引用
   - 会议/期刊名须核实官方全称
   - 不确定明确说"不知道"
5. **输出**：文献清单（按子领域分组，含 arXiv ID / DOI / venue / 一句话概括）

### 引用格式
- 本技能默认 arXiv ID 格式：`[arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)`
- 正式投稿时按目标 venue 的官方引用格式转换
- 中文稿件按 GB/T 7714 或学校指定格式

---

## 阶段4·绘图制表（Figures & Tables）

### 三核心图设计

| 图类型 | 作用 | 设计要点 |
|---|---|---|
| Figure 1·动机图 | 30秒让读者理解为什么做 | 左：现有方法的问题；右：本文的解法；中间：箭头连接 |
| Figure 2·方法总览 | 全文架构一图说清 | 自上而下或自左而右数据流；每模块标注输入输出 |
| Figure 3+·实验结果 | 量化证明有效 | 主表（主指标对比）+ 消融表 + 定性图 |

### 绘图工具选型

| 需求 | 推荐工具 | 输出格式 |
|---|---|---|
| 架构/流程图 | draw.io / SVG | 矢量（SVG/PDF） |
| 数据曲线/柱状 | matplotlib / seaborn | PDF（矢量） |
| 雷达图/对比表 | matplotlib / LaTeX booktabs | PDF |
| 论文配图风格 | 学术低饱和配色 | PDF/EPS |

### 质量检查
- [ ] 矢量格式（SVG/PDF/EPS），不用位图
- [ ] 字号在缩放后可读（正文图最小 8pt）
- [ ] 配色色盲友好（避免红绿对比）
- [ ] 图注自包含（不看正文也能理解图意）
- [ ] 表格用 booktabs 风格（\toprule \midrule \bottomrule）

---

## 阶段5·实验设计（Experiments）

### 流程
1. **明确假设**：本文要验证什么（每个组件验证一个假设）
2. **实验矩阵**：

| 实验 | 目的 | 数据集 | 基线 | 指标 | 消融 | 工作量 | 优先级 |
|---|---|---|---|---|---|---|---|
| 主实验 | 证明方法有效 | 3+ benchmark | 5+ 基线 | 主指标 | — | 高 | 必做 |
| 消融 | 证明每个组件有用 | 1-2 dataset | 本文完整版 | 主指标 | 逐组件去除 | 中 | 必做 |
| 效率 | 证明速度快/省资源 | 1 dataset | 基线 | FPS/内存/Token | — | 中 | 加分 |
| 定性 | 直观展示效果 | 选样 | 基线 | 视觉对比 | — | 低 | 加分 |

3. **Agent 领域常用指标**：
   - 任务成功率（Success Rate / Pass@k / SR）
   - 完成步数（Steps to Complete）
   - 效率（Token Cost / API Calls / Time）
   - 鲁棒性（OOD 成功率 / 干扰恢复率）
   - 安全性（越狱抵抗率 / 有害输出率）

4. **Agent 领域常用基准**（查 `data/benchmarks.json`）：
   - 通用：AgentBench, GAIA, MINT-Bench
   - 代码：SWE-bench, SWE-bench Verified, HumanEval, LiveCodeBench
   - Web/GUI：WebArena, OSWorld, Mind2Web, AndroidWorld
   - 工具：ToolBench, API-Bank, Tau-Bench
   - 安全：Agent-SafetyBench, InjecAgent, LITMUS
   - 记忆：EvoMemBench（NeurIPS 2026）

5. **消融设计纪律**：
   - 每个组件逐一去除，明确验证的假设
   - 机制归因类声称须补负对照（保留超参、仅移除机制）
   - 诚实报告 negative results
   - 多种子统计（≥3 seeds）+ 配对 t 检验

6. **输出**：实验计划表（固定列：序号/实验/目的/数据集/基线/指标/工作量/优先级）
   - 可填充模板见 `references/experiment-template.md`（含贡献-实验映射、消融设计、多种子统计、negative results、关键场景达标检查、投稿前自检清单）

---

## 阶段6·数据分析（Data Analysis）

### 流程
1. **数据整理**：原始日志 → 结构化表格（run_id / method / dataset / metric / value / seed）
2. **统计报告**：
   - 均值 ± 标准差（≥3 seeds）
   - 配对 t 检验或 Wilcoxon 检验（p 值）
   - 效应量（Cohen's d 或 相对提升%）
3. **可视化**：
   - 主表：LaTeX booktabs，最优值加粗，次优下划线
   - 趋势图：折线图（训练曲线/步数-成功率）
   - 消融表：逐行去除一个组件，标红下降
   - 雷达图：多维度对比（速度/质量/成本/泛化/安全）
4. **归因分析**：
   - 性能提升来自哪个组件（消融证据）
   - 失败案例归因（什么场景失败、为什么）
   - 与 claim 的一致性检查（数据是否支撑每个 claim）

### 检查项
- [ ] 每个数值有对应的原始日志可追溯
- [ ] 统计检验已做（不只是报均值）
- [ ] negative results 诚实报告
- [ ] claim 与数据一致（不夸大）

---

## 阶段7a·润色（Polishing）

### 流程
1. **语法与流畅性**：修复语法错误、提升句子连贯性
2. **术语规范化**：使用领域标准术语（Agent/LLM/Tool/RAG/Memory/ReAct/CoT 等），避免口语化
3. **AI 味去除**（红线，参照 Humanizer 规则）：
   - 不用排比句堆砌（"不仅...而且...更..."）
   - 不用破折号代替论证
   - 不用三段式法则（"第一...第二...第三..."机械列举）
   - 不用模糊归因（"研究表明"不附来源）
   - 不用 -ing 结尾的肤浅分析
   - 不用宣传性语言（"革命性""颠覆性"）
4. **claim 强度校准**：claim 须与证据强度匹配，不夸大
5. **顶刊语言风格自检**：对照 [`references/writing-style-guide.md`](references/writing-style-guide.md) §2.6 语言风格清单（主动语态/simple 是美德/claim 三档不越位/绝对值+相对值并用/术语操作化/禁止宣传性形容词）
6. **输出**：润色后全文 + 修改追踪（标注每处实质性修改的理由）

### 写作规范（老板偏好）
- 事实底线：不编造结果与引用
- 结论须有数据支撑，拒绝无依据断言
- 引用必须官方核实（arXiv API / DOI）
- 讲清问题-做法-后果，不堆金句

---

## 阶段7b·审稿自查（Self-Review）

### 多身份交叉审查
以三方视角分别审查，汇总问题清单：

| 身份 | 审查重点 |
|---|---|
| **审稿人** | 创新性、实验充分性、claim 有无数据支撑、可复现性 |
| **领域研究员** | 技术正确性、与最近工作的差异、术语准确 |
| **Agent 专家** | 基线是否公平、指标是否合理、消融是否完备 |

### 审稿意见编码（33 条真实审稿意见规律）
常见拒稿理由（按频率）：
1. 实验不充分（基线少 / 数据集少 / 无消融）
2. 创新性不足（与现有工作差异不明确）
3. claim 无数据支撑（夸大 / 无量化）
4. 可复现性差（缺细节 / 缺代码）
5. 写作问题（逻辑混乱 / AI 味重）

### 检查清单
- [ ] 每条贡献有对应实验验证
- [ ] 基线选取公平（用最新 SOTA，非 cherry-pick 旧基线）
- [ ] 消融完备（每个组件都有去除实验）
- [ ] 统计检验已做（不只报均值）
- [ ] 引用全部核实（arXiv ID resolve / DOI 有效）
- [ ] AI 味已去除（排比/破折号/金句/宣传语言）
- [ ] 格式符合 venue 要求（页数 / 模板 / 匿名化）
- [ ] 代码与数据 Availability 已写

---

## 阶段8·返修改稿（Rebuttal）

### 流程
1. **审稿意见分类**：Major / Minor / Clarification
2. **逐条回复策略**（P(Z|X,Y) 条件说服框架）：
   - 匹配审稿人心态 X（质疑什么、担心什么）
   - 选择回复策略 Y（补充实验 / 澄清说明 / 适度让步 / 礼貌反驳）
   - 用证据支撑（新数据 / 新引用 / 新分析）
3. **Cover Letter**：感谢审稿人 → 概述主要修改 → 强调最重要的新增结果
4. **Marked Manuscript**：用颜色标注修改处，方便审稿人定位
5. **常见回复模板**：
   - 补充实验型："感谢指出，我们补充了 XX 实验，结果如下表..."
   - 澄清说明型："感谢提问，我们在 X.X 节补充了说明..."
   - 适度让步型："同意该局限，我们在 Conclusion 中明确讨论..."
   - 礼貌反驳型："我们理解审稿人的关注，但基于以下证据认为..."

### 返修纪律
- 每条意见都回复，不遗漏
- 不静默修改（每处修改都说明改了什么、为什么）
- 新增实验如实报告（包括不支持原 claim 的结果）
- 不过度承诺（"我们完全解决了"→ "我们在 X 场景下改善了"）

---

## 知识库挂接

### 本仓库资源
| 资源 | 路径 | 用途 |
|---|---|---|
| 方法库 | `data/methods.json` (280) | 定位最近相关工作、找基线 |
| 框架库 | `data/frameworks.json` (52) | 工程对比、选型 |
| 基准库 | `data/benchmarks.json` (32) | 选数据集、选评测 |
| 行业库 | `data/industries.json` (106) | 找落地场景、motivation |
| 创业库 | `data/startups.json` (56) | 找产业趋势、差异化 |
| 领域图谱 | [`../../references/agent-research-areas.md`](../../references/agent-research-areas.md) (16领域，项目根) | 定位研究方向 |
| 写作风格指南 | `references/writing-style-guide.md` | 顶刊写作模式（基于 6 篇典范论文源码分析） |
| 论文样本库 | `references/top-paper-samples/` (6篇) | 高影响论文 PDF + LaTeX 源码范本 |
| 专家团 | [`../../references/agent-research-expert-team.md`](../../references/agent-research-expert-team.md) (R1-R9，项目根) | 科研协作流程 |
| 配套专著 | [`deployment-book/`](../../deployment-book/) (子模块，项目根) | 工程落地方法论 |

### 引用纪律
- 查询 `data/methods.json` 时核对方法名、arXiv ID、分类
- 不凭记忆编造方法或引用
- 方法库是起点索引，非穷尽文献检索；目录外的论文不是编造的
- 详见 [references/paper-database.md](references/paper-database.md) 获取已核实论文清单

---

## 结果交付

- 选题/骨架类：输出结构化 Markdown（表格 + 分层 + 待办）
- 实验设计类：输出实验计划表（固定列格式）
- 写作/润色类：输出修改后全文 + 修改追踪
- 审稿自查类：输出问题清单（按严重程度排序）+ 修改建议
- 返修类：输出逐条回复 + Cover Letter + Marked Manuscript 要点
- 所有建议附依据与验证方式（如何证明建议有效）
- 用户未确认的假设标注，不越权替用户做决定
