# MESSINA

MESSINA is a non-predictive, mechanism-encoding stress-testing framework for examining how maritime chokepoint shocks propagate through tightly coupled systems under explicit assumptions.

This repository is the **v25.9 public-safe release**. It is designed as a bounded, publication-safe companion to the working paper, not as a full release of the historical internal engine.

## Safest one-sentence description

> MESSINA is a mechanism-encoding, research-grade scenario-exploration framework whose public outputs should be read as comparative governance diagnostics under encoded assumptions, not as forecasts.

## Current release boundary

The broader internal v25.x architecture is documented as a 72-variable, six-layer, two-dozen-module design lineage. This public repository releases a narrower governance-observer subset:

- explicit governance formulas,
- governance profiles and comparison configs,
- friction-spectrum, policy, and theme overlays,
- public artifacts from the documented comparison surface,
- a bounded runner that reproduces governance-observer outputs,
- tests for the public runner,
- theory, methodology, validation, and release-boundary documentation.

The public claims supported by this repository rest on that exposed observer surface. Readers do **not** need to treat a non-public full engine as a black box in order to inspect the article-facing governance comparison.

## What this repository is

This repository is a bounded public release for:

- conceptual orientation,
- methodology inspection,
- reproducible public governance-observer comparisons,
- scrutiny of documented formulas and configs,
- understanding how visible stress and governability can diverge under similar chokepoint crisis frames.

## What this repository is not

This repository is not:

- a forecasting engine,
- a production decision tool,
- a release of the full historical internal engine,
- a complete public implementation of all 24 internal module families,
- a claim of full empirical calibration,
- a claim that the current public build contains a causal Decision Sovereignty Layer,
- a public fractal-diagnostics stack,
- a proof that one Hormuz-centered scenario generalizes mechanically across all chokepoints.

## Start here

If you arrived here after reading the working paper, use this order:

1. `docs/MESSINA_Working_Paper_v1_4.md`
2. `docs/model_card.md`
3. `docs/release_scope.md`
4. `docs/article_relation.md`
5. `docs/validation_status.md`
6. `REPRODUCIBILITY.md`
7. `analytics/formula_sheet.md`
8. `configs/governance_high_friction.json` and `configs/governance_frictionless.json`
9. `artifacts/v25.9/governance_summary.md`

## How to reproduce the public comparison

The public-safe runner uses only the Python standard library.

```bash
python -m unittest tests.public_validation.test_public_safe_runner -v
```

Run a single public-safe scenario:

```bash
python run_public.py single \
  --config configs/hormuz_v25_9_baseline.json \
  --out outputs/example_run
```

Run the high-friction versus frictionless comparison:

```bash
python run_public.py compare \
  --left configs/governance_high_friction.json \
  --right configs/governance_frictionless.json \
  --left-label high_friction \
  --right-label frictionless \
  --out outputs/example_compare
```

## Public evidence surface

The clearest public evidence files are:

- `src/public_safe/observer_formulas.py`
- `src/public_safe/scenario_loader.py`
- `configs/governance_high_friction.json`
- `configs/governance_frictionless.json`
- `artifacts/v25.9/governance_comparison.json`
- `artifacts/v25.9/governance_summary.md`
- `artifacts/overlay_suite/friction_spectrum_summary.md`
- `artifacts/overlay_suite/policy_overlay_summary.md`
- `artifacts/overlay_suite/theme_overlay_summary.md`
- `tests/public_validation/test_public_safe_runner.py`

## Public metadata updates

The repository URL is set as `https://github.com/emreertuhi/messina-v25-9-public`. After an SSRN page or DOI is created, add that citation to `README.md`, `CITATION.cff`, and `docs/MESSINA_Working_Paper_v1_4.md`. Keep draft-management and private planning material outside the public repository.

## Repository map

- `docs/` working paper, conceptual framing, methodology, limits, release scope, article relation, and validation status
- `analytics/` public variables, coefficients, formulas, and parameter-source discipline
- `modules/` public module overview and internal module-inventory boundary
- `scenarios/` actor registry, assumption ledger, case file, and non-executable scenario briefs
- `configs/` public scenario configurations used by the runner
- `artifacts/v25.9/` public outputs and comparison artifacts
- `artifacts/overlay_suite/` friction-spectrum, policy-overlay, and theme-overlay outputs
- `src/public_safe/` bounded public runner and formulas
- `tests/public_validation/` validation tests for the public runner
- `version_notes/` release and migration notes
- `templates/` reusable scenario and output skeletons
- `data/` public parameter table used in the current public surface
- `schemas/` lightweight public validation and interpretation schemas

## Monte Carlo boundary

The broader MESSINA design lineage includes bounded Monte Carlo use, especially the historically important MC512 ensemble size for branch stability, phase consistency, and scenario comparison. In this public repository, MC512 belongs to the methodological lineage and future release target. It is not a public validation claim unless the relevant stochastic runner, seed protocol, sampling assumptions, and ensemble artifacts are released.

## License

MIT License. See `LICENSE`.
