---
name: development-toolkit
description: "Optional compact reference for large repository refactors, specialized JS/Electron reverse-engineering, and engineering workflows. For normal coding, debugging, browser work and Skill creation, use the active Agent's native tools directly; do not load a generic router."
---

# Development Toolkit — native first

Use the Agent's built-in repository inspection, planning, editing, debugging, testing, code review and browser tools. Do not force extra frameworks, subagents, routing or evaluation on routine tasks.

For substantial architecture/refactoring decisions, use the existing `skills/engineering-five-step/SKILL.md`: **question → delete → simplify → accelerate → automate last**. Reproduce bugs and run proportionate regression tests; never claim unexecuted tests passed. Before deleting or changing live client configuration, inspect dependencies, back up and obtain approval as required.

## Specialized paths only when needed

- **REA**: one 6.5.0 repository at `~/AI-Infrastructure/03-Development/MCPs/rea`, one CLI and one MCP adapter. Use native source reading for ordinary code; use REA for authorized opaque JS/Electron / ASAR analysis. For retained evidence, page with `inspect_analysis_view` using the returned `normalized_result.parent_evidence_id`. Never bypass a client's explicit MCP approval rejection via shell. See `../../../_System/Docs/03-Development/MCPs.md` and the REA Lab on-demand documentation for details.
- **UI design**: use native implementation and visual review; for deterministic local style, palette and UX retrieval, consult `../ui-design-reference/`, not the entire archived UI-UX repository.
- **Browser**: prefer the Agent browser. `~/.agents/skills/playwright-cli` is a preserved optional compatibility path for explicit Playwright/test automation.
- **Skill creation**: Codex uses its native system Skill Creator / Installer; Claude uses its existing global creator when needed. `skill-toolkit` supplies third-party discovery through `find-skills`, not a second required creator pipeline.
- **Optional reference**: Superpowers TDD/debugging and other historical repositories are retained in the Development archive, available via their legacy paths. They are *not* automatically loaded engineering dependencies.

No automatically installed agents, new MCP servers, or background processes are implied by this guide.
