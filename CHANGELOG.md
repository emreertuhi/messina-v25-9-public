# CHANGELOG

All notable changes to the public-facing MESSINA repository should be recorded here.

## [v25.9-public-safe-v8.6] - 2026-05-02

### Changed
- Replaced the working paper with `docs/MESSINA_Working_Paper_v1_5.md`.
- Updated abstract to lead with framework contribution rather than defensive disclaimers.
- Updated keywords to 14 terms optimized for SSRN discoverability.
- Updated JEL codes to 7 (F51, F52, H56, C63, D02, H12, D81).
- Added governance-erosion delta decomposition to Section 3.9, Appendix A.4, formula sheet, and coefficient ledger.
- Clarified that platform dependency is profile-assigned in the public comparison rather than dynamically discovered by the public runner.
- Added interpretation rule to README showing platform-dependency dominance in the governance-erosion delta.
- Added Declaration of Interest, Ethics Approval, and Funder Statement to the working paper.
- Tightened README, CITATION.cff, and public-framing language around the public observer surface.
- Removed stale description language from public configs and regenerated affected artifacts.

### Validation
- Public unit tests rerun successfully after documentation and artifact updates.


## [v25.9-public-safe-v8.5-ssrn] - 2026-04-27

### Added
- Added SSRN working paper link to `README.md` and `CITATION.cff`.

## [v25.9-public-safe-v8.5] - 2026-04-27

### Changed
- Replaced legacy internal shorthand across public configs, artifacts, docs, tests, and parameter tables with neutral `governance_*`, `policy_*`, and `theme_*` naming.
- Renamed documented comparison artifacts to `governance_*` for clearer public readability.

## [v25.9-public-safe-v8.4] - 2026-04-26

### Fixed
- Corrected `docs/source_verification_log_v1_5.md` header and opening note from v1.3 to v1.4.
- Re-verified that generated Python cache directories and `.pyc` files are absent from the packaged public repository.

## [v25.9-public-safe-v8.3] - 2026-04-26

### Added
- Added AI disclosure statement to the working paper for SSRN/public distribution compatibility.

### Fixed
- Corrected Markdown emphasis on the working-paper repository URL line.
- Replaced the public test command with an explicit unittest module invocation.
- Updated public metadata language now that the GitHub repository URL is set.
- Renamed the source verification log to v1.4 and removed stale pre-SSRN wording.
- Strengthened `.gitignore` for local generated files and virtual environments.

## [v25.9-public-safe-v8.2] - 2026-04-26

### Changed
- Kept the public package Markdown-first.
- Consolidated public metadata guidance into `README.md`.
- Removed transient release-management material from the public package.

## [v25.9-public-safe-v8] - 2026-04-26

### Added
- `docs/MESSINA_Working_Paper_v1_5.md`
- `docs/source_verification_log_v1_5.md`
- Explicit public/internal reproducibility boundary language in README and core docs.
- Operationalization bridge language connecting theory families to public proxies.
- Public worked-example explanation for governance erosion.

### Changed
- README is now the primary repository entrance and points first to the v1.4 working paper.
- `docs/release_scope.md`, `docs/article_relation.md`, `docs/validation_status.md`, `docs/limitations.md`, `docs/methodology.md`, and `modules/module_registry.md` now align with the v1.4 public-claim boundary.
- `CITATION.cff` marks final public URL fields for completion after publication.
- `src/public_safe/scenario_loader.py` now performs stricter bounded numeric validation for public config values.

### Removed
- Python cache files from the release package.

### Clarified
- The 72-variable / six-layer / two-dozen-module architecture is broader internal design lineage.
- The public repository exposes the governance-observer subset, not the full internal engine.
- MC512 is internal lineage / future-release context, not a public validation claim.
- The module inventory is architectural documentation, not proof that all modules are publicly executable.

## [v25.9-public-safe-v7]

### Added
- `docs/validation_status.md`
- strengthened `docs/article_relation.md`
- strengthened `analytics/parameter_sources.md`
- friction-spectrum configs
- policy-facing overlays
- thematic overlays
- non-executable scenario briefs
- overlay artifacts

### Clarified
- New configs are descriptive overlays, not disguised empirical claims.
- Scenario briefs are non-executable.
- Public overlay summaries match public runner outputs.

## [v25.9-public-safe-v5]

### Added
- `docs/release_scope.md`
- `docs/article_relation.md`
- public schemas for provenance, interpretation contracts, and scenario packs.

### Clarified
- Relation between article and repository.
- Public/internal separation.
- Lightweight schemas for public inspection.
