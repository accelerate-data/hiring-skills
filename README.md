# Eval Skills

Evaluate submissions with rubrics, scorecards, and resume screening.

## Skills

| Skill | Description |
|-------|-------------|
| `grade-all` | Batch-grade all capstone submissions |
| `grade-submission` | Grade a single capstone submission |
| `list-capstone-rubrics` | List available capstone evaluation rubrics |
| `screen-resume` | Screen resumes against job rubrics with scorecards |
| `list-resume-rubrics` | List available resume screening rubrics |

## Install

```bash
claude plugin add accelerate-data/eval-skills
```

## Local development

```bash
claude --plugin-dir .      # Load without installing
claude plugin validate .   # Validate structure
```

## Updating the plugin

1. Make your changes to skills, commands, or rules
2. Bump `version` in `.claude-plugin/plugin.json`
3. Validate: `claude plugin validate .`
4. Test locally: `claude --plugin-dir .`
5. Commit and push — the marketplace picks up the latest default branch automatically (no version field in marketplace entries)
