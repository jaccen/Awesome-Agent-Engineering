# Agent 投稿 venue 速查

> 编制日期：2026-10-28 · 用途：agent-research-pipeline skill 阶段2/7 的 venue 选型与格式核查
> 分区为二手编译参考，不得直接作为稿件权威口径引用；正式投稿前以 venue 官网核对

---

## 顶会（Agent 论文主要去向）

| 会议 | 全称 | CCF | 截稿 | 页数 | 格式 | Agent 侧重 |
|---|---|:---:|---|---|---|---|
| **NeurIPS** | Neural Information Processing Systems | A | 5月 | 正文8页 | NeurIPS style | 推理/学习/多智能体主战场 |
| **ICLR** | Int'l Conf. on Learning Representations | — | 9月 | 9页 | ICLR style | 架构/规划/工具学习 |
| **ICML** | Int'l Conf. on Machine Learning | A | 1月 | 8页 | ICML style | 学习/世界模型 |
| **ACL** | Association for Computational Linguistics | A | 滚动 | 8页 | ACL style | 意图/记忆/对话/工具 |
| **EMNLP** | Empirical Methods in NLP | B | 滚动 | 8页 | ACL style | 同 ACL |
| **NAACL** | North American Chapter of ACL | B | 滚动 | 8页 | ACL style | 同 ACL |
| **AAAI** | Association for the Advancement of AI | A | 8月 | 7页 | AAAI style | 记忆/多智能体 |
| **CVPR** | Computer Vision & Pattern Recognition | A | 11月 | 正文8页 | IEEE双栏 | 具身/多模态/世界模型 |
| **ICCV** | Int'l Conf. on Computer Vision | A | 3月 | 正文8页 | IEEE双栏 | 同 CVPR |
| **ECCV** | European Conf. on Computer Vision | B | 3月 | 14页(LNCS) | Springer LNCS | 同 CVPR，页数宽裕 |
| **AAMAS** | Autonomous Agents & Multi-Agent Systems | B | 10月 | 12页 | Springer LNCS | **Agent 专门会议** |
| **IJCAI** | Int'l Joint Conf. on AI | A | 1月 | 7页 | IJCAI style | Agent 综合 |
| **KDD** | Knowledge Discovery & Data Mining | A | 2月 | 8页 | ACM style | Agent+数据 |
| **UIST** | User Interface Software & Technology | B | 5月 | — | ACM style | 人机协作/拟人化 |
| **SIGCHI** | Human Factors in Computing Systems | A | 9月 | — | ACM style | 同 UIST |

---

## 期刊（按中科院分区 / CCF 分级）

### 顶刊（1 区 / CCF A）

| 期刊 | 全称 | 中科院区 | CCF | IF≈ | Agent 适配 |
|---|---|:---:|:---:|:---:|---|
| **IEEE TPAMI** | Trans. on Pattern Analysis & Machine Intelligence | 1 | A | 24.7 | 多模态/具身/视觉 Agent 长文 |
| **IEEE TKDE** | Trans. on Knowledge & Data Engineering | 1 | A | — | 知识图谱/语义 Agent/场景图 |
| **IEEE TNNLS** | Trans. on Neural Networks & Learning Systems | 1 | B | 8.9 | 前馈/学习类 Agent |
| **IJCV** | Int'l Journal of Computer Vision | 1 | A | — | 视觉/具身/3D Agent |
| **Information Fusion** | Information Fusion | 1 | — | 15.5 | 多模态融合/Cross-Domain |
| **JAIR** | Journal of AI Research | 4(CCF A) | A | — | 算法/推理理论 |

### 系统与应用

| 期刊 | 全称 | 中科院区 | CCF | Agent 适配 |
|---|---|:---:|:---:|---|
| **ACM TIST** | Trans. on Intelligent Systems & Technology | 3 | B | 系统类/工程落地 |
| **Engineering Applications of AI** | — | 1 | — | 工业/仿真/具身应用 |
| **Expert Systems with Applications** | — | 1 | C | 工业/医学应用 |
| **Knowledge-Based Systems** | — | 1 | C | 语义/场景图/知识 |
| **Neurocomputing** | — | 2 | C | 学习类（国人友好） |
| **Medical Image Analysis** | — | 1 | — | 医学 Agent |

### Agent 专门期刊

| 期刊 | 全称 | 备注 |
|---|---|---|
| **JAAMAS** | Journal of Autonomous Agents and Multi-Agent Systems | Springer，**Agent 专门期刊** |
| **AIJ** | Artificial Intelligence（Elsevier） | AI 基础理论，含 Agent |

### 中文核心

| 期刊 | Agent 适配 |
|---|---|
| 计算机学报 | Agent 综述/系统 |
| 软件学报 | Agent 系统/理论 |
| 计算机研究与发展 | Agent 应用 |
| 自动化学报 | Agent/RL |
| 中国图象图形学报 | 视觉/具身/3D Agent |
| 图形学学报 | CG/具身交叉 |

---

## 审稿偏好速查

### CVPR / ICCV / ECCV
- 实验必须充分，至少 3 个 benchmark
- 定性可视化质量很重要
- 附 supplementary 常见
- 喜欢有实际应用场景的 motivation

### NeurIPS / ICML / ICLR
- 理论分析是加分项（收敛性、复杂度）
- 可复现性要求高（建议附代码）
- ICLR 重视 open review 互动

### ACL / EMNLP
- 语言任务实验设计要严谨（统计检验）
- 引用格式严格（ACL style）
- 重视 human evaluation（如适用）

### AAMAS
- Agent 专门会议，审稿人都是 Agent 领域
- 重视多智能体系统的理论建模
- 页数宽裕（12页 LNCS），可展开详细建模

### TPAMI / IJCV（期刊）
- 审稿周期长（4-6 月），但可发长文
- 要求 thorough 的实验和 analysis
- TPAMI 录用率约 15%

---

## 会议扩展为期刊版的合规路径

- 需 30% 以上实质性增量（非简单拼接）
- 常见路径：CVPR → TPAMI；NeurIPS → JMLR；AAMAS → JAAMAS
- 投稿时在 cover letter 说明与会议版的增量

---

## 使用建议

1. **阶段2·骨架**：根据论文定位（Technique / New Problem / Benchmark）初选 venue
2. **阶段7·审稿自查**：用目标 venue 的审稿偏好逐项检查
3. **阶段8·返修**：cover letter 说明增量（如适用期刊扩展版）
4. **引用格式**：本 skill 默认 arXiv ID 格式，投稿时按 venue 官方格式转换
5. **页数**：以 venue 官网当年要求为准，本表为常规值
