# AI Infrastructure — Public Core v0.1.0 RC1

A **curated set of 11 skills** organized into eight capability areas. Every area retains exactly three direct directories: Skills / Plugins / MCPs.

This is **not** a byte-for-byte export of the private AI Infrastructure workspace. Bundled content consists of selected local skill guidance only; externally maintained MCP servers, plugins, massive third-party projects and archives are intentionally **not** redistributed. Empty category placeholders describe the intended structure, not an installed implementation.

## Quick start

1. Choose a capability area, then open its `Skills/<name>/SKILL.md` (some areas have an additional purpose-specific subfolder).
2. Apply the instructions with your own agent environment. External services mentioned in a Skill are **optional integrations**, not bundled or guaranteed available.
3. See `catalog.json` for the exact files included in this distribution.

## Validation

```bash
python3 scripts/verify_release.py
```

No credentials, service integrations or network connections are required for this structural verification.

## Limitations and licensing

This release candidate is a **documentation and skill distribution**, not an installed all-in-one agent environment. Referenced local directories and external integrations from the original workspace may not exist on the recipient's machine. No paid provider, MCP, plugin or third-party tool availability is implied.

**License:** MIT for the original assembled skill guides in this distribution. Upstream external tools and their licenses are **not** included or relicensed. See `THIRD_PARTY_NOTICES.md` for the excluded provider-dependent or uncertain-origin components and `PUBLICATION_GATE.md` for the scope review.
