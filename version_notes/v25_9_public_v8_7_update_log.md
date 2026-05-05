# v25.9 Public-Safe v8.8 Update Log

## Purpose

This log records the public repository updates made to align the repository with the final Working Paper v1.7 claim surface.

## Core changes

- Replaced the working paper Markdown with `docs/MESSINA_Working_Paper_v1_7.md`.
- Removed the stale v1.6 working-paper Markdown file from `docs/`.
- Updated README and CITATION metadata to the v1.7 title: *MESSINA: A Bounded Governance-Diagnostic Surface for Chokepoint Crisis Stress Testing*.
- Updated public framing to emphasize the bounded governance-diagnostic surface rather than a full internal framework release.
- Added support notes for platform-dependency sensitivity, peak-stress saturation testing, and artifact status categories.
- Updated model card, article relation, release scope, validation status, limitations, outputs, coefficient ledger, parameter sources, and version notes to match the v1.7 public/internal boundary.
- Updated policy overlay language to clarify that overlays are modeled governance safeguards, not legal simulations or statutory-effect estimates.
- Updated test-results metadata to `v25.9-public-safe-v8.8` after rerunning public validation tests.

## Added files

- `docs/MESSINA_Working_Paper_v1_7.md`
- `docs/platform_dependency_sensitivity.md`
- `docs/peak_stress_saturation_test_plan.md`
- `docs/artifact_status_table.md`
- `version_notes/v25_9_public_v8_7_update_log.md`

## Removed files

- `docs/MESSINA_Working_Paper_v1_6 (2).md`

## Validation

Command:

```bash
python -m unittest tests.public_validation.test_public_safe_runner -v
```

Result: 3 tests run, 0 failures, 0 errors.

## Non-claims preserved

The update does not turn the public release into:

- a forecasting engine;
- a real-world probability model;
- a full release of the historical internal engine;
- an executable release of all 24 internal module families;
- a legal-effect simulator;
- a completed Decision Sovereignty causal layer.
