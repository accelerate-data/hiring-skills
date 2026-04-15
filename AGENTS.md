# Hiring Skills Plugin

Shared plugin repository for candidate screening and hiring assessment skills used by Claude Code and Codex.

**Maintenance rule:** This file contains durable repository guidance, not volatile inventory.

## Instruction Hierarchy

1. `AGENTS.md` - canonical, cross-agent source of truth
2. Skill-local references under `skills/<skill>/references/`
3. `CLAUDE.md` - Claude-specific adapter and routing

## Repository Purpose

Single plugin-source repo for hiring skills — candidate screening, assessment grading, and rubric-based evaluation.

- Root manifests: `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`
- Canonical skill content: `skills/`

## Skills

- `skills/grade-all/SKILL.md` - batch-grade all capstone submissions
- `skills/grade-submission/SKILL.md` - grade a single capstone submission
- `skills/list-capstone-rubrics/SKILL.md` - list available capstone evaluation rubrics
- `skills/screen-resume/SKILL.md` - screen resumes against job rubrics with scorecards
- `skills/list-resume-rubrics/SKILL.md` - list available resume screening rubrics

## Conventions

- Keep all skill directories under `skills/`.
