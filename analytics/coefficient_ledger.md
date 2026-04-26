# Coefficient Ledger
## Public Governance-Observer Weights in MESSINA v25.9

These coefficients should be read as explicit design weights for comparative public diagnostics. They are not presented here as strong empirical estimates.

## Core interpretive rule

> Governance proxy weights in the public release are explicit and inspectable design weights. They are not strong external calibrations of geopolitical reality.

## Epistemic integrity proxy

```python
epistemic_integrity_proxy = 1.0 - (
    0.35 * intelligence_reliability_gap +
    0.30 * info_distortion +
    0.20 * intelligence_contamination +
    0.15 * (1.0 - negotiation_credibility)
)
```

## Decision friction proxy

```python
decision_friction_proxy = (
    0.40 * congressional_constraint +
    0.30 * negotiation_credibility +
    0.20 * legal_cohesion +
    0.10 * religious_moral_constraint
)
```

## Mosaic response proxy

```python
mosaic_response_proxy = (
    0.35 * delegated_command_depth +
    0.25 * local_unit_autonomy +
    0.20 * strategic_control_gap +
    0.20 * ceasefire_lag
)
```

## Governance erosion score

```python
governance_erosion_score = (
    0.30 * (1.0 - epistemic_integrity_proxy) +
    0.25 * (1.0 - decision_friction_proxy) +
    0.25 * platform_dependency_proxy +
    0.20 * mosaic_response_proxy
)
```

## What this file does and does not claim

This file supports the claim that the public v25.9 governance diagnostics are explicit and inspectable.
It does **not** claim that these weights are historically calibrated empirical constants.
