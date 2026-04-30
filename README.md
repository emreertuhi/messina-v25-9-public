# MESSINA

MESSINA is a mechanism-encoding stress-testing framework for exploring how chokepoint crises propagate through tightly coupled systems under structured governance conditions.

This repository is the v25.9 public-safe release. It is a bounded companion to the SSRN working paper and does not release the full historical internal engine.

## Working paper

Ertuhi, Emre. 2026. *MESSINA v25.9: A Mechanism-Encoding Stress-Testing Framework for Chokepoint Crisis Governance*. SSRN Working Paper. Available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6654978

**Keywords:** chokepoint crisis, institutional friction, governance erosion, stress testing, Hormuz, maritime coercion, securitization, normal accidents, agent-based modeling, platform dependency, crisis propagation, tight coupling, governance diagnostics, simulation framework

**JEL Classification:** F51, F52, H56, C63, D02, H12, D81

## Safest one-sentence description

MESSINA is a mechanism-encoding, research-grade scenario-exploration framework whose public outputs should be read as comparative governance diagnostics under encoded assumptions, not as forecasts.

## Current release boundary

The broader internal v25.x architecture is documented as a 72-variable, six-layer, two-dozen-module design lineage. This public repository releases a narrower governance-observer subset: explicit governance formulas, governance profiles and comparison configs, friction-spectrum/policy/theme overlays, public artifacts, a bounded runner, validation tests, and supporting documentation.

The public claims supported by this repository rest on that exposed observer surface. Readers do not need to treat a non-public full engine as a black box in order to inspect the article-facing governance comparison.

## What this repository is not

This repository is not a forecasting engine, production decision tool, full release of the historical internal engine, complete public implementation of all 24 internal module families, or claim of full empirical calibration.

## Start here

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

```
python -m unittest tests.public_validation.test_public_safe_runner -v
```

Run a single public-safe scenario:

```
python run_public.py single --config configs/hormuz_v25_9_baseline.json --out outputs/example_run
```

Run the high-friction versus frictionless comparison:

```
python run_public.py compare --left configs/governance_high_friction.json --right configs/governance_frictionless.json --left-label high_friction --right-label frictionless --out outputs/example_compare
```

## Public evidence surface

The clearest public evidence files are `src/public_safe/observer_formulas.py`, `src/public_safe/scenario_loader.py`, `configs/governance_high_friction.json`, `configs/governance_frictionless.json`, `artifacts/v25.9/governance_comparison.json`, `artifacts/v25.9/governance_summary.md`, and `tests/public_validation/test_public_safe_runner.py`.

## Public metadata

- **Repository:** https://github.com/emreertuhi/messina-v25-9-public
- **Working paper:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6654978
- **DOI:** [10.2139/ssrn.6654978](https://doi.org/10.2139/ssrn.6654978)

Keep draft-management and private planning material outside the public repository.

## Monte Carlo boundary

The broader MESSINA design lineage includes bounded Monte Carlo use, especially the historically important MC512 ensemble size for branch stability, phase consistency, and scenario comparison. In this public repository, MC512 belongs to the methodological lineage and future release target. It is not a public validation claim unless the relevant stochastic runner, seed protocol, sampling assumptions, and ensemble artifacts are released.

## License

MIT License. See `LICENSE`.
