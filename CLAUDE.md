# Awesome-Agent-Engineering — AI 协作指令

本仓库是 AI/Agent 领域的科研基础设施库，含 5 个知识库、1 个科研全流程技能。当 AI 助手在本仓库或基于本仓库资源协助用户做 AI/Agent 论文写作时，按以下规则工作。

## 科研全流程技能：agent-research-pipeline

技能位置：`skills/agent-research-pipeline/SKILL.md`

覆盖 8 个阶段，每个阶段有明确的流程与输出格式：

| 阶段 | 触发场景 | 核心输出 | 配套资源 |
|---|---|---|---|
| 1·选题评估 | "这个 idea 行不行" | 五维评估 + 致命伤审计 | — |
| 2·论文骨架 | "帮我搭论文结构" | 思维模板七格 + 四点自洽 | — |
| 3·文献检索 | "帮我找相关论文" | 论文清单 + BibTeX | `references/paper-database.md`、`data/papers.json` |
| 4·绘图 | "画架构图/实验图" | 三核心图设计 + 代码模板 | — |
| 5·实验设计 | "帮我设计实验/消融" | 实验计划表 | `references/experiment-template.md`、`data/benchmarks.json` |
| 6·数据分析 | "实验结果怎么分析" | 统计报告（均值±标准差+t检验） | — |
| 7·润色审稿 | "帮我润色/审稿" | 逐点审稿意见 + 润色稿 | `references/venues.md` |
| 8·返修改稿 | "审稿意见怎么回" | 逐条回复 + cover letter | — |

## 引用纪律（红线）

1. **不编造引用**：列出的每篇论文必须真实存在。arXiv ID 必须能在 arxiv.org resolve。
2. **核实标注**：`[核实]` = 本轮检索到明确 venue/官方来源；`[公认]` = 学界长期公认标志性工作。无法核实的不列入。
3. **宁缺毋滥**：检索不到足够真实论文时如实说明数量，不编造补齐。

## 关键资源路径

- 论文库（机器可读）：`data/papers.json`（995 篇，官方 arXiv 标题/venue/核实状态）
- 论文库（人工可读）：`references/paper-database.md`（16 子领域）
- 投稿速查：`references/venues.md`（15 顶会 + 20 期刊，CCF/页数/截稿）
- 实验模板：`references/experiment-template.md`（可直接复制填充）
- 基准清单：`data/benchmarks.json`（32 个 Agent 评测基准）
- 方法库：`data/methods.json`（280 方法，12 类别）
- 研究图谱：`references/agent-research-areas.md`（16 核心领域）
- 科研专家团：`references/agent-research-expert-team.md`（R1-R9 角色）

## 工作原则

- 事实底线：一切回答基于事实，不知道就明确说"不知道"，不以推测代替论据。
- 实验纪律：每条贡献须有对应实验；机制归因须补负对照；≥3 seeds + 配对 t 检验；诚实报告 negative results；先关键场景达标再全量重跑。
- 写作风格：去 AI 味，不用排比/破折号/金句/宣传语言；结论须有数据支撑。
