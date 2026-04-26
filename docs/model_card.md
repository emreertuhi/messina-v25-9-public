# Model Card
## MESSINA v25.9 Public-Safe Release

## Model type

MESSINA is a non-predictive, mechanism-encoding scenario-exploration framework. This public release exposes a bounded governance-observer runner and comparison surface.

## Primary use

This public release is meant for:

- reading the conceptual and methodological logic of the framework,
- inspecting governance-observer formulas,
- reproducing the public v25.9 comparison surface,
- understanding how similar visible stress can coexist with different governability conditions.

## Non-goals

This public release is not:

- a forecasting engine,
- a production decision system,
- a full release of the historical internal engine,
- a complete executable release of all 24 internal module families,
- a claim of full empirical calibration,
- a complete governance-causation architecture.

## Current evidence surface

The strongest public evidence files are:

- `src/public_safe/observer_formulas.py`
- `src/public_safe/scenario_loader.py`
- `configs/governance_high_friction.json`
- `configs/governance_frictionless.json`
- `artifacts/v25.9/governance_comparison.json`
- `artifacts/v25.9/governance_summary.md`
- `artifacts/v25.9/test_results.json`
- `tests/public_validation/test_public_safe_runner.py`

## Current claims

The public release supports these narrow claims:

- visible stress and governability can diverge under the same broad chokepoint crisis frame,
- reduced-friction conditions can worsen governance diagnostics while leaving peak stress broadly similar,
- public formulas and comparison artifacts are explicit and inspectable,
- the public runner reproduces the documented v25.9 governance-observer surface.

## Current limits

The public release does not justify:

- real-world event prediction,
- strong real-world probability claims,
- claims that proxy values are direct empirical measurements,
- claims that all internal module families are publicly executable,
- claims that the current public build contains a full fractal-analytics layer,
- claims that the current public build contains a full Decision Sovereignty Layer.

## Monte Carlo note

The broader methodology lineage includes bounded Monte Carlo use, especially MC512 for branch stability and phase consistency. In this public release, MC512 belongs to the methodological lineage and future-release target, not to a claim of rare-event precision or real-world probability estimation.

## Recommended reading order

1. `README.md`
2. `docs/MESSINA_Working_Paper_v1_4.md`
3. `docs/release_scope.md`
4. `docs/article_relation.md`
5. `docs/validation_status.md`
6. `REPRODUCIBILITY.md`
