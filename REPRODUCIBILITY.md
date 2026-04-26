# Reproducibility
## Public-Safe Runner for MESSINA v25.9

## What this reproduces

This public-safe runner reproduces the **documented v25.9 governance-observer surface**, not the full historical internal engine.

It reproduces:

- single-run governance signals,
- public governance-observer formulas,
- same-frame / different-governance comparison outputs,
- public run reports and comparison summaries,
- bounded comparison claims documented in this repository.

It does **not** reproduce:

- the full historical internal codebase,
- all 24 internal module families,
- complete multi-version architecture history,
- live-data or classified-data pipelines,
- a fully integrated Decision Sovereignty Layer,
- a formal fractal-diagnostics stack,
- MC512 ensemble claims from the broader internal lineage.

## Requirements

The public-safe runner uses only the Python standard library. The requirements file is intentionally minimal.

```bash
pip install -r requirements.txt
```

## Validate the public release

```bash
python -m unittest tests.public_validation.test_public_safe_runner -v
```

Expected result:

```text
Ran 3 tests ... OK
```

## Single-run example

```bash
python run_public.py single \
  --config configs/hormuz_v25_9_baseline.json \
  --out outputs/example_run
```

This writes:

- `outputs/example_run/governance_signals.json`
- `outputs/example_run/single_run.json`
- `outputs/example_run/full_run_report.md`

## Comparison example

```bash
python run_public.py compare \
  --left configs/governance_high_friction.json \
  --right configs/governance_frictionless.json \
  --left-label high_friction \
  --right-label frictionless \
  --out outputs/example_compare
```

This writes:

- `outputs/example_compare/comparison.json`
- `outputs/example_compare/summary.md`

## Hygiene check before release

```bash
find . -name '__pycache__' -o -name '*.pyc'
```

The command should return nothing in the release zip.

## Reading rule

Successful reproduction of this runner supports narrow public-build claims: the public formulas are inspectable, the public artifacts can be regenerated, and the documented v25.9 governance-observer surface is reproducible. It does not justify forecasting claims, external-probability claims, or claims about undisclosed internal engine behavior.
