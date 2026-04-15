# Capstone Scorecard

## Summary

- **Candidate**: [full name]
- **Repo**: [GitHub URL]
- **Tech Stack**: [backend language + framework, frontend framework, streaming protocol]
- **SDK Used**: [claude_agent_sdk / @anthropic-ai/sdk / Gemini / LangGraph / other]
- **Verdict**: [STRONG HIRE / HIRE / MAYBE / REJECT]
- **Total Score**: X.X / 4.0 (XX / 100)
- **Stretch Bonus Applied**: +X.X (or "None")
- **Auto-Reject Triggered**: Yes — [state which rule and why] / No

---

## Scores

### D1 — Claude Agent SDK Integration (25%) — Score: X / 4

**SDK identification:**
- Package/dependency: [exact package name and version from package.json/pyproject.toml]
- Imports: [exact import statements with file path]
- Classes used: [ClaudeSDKClient / AgentDefinition / HookMatcher / ClaudeAgentOptions — or none]

**Evidence from code:**
- [direct quote or observation, with file path]

**Key findings:**
- Hooks registered: [PreToolUse / PostToolUse / SubagentStart / SubagentStop — or none]
- `parent_tool_use_id`: [correctly used / always null / absent]
- Orchestration driver: [LLM via Task tool / hardcoded code sequence]
- Live SDK or mock-only: [live / mock-only / no LLM at all]

**Concerns:**
- [gaps]

---

### D2 — Agent Orchestration & Prompt Design (15%) — Score: X / 4

**Agent definitions:**

| Agent | Defined as | Prompt source | Tools | Model |
|-------|-----------|---------------|-------|-------|
| lead-analyst | [AgentDefinition / JS function / etc.] | [file path or inline] | [tool list] | [model] |
| web-researcher | ... | ... | ... | ... |
| data-analyst | ... | ... | ... | ... |
| report-writer | ... | ... | ... | ... |

**Evidence from code:**
- [file path + observation about prompt quality, tool scoping, allowed_tools]

**Concerns:**
- [prompt gaps, missing ask_user instructions, tool scoping issues]

---

### D3 — Event Decode & Trace Tree Correctness (20%) — Score: X / 4

**Event type coverage:**

| Event Type | Handled? | Typed? | Tested? |
|-----------|----------|--------|---------|
| session_start | Yes / No / Partial | Yes / No | Yes / No |
| agent_start | ... | ... | ... |
| thinking | ... | ... | ... |
| tool_start | ... | ... | ... |
| tool_end | ... | ... | ... |
| agent_end | ... | ... | ... |
| ask_user | ... | ... | ... |
| user_answer | ... | ... | ... |
| final_message | ... | ... | ... |
| error | ... | ... | ... |
| session_end | ... | ... | ... |

**Tree builder:**
- Routing method: [`parent_tool_use_id` lookup / agent-type inference / flat list]
- Parallel agent handling: [sibling nodes by ID / sequential / not handled]

**Concerns:**
- [missing types, wrong routing, test gaps]

---

### D4 — Architecture & Stream Design (15%) — Score: X / 4

**Evidence from code:**
- [SSE implementation, normalization layer, ask_user mechanism, state management]

**Concerns:**
- [stream closes on ask_user, no normalization, race conditions]

---

### D5 — UI/UX Quality (10%) — Score: X / 4

**Evidence from code:**
- [trace panel, parallel viz, chat status, agent badges, artifacts, ask_user UI]

**Concerns:**
- [idle chat, missing badges, sequential parallel agents]

---

### D6 — Code Quality & Testing (10%) — Score: X / 4

**Evidence from code:**
- [typing approach, test coverage, component structure, dead code]

**Test inventory:**

| Test file | Coverage | Event types tested |
|-----------|----------|-------------------|
| [file path] | [what it tests] | [which events] |

**Concerns:**
- [untyped payloads, missing tests, dead code]

---

### D7 — Builder DNA & Delivery (5%) — Score: X / 4

**Evidence:**
- README: [quality assessment]
- `.env.example`: [present / absent]
- Design doc: [sections present out of 7]
- Known limitations: [documented / not]

**Concerns:**
- [missing docs, broken setup]

---

### D8 — Stretch Features (bonus)

| Feature | Implemented? | Bonus |
|---------|-------------|-------|
| Stream reconnection + replay | Yes / No | +0.10 / 0 |
| Multi-conversation / persistence | Yes / No | +0.10 / 0 |
| Activity ticker | Yes / No | +0.05 / 0 |
| Agent spawn guard | Yes / No | +0.05 / 0 |
| Retry on error | Yes / No | +0.05 / 0 |
| Auto-collapse nodes | Yes / No | +0.05 / 0 |

**Total stretch bonus**: +X.X

---

## Score Calculation

```
(D1 × 0.25) + (D2 × 0.15) + (D3 × 0.20) + (D4 × 0.15) + (D5 × 0.10) + (D6 × 0.10) + (D7 × 0.05) + stretch
= (X × 0.25) + (X × 0.15) + (X × 0.20) + (X × 0.15) + (X × 0.10) + (X × 0.10) + (X × 0.05) + X.X
= X.X / 4.0 (XX / 100)
```

---

## Overall Assessment

[2–3 sentences. Specific. Reference dimension scores and code evidence. Plain language.]

---

## Technical Deep Dive

*(Include ONLY if --deep-dive flag was set. Omit entirely otherwise.)*

### SDK & Architecture Detail
[Exact SDK imports, ClaudeAgentOptions construction, AgentDefinition fields, hook registrations, prompt file contents summary]

### Event Pipeline Detail
[Event flow diagram, all event types with data fields, parent_tool_use_id routing logic, parallel agent disambiguation]

### ask_user Flow Detail
[Backend blocking mechanism, frontend rendering, end-to-end sequence with file/line references]

### Grilling Questions

1. **[Question]** — Expected answer: [what a strong answer includes]. Weak answer signal: [what to watch for].
2. **[Question]** — Expected: [...]. Weak signal: [...].
3. **[Question]** — Expected: [...]. Weak signal: [...].
4. **[Question]** — Expected: [...]. Weak signal: [...].
5. **[Question]** — Expected: [...]. Weak signal: [...].
6. **[Question]** — Expected: [...]. Weak signal: [...].

---

## HR Phone Screen Questions

*(Include ONLY if advancing — omit entirely for REJECT.)*

1. **[Question]** — What to listen for: [what a good answer sounds like]
2. **[Question]** — What to listen for: [...]
3. **[Question]** — What to listen for: [...]

---

## Technical Interview Questions

*(Include ONLY if advancing — omit entirely for REJECT.)*

1. **[Question]** — Probes: [what this tests and what a strong answer demonstrates]
2. **[Question]** — Probes: [...]
3. **[Question]** — Probes: [...]

---

## Red Flags

- [Concern that exists regardless of score]

OR

None identified.
