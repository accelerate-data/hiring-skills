---
name: list-capstone-rubrics
description: "List all available capstone evaluation rubrics. Use when someone asks what rubrics exist, what they can evaluate against, or says: list rubrics, what rubrics are available, what roles can I evaluate."
---

# List Available Rubrics

List all capstone evaluation rubrics available.

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

**To evaluate a submission**: Provide a student name or path and say which rubric to use (or leave unspecified to use the only available rubric).

---

If no rubric files exist, say:
"No rubrics are available yet. Please ask your admin to add one."

**Important**: Only list rubrics for which a file exists in `${CLAUDE_PLUGIN_ROOT}/rubrics/`. Do not suggest, invent, or list any others.
