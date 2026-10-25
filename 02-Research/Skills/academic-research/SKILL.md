---
name: academic-research
description: "Coordinate substantive academic research tasks: source-grounded literature reviews, paper analysis, research design, scholarly evidence synthesis, empirical methods or reproducibility checks. Trigger on 学术研究/论文分析/文献综述/研究方法/实证研究/学术写作/literature review/research design; do not trigger for ordinary data analysis, generic reports, one-off definitions, or simple fact lookups."
---

# Academic Research
## Research workflow
Use only the necessary steps for the requested depth. For substantive studies: define question/scope -> select sources -> inspect primary evidence -> compare methods/claims -> reproduce/inspect data when relevant -> synthesize with citations. A one-paper explanation or narrow question should not become a full literature review, reproduction or formal evaluation.

- **Literature**: track exact paper, authors, year, identifiers, what was read, sample, identification, controls, robustness, limitations and open questions.
- **Analysis**: describe provenance, sample selection, preprocessing, equations, variables, assumptions, uncertainty and reproducibility; never invent statistical outputs.
- **Writing**: distinguish known facts, original interpretation and hypotheses; cite verified sources, not hallucinated bibliographies.
- **Sources/tools**: first use the active Agent’s available native search/connectors or directly accessible source; use Search & Access only for a genuine retrieval gap. Research Workspace currently provides NotebookLM-specific operations, not a mandatory research engine. Use Knowledge Management only when persistent notes are explicitly needed; do not copy entire datasets between tools.
- **Evaluation**: use project-owned OIRF evaluator only when explicitly asked to evaluate an OIRF research package; use OIRF meta-evaluator only to assess the evaluator itself. They are not mandatory for ordinary academic work. Locate the current project source before invocation; never assume the former `~/oirf` directory still exists or move project files.
- **Math competitions**: six-stage skills, norms, templates and verification scripts are preserved in ~/.agents/skill-packs/projects/math-modeling/. Project-specific frozen assumptions/status must be read before any modeling modifications.
- **Academic style and Typst**: use default writing tools; optional preserved guidance in ~/.agents/skill-packs/optional/academic-humanizer/ or typst-author/.

Six old generic research writing/how-to guides are archived outside global discovery; the above workflow is canonical.
