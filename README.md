# MESSINA

MESSINA v25.9 is a bounded public governance-diagnostic surface for chokepoint crisis stress testing under explicit institutional-friction assumptions.

This repository is the v25.9 public-safe release. It exposes formulas, configs, overlay artifacts, a bounded public runner, and documentation for the article-facing governance comparison. It does not release the full historical internal engine.

MESSINA v25.9 is treated as a frozen-core snapshot. Future extensions should be designed as independent satellite scenario or module packs rather than retroactive changes to the v25.9 engine. This preserves comparability of the public release while allowing adjacent domains to be tested without reopening the core architecture.

## Working paper

Ertuhi, Emre. 2026. *MESSINA: A Bounded Governance-Diagnostic Surface for Chokepoint Crisis Stress Testing*. SSRN Working Paper. Available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6654978
## Working Paper Figures

The v1.7 working paper includes five embedded public-observer figures: governance-erosion delta decomposition, equalized platform-dependency stress check, core high-friction vs frictionless comparison, five-point friction spectrum, and policy-overlay comparison. These figures visualize the public formulas, profiles, and overlay artifacts only; they do not add empirical calibration, legal-effect estimates, or forecasting claims.


**Keywords:** chokepoint crisis, institutional friction, governance erosion, stress testing, Hormuz, maritime coercion, securitization, normal accidents, agent-based modeling, platform dependency, crisis propagation, tight coupling, governance diagnostics, simulation framework, circulation crisis, rented visibility, braking architecture, decision sovereignty, governance-observer surface, mechanism encoding, maritime domain awareness, crisis governance, observer diagnostics, public reproducibility

**JEL Classification:** F51, F52, H56, C63, D02, H12, D81

## Safest one-sentence description

MESSINA v25.9 is a bounded public observer surface whose outputs should be read as comparative governance diagnostics under explicit assumptions, not as forecasts, empirical measurements, or full internal-engine validation.

## Current release boundary

The broader internal v25.x architecture is documented as a 72-variable, six-layer, two-dozen-module design lineage. That lineage is not the public validation surface. This public repository releases a narrower governance-observer subset: explicit governance formulas, governance profiles and comparison configs, friction-spectrum/policy/theme overlays, public artifacts, a bounded runner, validation tests, and supporting documentation.

The public claims supported by this repository rest on that exposed observer surface. Readers do not need to treat a non-public full engine as a black box in order to inspect the article-facing governance comparison. The repository supports a limited claim: under documented governance profiles, visible stress can remain broadly similar while governance diagnostics differ materially.

## What this repository is not

This repository is not a forecasting engine, production decision tool, full release of the historical internal engine, complete public implementation of all 24 internal module families, empirical calibration claim, causal estimate, or proof that reduced institutional friction produces governance erosion in the external world.

## Start here

1. `docs/MESSINA_Working_Paper_v1_7.md`
2. `docs/model_card.md`
3. `docs/release_scope.md`
4. `docs/article_relation.md`
5. `docs/validation_status.md`
6. `REPRODUCIBILITY.md`
7. `analytics/formula_sheet.md`
8. `analytics/coefficient_ledger.md`
9. `docs/platform_dependency_sensitivity.md`
10. `docs/peak_stress_saturation_test_plan.md`
11. `docs/artifact_status_table.md`
12. `configs/governance_high_friction.json` and `configs/governance_frictionless.json`
13. `artifacts/v25.9/governance_summary.md`

## How to reproduce the public comparison

The public-safe runner uses only the Python standard library.

```bash
python -m unittest tests.public_validation.test_public_safe_runner -v
```

Run a single public-safe scenario:

```bash
python run_public.py single --config configs/hormuz_v25_9_baseline.json --out outputs/example_run
```

Run the high-friction versus frictionless comparison:

```bash
python run_public.py compare --left configs/governance_high_friction.json --right configs/governance_frictionless.json --left-label high_friction --right-label frictionless --out outputs/example_compare
```

## Public evidence surface

The clearest public evidence files are `src/public_safe/observer_formulas.py`, `src/public_safe/scenario_loader.py`, `configs/governance_high_friction.json`, `configs/governance_frictionless.json`, `artifacts/v25.9/governance_comparison.json`, `artifacts/v25.9/governance_summary.md`, and `tests/public_validation/test_public_safe_runner.py`.

## Interpretation rule

The public comparison should be read as an assumption-sensitive observer diagnostic. In the core high-friction versus frictionless comparison, governance erosion rises from 0.561 to 0.693, but that delta is dominated by the platform-dependency assumption: platform dependency is assigned at 0.15 in the high-friction profile and 0.65 in the frictionless profile. Equalizing platform dependency reduces the remaining governance-erosion delta to approximately 0.0075. Readers can challenge that assumption, alter the profile, and rerun the comparison.

Peak-stress values should also be read cautiously. The public governance layer is observer-only and the current calibration may compress peak-stress variation in high-intensity chokepoint cases. The stronger public comparison is the divergence in governance-observer diagnostics rather than a precise claim about peak-stress movement.

## Public metadata

- **Repository:** https://github.com/emreertuhi/messina-v25-9-public
- **Working paper:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6654978
- **DOI:** [10.2139/ssrn.6654978](https://doi.org/10.2139/ssrn.6654978)

Keep draft-management and private planning material outside the public repository.

## Monte Carlo boundary

The broader MESSINA design lineage includes bounded Monte Carlo use, especially the historically important MC512 ensemble size for branch stability, phase consistency, and scenario comparison. In this public repository, MC512 belongs to the methodological lineage and future release target. It is not a public validation claim unless the relevant stochastic runner, seed protocol, sampling assumptions, and ensemble artifacts are released. Stochastic repetition does not convert these outputs into real-world probabilities.

## License

MIT License. See `LICENSE`.
