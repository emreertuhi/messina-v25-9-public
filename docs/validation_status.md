# Validation Status
## What the Current Public Release Validates — and What It Does Not

## Purpose

This file states the validation status of the v25.9 public-safe release in plain language.

## Current public validation surface

The public package validates that:

- the bounded public-safe runner executes successfully,
- required scenario keys are checked before execution,
- public config values used by the observer formulas are numeric and bounded where expected,
- the documented public formulas reproduce published governance-observer outputs,
- same-frame / different-governance comparison files can be rerun from included configs,
- included unit tests pass under the public runner.

## Public evidence files

The clearest public validation anchors are:

- `tests/public_validation/test_public_safe_runner.py`
- `artifacts/v25.9/test_results.json`
- `REPRODUCIBILITY.md`
- `src/public_safe/scenario_loader.py`
- `src/public_safe/observer_formulas.py`
- `schemas/provenance.schema.json`
- `schemas/interpretation_contract.schema.json`

## What the public release does not validate

The current public package does **not** validate:

- full external empirical calibration,
- full historical-engine replay,
- rare-event probability estimation,
- a complete causal governance layer,
- public execution of all 24 internal module families,
- a first-class public fractal-diagnostics stack,
- live early warning from real-time data feeds.

## Monte Carlo boundary

MC512 belongs to the broader internal development lineage. It is not a public validation claim for this repository unless the relevant stochastic runner, seed protocol, sampling assumptions, and ensemble artifacts are released. The public v25.9 repository should therefore not be described as a rare-event probability engine.

## Historical lineage note

The broader v25.x lineage included richer internal validation and audit artifacts, including threshold stability checks, sensitivity rankings, replay checks, and same-horizon pack comparisons. Those artifacts inform the development history, but they are not re-presented here as if they were freshly reproduced by the bounded public runner.

## Safe reading rule

Use this release as a validated public comparison surface for bounded governance diagnostics. Do not treat it as a fully externally calibrated forecasting or command system.
