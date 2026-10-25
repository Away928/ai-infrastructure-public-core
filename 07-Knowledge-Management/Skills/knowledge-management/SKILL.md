---
name: knowledge-management
description: Manage explicitly requested persistent knowledge updates, Obsidian organization, provenance and cross-tool references; not ordinary search, reading or one-off summaries.
---

# Knowledge Management — minimal persistence contract

One authoritative original per dataset. Obsidian stores selected durable knowledge; NotebookLM maintains its own notebooks and source references; 01 Information Acquisition owns WeChat article collection/originals. Its optional JSON workbench and HTML are **not** the default knowledge pipeline. Prefer stable IDs, paths and URLs over copying full datasets.

## One review, one commit
1. Read the actual source, current Vault page and Cognitive Engine rules. Distiller emits only genuine Knowledge Deltas (empty is valid); a question or AI idea is not user mastery.
2. Knowledge Manager deduplicates, merges and maps deltas onto existing concepts when possible, then produces exact before/after Diff, source IDs and preimage hashes.
3. Human Review approves or rejects the final Change Set once. Never treat old V1 Delta approval as authorization for new condensed text.
4. Knowledge Commit verifies that exact approved version and destination, applies only the approved content, and stops on conflicts. No second routine approval, no shadow database.
5. If every candidate is redundant, a question without a confirmed cognitive change, or missing decisive source context, stop **before** building a Change Set: no empty approval ceremony, no automatic USER mastery. For a new Concept that does merit a proposal, show the complete final page and every exact navigation/count edit to `index.md` and the **existing** domain `_domain.md` in the same chat-native review. Ordinary Entity bodies and Raw Sources are not writable via the domain-navigation exception.

## Select only the relevant specialist
- Obsidian Markdown = note syntax; Bases = dynamic views; Canvas = visual graphs; CLI = direct vault operations. Do not automatically load all four.
- NotebookLM is shared from Research Workspace via a symlink; do not install or bulk-sync another copy.
- WeChat acquisition now belongs to 01 via a single-source entry. Keep original article IDs/URLs, do not auto-copy full articles or start the legacy JSON KB/HTML; selectively synthesize via 05 Knowledge Manager only after the final user-approved Change Set.
- Information Acquisition obtains; Research analyzes; Knowledge Management persists.

No unsolicited writes, destructive migration, external upload, automatic cross-platform sync or new persistent index. Respect the real Vault's agent instructions, immutable raw sources and one-review boundary.
