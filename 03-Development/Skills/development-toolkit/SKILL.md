---
name: development-toolkit
description: "Optional compact reference for large repository refactors, specialized JS/Electron reverse-engineering, and engineering workflows. For normal coding, debugging, browser work and Skill creation, use the active Agent's native tools directly; do not load a generic router."
---

# Development Toolkit — native first

Use the Agent's built-in repository inspection, planning, editing, debugging, testing, code review and browser tools. Do not force extra frameworks, subagents, routing or evaluation on routine tasks.

For substantial architecture/refactoring decisions, use the existing `skills/engineering-five-step/SKILL.md`: **question → delete → simplify → accelerate → automate last**. Reproduce bugs and run proportionate regression tests; never claim unexecuted tests passed. Before deleting or changing live client configuration, inspect dependencies, back up and obtain approval as required.

## Specialized paths only when needed

- **REA (optional external integration)**: not shipped here. Prefer native source inspection for ordinary code. If you independently install REA for authorized opaque JS/Electron or ASAR analysis, follow its upstream documentation and client approval rules. Never bypass an explicit MCP approval rejection.
- **UI design**: use native implementation and visual review. Any external style reference library must be installed separately; this package does not ship one.
- **Browser**: prefer the current agent's browser support. Install and configure Playwright or other browser tooling separately only when the task requires it.
- **Skill creation**: Codex uses its native system Skill Creator / Installer; Claude uses its existing global creator when needed. `skill-toolkit` supplies third-party discovery through `find-skills`, not a second required creator pipeline.
- **Optional reference**: specialized TDD/debugging guides can be used when independently available, but are not bundled or automatically loaded here.

No automatically installed agents, new MCP servers, or background processes are implied by this guide.
