# Parameter Sources
## Public Source Discipline for the v25.9 Public Release

## Purpose
This file explains what kind of source claim is being made for public parameters, weights, scenario values, and no-code overlay extensions in the current release.

## Core rule
The safest repository-wide statement remains:

> Public proxy labels and config values in this release are explicit design structures for disciplined comparison, not fully externally calibrated empirical measurements.

## Source categories used in this repository

### 1. Design-weighted public diagnostic coefficients
These are explicit formulas used in the public governance-observer runner.
They are:
- visible,
- inspectable,
- reproducible,
- conceptually informed.

They are **not** presented as fully externally calibrated empirical estimates.

Primary files:
- `src/public_safe/observer_formulas.py`
- `analytics/coefficient_ledger.md`
- `analytics/formula_sheet.md`

### 2. Documented public config values
These are values written directly into public scenario configs.
They should be read as:
- encoded assumptions for a documented comparison,
- bounded configuration choices for public release,
- explicit comparison settings rather than universal constants.

Primary files:
- `configs/hormuz_v25_9_baseline.json`
- `configs/governance_high_friction.json`
- `configs/governance_frictionless.json`

### 3. Interpolated friction-spectrum overlays
The partial-friction spectrum overlays are derived by bounded interpolation between the documented high-friction baseline and frictionless counterfactual across the public governance-observer variables.

Included files:
- `configs/governance_mildly_reduced_friction.json`
- `configs/governance_moderately_reduced_friction.json`
- `configs/governance_severely_reduced_friction.json`

These overlays should be read as:
- illustrative spectrum points,
- aids for showing that friction is better treated as a gradient than as a binary switch,
not as empirically estimated regime states.

### 4. Policy-facing governance overlays
The policy overlays in this release are explicit illustrative counterfactuals built **without new code** on top of the documented public governance-observer surface.

Included files:
- `configs/policy_12h_notification.json`
- `configs/policy_structured_dissent.json`
- `configs/policy_automatic_sunset.json`
- `configs/policy_minimum_brake_package.json`
- `configs/theme_allied_legal_objections.json`
- `configs/theme_food_fertilizer_carveout.json`
- `configs/theme_buyer_testing_emphasis.json`

These files should be read as:
- governance-condition overlays,
- structured interpretive experiments,
- policy-facing comparison aids,
not as direct legal simulation or statutory modeling.

### 5. Public artifact values
These are output values shown in public artifacts such as:
- `artifacts/v25.9/governance_signals.json`
- `artifacts/v25.9/single_run.json`
- `artifacts/v25.9/governance_comparison.json`
- `artifacts/v25.9/governance_summary.md`
- `artifacts/overlay_suite/*.json`
- `artifacts/overlay_suite/*.md`

These values support current-build public claims about the documented v25.9 comparison surface.

### 6. Historical design memory
Some terms, mechanisms, and influences discussed elsewhere in the broader MESSINA lineage are real parts of the design memory but are not fully disclosed here as stable public numeric source lines.

## Interpretive caution
The public release makes four distinct kinds of source claim:
- **formula transparency** for public proxy construction,
- **config transparency** for documented scenario values,
- **artifact transparency** for bounded rerun outputs,
- **lineage transparency** about what remains outside the public package.

What it does **not** claim is:
- full external calibration,
- strong historical parameter fitting,
- rare-event probability estimation,
- that every governance quantity is anchored to a direct external dataset.
