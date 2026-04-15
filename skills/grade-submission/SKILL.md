---
name: grade-submission
description: "Evaluate a single capstone submission against the rubric. Use when someone provides a student name, git URL, or submission path and wants it graded, scored, or assessed. Trigger phrases: grade arpit, evaluate duy, score ext/khang, assess this submission, how did [name] do. Supports --deep-dive flag for detailed technical analysis."
---

# Grade Submission

You are evaluating a single capstone submission for the agent-transparent chat application challenge. Follow these steps exactly.

## Input Formats

The user can provide submissions in any of these formats:

1. **Git URL + name**: `grade "Hong Dao" https://github.com/HONG-DAO/Deep-Analyst-Research-Intelligence-Platform`
2. **Local path**: `grade ext/duy`
3. **Student name** (if already cloned): `grade arpit`
4. **Multiple in one command**: `grade-all` with a list of `name: url` pairs

## Options

- **`--deep-dive`** — Show detailed technical deep dive per candidate with per-dimension evidence, grilling questions, and the full scorecard. Default is OFF (summary table only).

## Step 1: Locate the submission

Resolve the submission path:
- **Git URL given** → Clone into a temp directory or `ext/[name]` if a name is provided. Use `git clone --depth=1` for speed.
- **Local path given** → Use as-is.
- **Student name given** → Look for `ext/[name]` relative to the capstone repo root. Check main branch and `origin/develop` (some repos have code on develop only).
- **`hitesh`** → use `ext/hitesh` (contains two subdirs: `deep-analyst-api/` and `deep-analyst-app/`)

If the path does not exist and no URL was provided, ask the user for the git URL.

## Step 2: Get the rubric

If the user specified a rubric name:
- Read the matching rubric from `${CLAUDE_PLUGIN_ROOT}/rubrics/`.

If the user did not specify a rubric:
- List available rubrics in `${CLAUDE_PLUGIN_ROOT}/rubrics/`.
- If only one rubric exists, use it automatically and note this.
- If multiple exist, ask the user which to use.

## Step 3: Read top-level artifacts

Read these files if they exist:
- `README.md` — setup instructions, architecture overview, known limitations
- `DESIGN.md` / `docs/design-doc.md` / `DESIGN_DOC.md` — 1-pager design document

Note: whether a design doc exists, which Amazon sections it covers, and whether setup instructions are complete.

## Step 4: Identify tech stack and SDK

Inspect `package.json`, `pyproject.toml`, `requirements.txt`, `uv.lock`, `server.js`, `main.py`, or equivalent.

**Critical SDK identification — read actual imports, do not infer:**
- Search for `claude_agent_sdk` or `claude-agent-sdk` in imports and dependency files
- Search for `@anthropic-ai/sdk` (raw Messages API — different from Agent SDK)
- Search for `@google/generative-ai`, `langchain`, `langgraph`, `openai` (wrong SDK)
- Check which classes are imported: `ClaudeSDKClient`, `AgentDefinition`, `HookMatcher`, `ClaudeAgentOptions`

Also identify:
- Frontend framework and state management
- Streaming protocol (SSE / WebSocket / polling)

## Step 5: Trace agent definitions and prompts

Find where agents are defined. Look for:
- `AgentDefinition` objects with `description`, `prompt`, `tools`, `model` fields
- Plugin directories (`.claude/plugins/`)
- Prompt files (`.txt`, `.md`) in a prompts directory
- Inline prompt strings in orchestrator code
- `allowed_tools`, `allowed_plugins` on `ClaudeAgentOptions`
- `HookMatcher` registrations for `PreToolUse`, `PostToolUse`, `SubagentStart`, `SubagentStop`

Note how the orchestration is driven: by the LLM (via `Task` tool in the prompt) or by code (hardcoded function call sequence).

## Step 6: Trace the event decoder

Find the file responsible for routing normalized events to state. Common names: `decoder.ts`, `normalizer.py`, `eventDecoder.ts`, `stream-parser.ts`, `eventDispatcher.js`, `event_decoder.py`.

Read it fully. For each required event type from the rubric, check:
- Is it handled explicitly (not via a default catch-all)?
- Is it typed (discriminated union, Pydantic, or Zod — not `any`)?
- Is there a corresponding test?

## Step 7: Trace the tree builder

Find the logic that constructs the nested agent trace tree from flat events. Common names: `tree-builder.ts`, `agentTreeStore.js`, `trace-store.ts`, `buildAgentTree`.

Check:
- Is `parent_tool_use_id` used to link sub-agent events to their parent node?
- Or does it use agent-type/name inference (fragile for parallel same-named agents)?
- Are parallel agents rendered as siblings under the same parent?
- Does the tree grow incrementally as events arrive?

