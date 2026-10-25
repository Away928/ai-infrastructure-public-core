# v0.1 public release scope

This repository deliberately ships a **small, curated core**, not the author's complete AI Infrastructure workspace.

**Included:** 11 original Skill guidance packages, eight capability-area folders with three consistent categories (`Skills`, `Plugins`, `MCPs`), manifest, offline verifier, CI, and MIT license.

**Excluded:** private account configuration, credentials, user work, archives and full third-party source trees, binaries, MCP/Plugin deployments, installed dependencies and runtime output.

The initially considered `corporate-disclosures` Skill depends on a separately installed CLI; the `grill-me` and `grilling` texts need additional provenance review. None is included in this version. Empty category folders are structural placeholders **only**.

## Verification

Run `python3 scripts/verify_release.py`. It checks file SHA-256, expected directory layout and the 11 entries in `catalog.json`. The same check runs in GitHub Actions. It does **not** validate every external reference or guarantee integration portability.

Any future Skill, MCP or Plugin addition should bring explicit provenance/licensing, reproducible setup instructions, tests where applicable, and a minimal dependency boundary.
