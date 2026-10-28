# Contributing to Awesome-Agent-Engineering

Thank you for your interest in contributing! This repo is a living, auto-updated knowledge base for AI Agent research, industry applications, startup innovation, and enterprise deployment.

## How to Contribute

### 1. Add a Method / Framework / Case / Benchmark

Every entry must be **verifiable** — we follow an evidence protocol (adapted from the R-protocol):

- **Self-stated name**: The method/project name must appear in the paper's own title or abstract, or in the project's official repo description. No fabricated names.
- **Reachable source**: arXiv ID must resolve; GitHub URL must be live; benchmark must have a public leaderboard or paper.
- **One entry, one identity**: No duplicates. If two projects share a name, disambiguate with a suffix.
- **No marketing fluff**: Descriptions are technical and factual.

### 2. Verification Protocol (A1–A5)

| Rule | Requirement |
|------|-------------|
| A1 | Method name self-stated in title/abstract or repo README |
| A2 | arXiv ID (if any) verified reachable via the arXiv API |
| A3 | GitHub/code URL (if any) live and points to the real project |
| A4 | Venue (if any) from the paper's official metadata, not guessed |
| A5 | Description is a one-line technical summary, no hype words |

### 3. Submission Checklist

- [ ] Entry added to the correct `data/*.json` (the single source of truth)
- [ ] `scripts/validate_kb.py` passes with no errors
- [ ] Carrier files (`references/*-overview.md`) regenerated via `scripts/sync_carriers.py`
- [ ] No AIGC watermark or AI-trace words in descriptions
- [ ] PR description states the source URL for each new entry

### 4. Auto-Update Pipeline

Daily arXiv scans and weekly industry trend scans run automatically. If you want to **manually trigger** a scan:

```bash
python scripts/daily_arxiv_scan.py          # discover new Agent papers
python scripts/weekly_industry_scan.py      # discover new frameworks/cases/startups
python scripts/sync_carriers.py             # regenerate markdown overviews
python scripts/validate_kb.py               # validate knowledge base integrity
```

### 5. Style Guide

- Descriptions: ≤120 chars, active voice, technical terms only, no "groundbreaking" / "revolutionary" / "state-of-the-art" unless quantified.
- Categories: use the existing taxonomy; propose new categories via an issue first.
- Dates: ISO 8601 (`YYYY-MM-DD`).

## Code of Conduct

Be respectful, factual, and constructive. Disagreements about taxonomy or admission criteria should be discussed in issues, not in PR flame wars.

## License

By contributing, you agree that your contributions are licensed under the Apache 2.0 License.
