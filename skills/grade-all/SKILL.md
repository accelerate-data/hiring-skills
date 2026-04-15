---
name: grade-all
description: "Grade all capstone submissions and produce a ranked comparison table. Use when someone asks to evaluate all submissions, rank all candidates, compare all students, or says: grade all, evaluate all, rank submissions, compare all. Accepts a list of name:url pairs or uses local ext/ paths."
---

# Grade All Submissions

Evaluate all student capstone submissions and produce a ranked comparison table.

## Options

- **`--deep-dive`** — Show detailed technical deep dive per candidate before the summary table. Default is OFF (summary table only with per-candidate scorecard).

## Step 1: Identify submissions

The user provides submissions in one of these formats:

### Format A — Name + Git URL list
```
grade-all:
- "Hong Dao" https://github.com/HONG-DAO/Deep-Analyst-Research-Intelligence-Platform
- "Nguyen Thanh Anh Duy" https://github.com/ntad27/chat-app-capstone
- "Nguyen Trong Quy" https://github.com/nguyenquyking/Research-Intelligence-Platform
```

For each entry, clone the repo with `git clone --depth=1 <url>` into a temp directory or `ext/[shortname]`.

### Format B — Local paths (default)
If no URLs provided, look for submissions in `ext/` relative to the capstone repo root. Ask the user which subdirectories to evaluate.

### Format C — Mixed
Some entries may be local paths, others may be git URLs. Handle both.

For repos where code is on a branch other than `main` (e.g., `develop`), check `git branch -a` and checkout the branch with the most recent commits.

## Step 2: Grade each submission

For each submission, run the full `grade-submission` skill workflow from `${CLAUDE_PLUGIN_ROOT}/skills/grade-submission/SKILL.md`.

- If `--deep-dive` is set, pass it through to each grade-submission call.
- If `--deep-dive` is NOT set, still run the full evaluation internally but only output the scorecard summary (not the technical deep dive section).

Output each complete scorecard as you go — do not batch them all at the end.

## Step 3: Compile the summary comparison table

After all scorecards are produced, output a ranked summary table with the columns defined in the rubric's "Summary Table Columns" section:

---

**Capstone Cohort Ranking**

| Full Name | Repo | Score | SDK Used | `parent_tool_use_id` | ask_user | Tests | Design Doc | TypeScript | Verdict |
|-----------|------|-------|----------|---------------------|----------|-------|------------|------------|---------|
| ... | [owner/repo](url) | XX/100 | claude_agent_sdk ✅ | ✅ Correct | ✅ | N tests ✅ | Complete ✅ | ✅ | STRONG HIRE |
| ... | [owner/repo](url) | XX/100 | ... | ... | ... | ... | ... | ... | ... |

Sort by score descending. Use emoji indicators: ✅ (present/correct), ❌ (absent/wrong), ⚠️ (partial).

---

## Step 4: Compile the dimension breakdown table

Also output a per-dimension breakdown:

| Rank | Name | Total | D1 SDK | D2 Orch | D3 Decode | D4 Arch | D5 UI | D6 Code | D7 Delivery | Stretch | Verdict |
|------|------|-------|--------|---------|-----------|---------|-------|---------|-------------|---------|---------|
| 1 | ... | X.X | X/4 | X/4 | X/4 | X/4 | X/4 | X/4 | X/4 | +X.X | ... |

## Step 5: Write a cohort summary

2–3 sentences on:
- What distinguishes the top submission from the rest
- The most common gap across the cohort
- Any auto-reject triggers and which rules they hit
- Which SDK each candidate used and how that affected their score