## Step 8: Inspect SSE / stream layer

Find the backend SSE endpoint.

Check:
- Does the stream stay open during `ask_user` pause (not close and reconnect)?
- Is the `ask_user` answer submitted via a separate HTTP POST?
- Does the backend normalize raw SDK events before emitting?
- Is there a mock mode for development without API key?

## Step 9: Inspect UI components

Find and read the trace panel, chat panel, and any parallel visualization components.

Check:
- Trace panel: expand/collapse per node? Tool inputs/outputs on expand?
- Parallel visualization: sub-agents shown side-by-side or one after the other?
- Agent state indicators: visual badges for queued / running / completed / failed?
- Chat panel: live activity text during run, or idle?
- Artifacts: collected from agent outputs and surfaced in UI?
- `ask_user` UI: visually prominent? Keyboard-accessible?

## Step 10: Check tests

Find all test files (`__tests__/`, `tests/`, `*.test.ts`, `test_*.py`).

For each test file, note what it covers and whether it includes edge cases (nested contexts, parallel agents, error events).

## Step 11: Score each dimension

For each dimension in the rubric (D1–D7 plus D8 stretch):

1. **Extract evidence** — Quote directly from files (include file path). Label any GitHub data "(from GitHub)".
2. **Assign a score (1–4)** — Match evidence to rubric criteria. Do not round up. "No evidence" = low score.
3. **Note concerns** — Gaps, missing features, architectural risks.

### Scoring integrity rules

- **Never inflate.** An honest scorecard saves everyone time.
- **"No evidence" = low score.** If the code does not show it, do not assume.
- **Do not guess.** Score only from what you can read.
- **Use the rubric criteria.** Do not invent your own standards.

## Step 12: Check auto-reject rules

Read the auto-reject rules from the rubric. If any trigger:
- Verdict is **REJECT** regardless of total.
- State which rule triggered and why.

## Step 13: Calculate total score

Use the formula from the rubric. Round to one decimal place. Total capped at 4.0.

Convert to /100 scale for the summary table: `score_100 = total × 25`.

## Step 14: Determine verdict

Use the decision rules table from the rubric.

## Step 15: Write overall assessment

2–3 sentences. Specific. Reference dimension scores and code evidence.

## Step 16: Technical Deep Dive (only if --deep-dive flag is set)

**If --deep-dive is NOT set: skip this step entirely.**

If --deep-dive IS set, produce a detailed technical analysis covering:

### SDK & Architecture
- Exact SDK imports (file paths and line numbers)
- How `ClaudeAgentOptions` is constructed (every field)
- How agents are defined (AgentDefinition fields or equivalent)
- All prompt files and their key instructions
- Hook registrations and what each hook does

### Event Pipeline
- How events flow from SDK → backend → SSE → frontend → state → UI
- Every event type emitted and its data fields
- The `parent_tool_use_id` routing logic (the lookup maps, resolution sequence)
- How parallel agents are distinguished

### ask_user Flow
- Backend: what blocks, what unblocks, does stream stay open?
- Frontend: what renders, how answer is submitted
- End-to-end sequence with file/line references

### Grilling Questions (6-8 questions)
Generate probing technical questions specific to THIS submission. Include:
- Questions about SDK/architecture decisions the candidate made
- Questions that test whether they understand their own code
- Expected answers and what a weak answer would reveal
- At least 2 questions targeting the candidate's weakest dimension

## Step 17: Interview questions (only if NOT rejected)

**If verdict is REJECT (including auto-reject): skip this step entirely.**

If advancing, generate two sets:

**Set 1 — HR Screen Questions (3 questions)**
- Non-technical. Behavioral and situational.
- Target gaps from the scorecard.
- Include "what to listen for" for each question.

**Set 2 — Technical Interview Questions (3 questions)**
- Specific to this submission's architecture and gaps.
- Target the highest-weight dimension gaps.
- Include what a strong answer demonstrates.

## Step 18: List red flags

- Missing `.env.example` but app requires API keys
- No run instructions
- Single initial commit (no iteration visible)
- Claims not backed by code
- Sensitive data (API keys) committed to repo
- Wrong SDK used (Gemini, LangGraph, OpenAI instead of Claude Agent SDK)

If none: "None identified."

## Step 19: Output the scorecard

Use the format from `${CLAUDE_PLUGIN_ROOT}/skills/grade-submission/scorecard-template.md`.

Output as formatted markdown directly in the chat. Fill every section. Do not skip sections. Omit interview questions only if verdict is REJECT. Include technical deep dive only if --deep-dive was set.
