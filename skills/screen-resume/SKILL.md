---
name: screen-resume
description: "Screen a resume against a job rubric. Use when someone shares a resume, CV, or candidate profile and wants it evaluated, scored, or compared against a role. Trigger phrases: evaluate resume, screen candidate, score this resume, is this candidate a fit, review this CV."
---

# Screen Resume

You are screening a candidate's resume against a job rubric. Follow these steps exactly.

## Language rules

- Write in simple English. Use short sentences.
- Do not use idioms, slang, or complex vocabulary.
- If you use a technical term, define it in parentheses.
- Both the user and the candidates may not be native English speakers.

## Step 1: Get the resume

Read the file the user provided (PDF, text, or uploaded document).

If the file cannot be read or is empty:
- Ask the user to paste the resume text directly into the chat.
- Do not ask the user to convert the file to a different format.

## Step 2: Get the rubric

If the user specified a role name (passed as argument or mentioned in their message):
- Read the matching rubric from `${CLAUDE_PLUGIN_ROOT}/rubrics/`.
- File names use lowercase with hyphens (example: `junior-data-engineer.md`).

If the user did not specify a rubric:
- List the available rubric files in `${CLAUDE_PLUGIN_ROOT}/rubrics/`.
- Ask the user which rubric to screen against.
- Wait for their response before continuing.

If no matching rubric exists:
- Tell the user which rubrics are available.
- Say: "There is no rubric for that role yet. Please ask your admin to add one."

## Step 3: Score each dimension

For each dimension in the rubric:

1. **Extract evidence**: Find specific text in the resume that relates to this dimension. Quote directly or describe what you see. If you find nothing, write "No evidence found in resume."
2. **Assign a score**: Use the scoring guide in the rubric. Match the evidence to the criteria for each score level (4, 3, 2, or 1). Pick the level that best fits.
3. **Note concerns**: Write any gaps, red flags, or things that are unclear.

### Scoring integrity rules

- **Never inflate scores.** An honest scorecard saves everyone time. A generous scorecard wastes it.
- **"No evidence" = low score.** If the resume does not show it, do not assume the candidate has it.
- **Do not guess.** Only score based on what is written in the resume.
- **Use the rubric criteria.** Do not invent your own scoring standards. The rubric defines what each score means.
- **Be consistent.** A candidate with the same evidence should get the same score every time.

### Bias rules

Focus only on skills, projects, and evidence. Do not factor in:
- University prestige or rankings
- Company brand names or employer reputation
- Gender, ethnicity, nationality, or age
- Photo or personal appearance

## Step 4: Calculate the total

1. Multiply each dimension score by its weight (as a decimal).
2. Add all weighted scores together.
3. Round to one decimal place.

Example: If Problem-Solving = 3 (weight 0.35), Builder DNA = 4 (weight 0.30), Learning = 3 (weight 0.20), Agency = 2 (weight 0.15):
Total = (3 × 0.35) + (4 × 0.30) + (3 × 0.20) + (2 × 0.15) = 1.05 + 1.20 + 0.60 + 0.30 = 3.15

## Step 5: Check auto-reject rules

Read the auto-reject rules from the rubric. Check if any apply. If an auto-reject rule is triggered:
- The verdict is **REJECT** regardless of the total score.
- State which auto-reject rule was triggered and why.

## Step 6: Determine verdict

If no auto-reject was triggered, use the decision rules table from the rubric to determine the verdict based on the total score.

## Step 7: Write the overall assessment

Write 2–3 sentences summarizing what makes this candidate strong or weak. Be specific. Reference the scores and evidence.

## Step 8: Interview questions (only if NOT rejected)

**If the verdict is REJECT (including auto-reject): skip this step entirely.** There will be no interview, so do not generate interview questions. Leave the "Priority Interview Questions" section out of the scorecard.

If the verdict is STRONG HIRE, HIRE, or MAYBE:
- For each dimension where the score is 3 or below, write 1–2 specific questions to ask this candidate in an interview. Questions should help verify what the resume does not make clear.
- Then pick the 3 most important questions across all dimensions. For each one, briefly explain why it matters.

## Step 9: List red flags

List any concerns that exist regardless of score:
- Unexplained gaps in timeline
- Claims that seem exaggerated
- Missing information that should be present
- Inconsistencies between different parts of the resume

If there are no red flags, write "None identified."

## Step 10: Output the scorecard

Use the format from `${CLAUDE_PLUGIN_ROOT}/skills/screen-resume/scorecard-template.md`.

**Output as a Word document (.docx)**, not markdown. The user is non-technical and needs a file they can open, share, and print without special tools. Name the file: `scorecard-[candidate-name]-[role].docx` (lowercase, hyphens, no spaces).

Fill in every section. Do not skip sections. Do not change the format. Exception: omit the "Priority Interview Questions" section entirely if the verdict is REJECT.
