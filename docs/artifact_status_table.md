# Artifact Status Table
## Source, Assumption, and Reproducibility Categories

## Purpose

This file separates the main kinds of public values and artifacts in the v25.9 release. It prevents sourced evidence, stylized assumptions, design priors, profile-assigned values, generated outputs, and future validation targets from being collapsed into one claim type.

| Category | Meaning | Examples | Public status |
|---|---|---|---|
| External source anchor | Background fact or institutional context supported by external references | Hormuz chokepoint exposure, War Powers reporting baseline, maritime chokepoint background | Cited in working paper / evidence sources |
| Design prior | Conceptual weight or formula choice used for structured comparison | Governance-erosion component weights; epistemic-integrity weights | Explicit and inspectable; not empirically estimated |
| Profile-assigned value | Config value assigned to a governance condition | Platform dependency 0.15 / 0.65; legal cohesion; congressional constraint | Public config assumption; rerunnable |
| Generated public artifact | Output produced by the bounded public runner from public configs and formulas | `governance_summary.md`; `governance_comparison.json`; overlay summaries | Reproducible with public runner |
| Architectural lineage | Broader internal design inventory not fully executed by public package | 72 core variables; six layers; two-dozen module families | Documented as lineage, not public validation surface |
| Future validation target | Planned robustness or reproducibility extension | Platform-dependency sensitivity sweep; peak-stress saturation test; minimal module fixture | Roadmap item; not current result |
| Non-executable scenario brief | Public mechanism sketch for future cross-theater work | Bab el-Mandeb, Suez, Panama, Taiwan / South China Sea briefs | Contextual roadmap; not executable scenario pack |

## Reading rule

Public claims that depend on reproducibility should rest on public formulas, public configs, bounded runner outputs, and generated artifacts. Architectural lineage and future validation targets should not be used as evidence for Section 4 public comparison outputs unless the relevant fixtures are released.
