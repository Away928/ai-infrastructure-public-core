# AI Infrastructure — Public Core

**A small, readable collection of AI workflow skills, organized by capability rather than model or product.**

[Release v0.1.0](https://github.com/Away928/ai-infrastructure-public-core/releases/tag/v0.1.1) · [Skills catalog](catalog.json) · [MIT License](LICENSE) · [中文说明](#中文简介)

> **Scope:** This is a curated **Skill/documentation pack**, not the author's complete private AI environment. It does not bundle working MCP servers, third-party plugins, credentials, or client configurations.

## What is here?

The public core follows one consistent structure across eight capability areas:

```text
Capability area/
├── Skills/     # Task-specific instructions and references
├── Plugins/    # Reserved for future reviewed integrations
└── MCPs/       # Reserved for future reviewed integrations
```

The **11 included Skills** are:

| Area | Available Skills | Purpose |
| --- | --- | --- |
| Research | [Academic Research](02-Research/Skills/academic-research/SKILL.md), [Investment Research](02-Research/Skills/investment-research/SKILL.md) | Evidence-based academic and investment analysis |
| Development | [Development Toolkit](03-Development/Skills/development-toolkit/SKILL.md) | Optional engineering practices; native tools first |
| Career | [Opportunity Evaluation](05-Career/Skills/career-opportunity-evaluation/SKILL.md), [Fact Verification](05-Career/Skills/career-fact-verification/SKILL.md), [Content Writing](05-Career/Skills/career-content-writing/SKILL.md), [Application Tracking](05-Career/Skills/career-application-tracking/SKILL.md), [Assessment Preparation](05-Career/Skills/career-assessment-preparation/SKILL.md) | Five distinct steps from evaluating roles to interviews |
| Documents | [HTML Page Builder](06-Documents/Skills/HTML/html-page-builder/SKILL.md), [PDF Quality Check](06-Documents/Skills/PDF/pdf-quality-check/SKILL.md) | Source-level webpage creation and PDF inspection |
| Knowledge Management | [Knowledge Management](07-Knowledge-Management/Skills/knowledge-management/SKILL.md) | Deliberate, reviewed persistence of knowledge |

**Not included in v0.1:** Information Acquisition, Media, and Special have no bundled Skills. Empty directories are intentional; they do not indicate working installed tools. Some Skills refer to external utilities or private-workspace conventions. Those dependencies are **not included** and may need adaptation.

## Try it in two minutes

**Requirements:** Python 3.9+ for validation; a text editor or compatible AI agent for the Skill instructions. No API key, installation script, or network access is required for inspection.

```bash
git clone https://github.com/Away928/ai-infrastructure-public-core.git
cd ai-infrastructure-public-core
python3 scripts/verify_release.py
```

Then open, for example, [Investment Research](02-Research/Skills/investment-research/SKILL.md) or [Career Content Writing](05-Career/Skills/career-content-writing/SKILL.md). Read its `SKILL.md` together with any nearby `references/` documents.

These are **agent-readable instructions**, not Python packages or standalone executables. To use one with your agent, follow that client's documented Skill installation conventions and supply any optional external tools yourself. Do not copy the whole repository into a global skill directory indiscriminately.

## Design choices

1. **One responsibility per capability.** Avoid duplicate layers and overlapping Skills.
2. **Native tools first.** Add an integration only when it fills a real gap.
3. **Evidence over ceremony.** Make facts, limits, and verification explicit without imposing a heavyweight process on simple requests.
4. **Portability over personal setup.** Never rely on the author's local caches, machine paths, or accounts.

## Quality and release scope

The included `catalog.json` lists exactly what is shipped. `scripts/verify_release.py` checks the 8 × 3 directory layout, 11 Skill entries, the file allowlist, and SHA-256 manifest integrity. The same check runs in [GitHub Actions](https://github.com/Away928/ai-infrastructure-public-core/actions).

Passing this check **does not** certify that every optional integration works on another computer. There are no included Plugin/MCP server implementations. This is an early, intentionally small release; see [Release Scope](RELEASE_SCOPE.md) and [Third-Party Notices](THIRD_PARTY_NOTICES.md).

## Contributing and security

Bug reports, broken paths, improved examples, and focused capability proposals are welcome via [Issues](https://github.com/Away928/ai-infrastructure-public-core/issues). Read [Contributing](CONTRIBUTING.md) first. Do **not** post secrets, private documents, or exploitable security details in public issues; follow [Security](SECURITY.md).

**License:** [MIT](LICENSE) for included original material. Referenced third-party software, brands, and services keep their own terms.

## 中文简介

AI Infrastructure Public Core 是一个**按能力分类的 AI 工作流 Skill 集合**，而不是可一键安装的完整 Agent 平台。

- 当前提供 **11 个精选 Skill**，覆盖研究、开发、求职、文档和知识管理。
- 八个板块的目录统一保留 `Skills / Plugins / MCPs`；空目录只是分类占位，不代表服务已经实现。
- 使用 `python3 scripts/verify_release.py` 检查发行包；选择所需的 `SKILL.md` 阅读并按所用客户端的规范安装。
- 私有配置、用户资料、第三方完整项目与模型密钥均不在发行包中。

欢迎通过 Issues 提交可复现的问题。该版本属于 **v0.1 公开核心预发布版**，后续功能会在经过验证和授权后逐步加入。
