# 顶刊典范论文样本库（top-paper-samples）

本目录存放 6 篇高影响论文的 PDF 与 LaTeX 源码，作为 `../writing-style-guide.md` 的分析语料与写作范本。

## 样本清单（均经 arXiv API 官方核实）

| 目录 | 论文 | arXiv | Venue | 下载日期 |
|---|---|---|---|---|
| `01-attention-is-all-you-need/` | Attention Is All You Need | [1706.03762](https://arxiv.org/abs/1706.03762) | NeurIPS 2017 | 2026-10-30 |
| `02-chain-of-thought/` | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | [2201.11903](https://arxiv.org/abs/2201.11903) | NeurIPS 2022 | 2026-10-30 |
| `03-react/` | ReAct: Synergizing Reasoning and Acting in Language Models | [2210.03629](https://arxiv.org/abs/2210.03629) | ICLR 2023 | 2026-10-30 |
| `04-toolformer/` | Toolformer: Language Models Can Teach Themselves to Use Tools | [2302.04761](https://arxiv.org/abs/2302.04761) | NeurIPS 2023 | 2026-10-30 |
| `05-3d-gaussian-splatting/` | 3D Gaussian Splatting for Real-Time Radiance Field Rendering | [2308.04079](https://arxiv.org/abs/2308.04079) | ACM TOG / SIGGRAPH 2023 | 2026-10-30 |
| `06-generative-agents/` | Generative Agents: Interactive Simulacra of Human Behavior | [2304.03442](https://arxiv.org/abs/2304.03442) | UIST 2023 | 2026-10-30 |

## 目录结构

每个论文目录内：
- `<arxiv_id>.pdf` — 官方 PDF（看最终排版效果）
- `source/` — 解压后的 LaTeX 源码（研究写作结构与排版技巧用）

> 空间说明：本库约 100 MB，主要为 05（3DGS）与 06（Generative Agents）的高清 PDF 与源码图。若需精简，可删除大 PDF（arXiv 可随时重新下载：`https://arxiv.org/pdf/<id>`）；LaTeX 源码建议保留（含排版细节）。

主文件入口：
- 01: `source/ms.tex`（分节 \input）
- 02: `source/neurips_2022.tex`（单文件）
- 03: `source/iclr2023_conference.tex`（分节 \input；`iclr2023 2_arXiv/` 为重复副本可忽略）
- 04: `source/main.tex`（单文件）
- 05: `source/fast_radiance_fields.tex`（ACM TOG 模板主文件，分节 \input）
- 06: `source/main.tex`（分节 \input，章节在 `source/content/`）

## 版权与使用边界

- 论文版权归原作者；本目录仅用于**本仓库内部写作研究与教学**，不得用于商业再分发
- 下载自 arXiv 官方（e-print 服务），分发遵循 arXiv 站点条款与各论文自身许可
- 若需引用观点，请引用论文原文（按上方 arXiv 链接），不要引用本目录
