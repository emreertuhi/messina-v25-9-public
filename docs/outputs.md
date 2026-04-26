# Outputs
## How to Read Public Outputs in MESSINA

## Core reading rule

Public outputs in this release should be read as:
- comparative stress diagnostics,
- governance-diagnostic proxies,
- scenario-conditioned structured signals,
- bounded evidence for current-release claims.

They should not be read as:
- real-world event probabilities,
- direct measurements of political reality,
- proof of full empirical calibration,
- proof of a complete causal governance engine.

## Main output families

### 1. Baseline single-run outputs
- `artifacts/v25.9/governance_signals.json`
- `artifacts/v25.9/single_run.json`
- `artifacts/v25.9/full_run_report.md`

These establish the documented baseline governance-observer surface.

### 2. Same-shock / different-governance comparison outputs
- `artifacts/v25.9/governance_comparison.json`
- `artifacts/v25.9/governance_summary.md`

These support the narrow public comparison claim that reduced-friction conditions worsen governance diagnostics while leaving peak stress broadly similar.

### 3. Validation outputs
- `artifacts/v25.9/test_results.json`
- `tests/public_validation/test_public_safe_runner.py`

These show that the bounded public runner reproduces the documented public surface.

### 4. Registry and formula files
- `analytics/variable_registry.md`
- `analytics/coefficient_ledger.md`
- `analytics/formula_sheet.md`
- `analytics/parameter_sources.md`

These explain what the public variables, weights, and source categories are supposed to mean.

## Weight disclaimer

Governance proxy weights in the public runner are design choices, not empirical estimates.


### 5. Overlay-suite outputs
- `artifacts/overlay_suite/friction_spectrum_summary.json`
- `artifacts/overlay_suite/friction_spectrum_summary.md`
- `artifacts/overlay_suite/policy_overlay_summary.json`
- `artifacts/overlay_suite/policy_overlay_summary.md`
- `artifacts/overlay_suite/theme_overlay_summary.json`
- `artifacts/overlay_suite/theme_overlay_summary.md`

These extend the bounded comparison surface without changing the public-safe code path.
