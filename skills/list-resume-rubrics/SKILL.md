---
name: list-resume-rubrics
description: "List all available screening rubrics. Use when someone asks what rubrics exist, what they can screen for, which rubrics are available, or says: list rubrics, what can I screen, available rubrics, what rubrics do we have."
---

# List Available Rubrics

List all screening rubrics available for resume evaluation.

## Steps

1. Read all files in `${CLAUDE_PLUGIN_ROOT}/rubrics/`.
2. For each rubric file, extract:
   - The role name (from the `#` heading)
   - The company name (from the **Company** field)
   - The summary (from the **Summary** field)
   - The number of dimensions
3. Display the results in this format:

---

**Available rubrics:**

| # | Rubric | Summary | Dimensions |
|---|--------|---------|------------|
| 1 | [Role name] | [Summary] | [count] |

**To screen a resume**: Upload or paste a resume and say which rubric to screen against.

---

If no rubric files exist, say:
"No rubrics are available yet. Please ask your admin to add one."

**Important**: Only list rubrics for which a file exists in `${CLAUDE_PLUGIN_ROOT}/rubrics/`. Do not suggest, invent, or list any others.
