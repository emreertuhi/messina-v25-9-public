# Peak-Stress Dynamic-Range and Saturation Test Plan
## Public v25.9 Validation Roadmap Item

## Purpose

The public v25.9 comparison shows near-identical peak-stress values across governance overlays while governance diagnostics diverge. This test plan records how a later public release should examine whether that flatness reflects substantive stress similarity, observer-boundary design, or calibration-driven compression.

This file is a validation-roadmap artifact. It does not claim that the test has already been run.

## Current interpretation

In the current public release, governance diagnostics are observer-only. They do not rewrite core stress dynamics. This design choice makes peak-stress flatness expected under the public comparison surface and prevents overclaiming that governance overlays dynamically dampen or intensify the physical crisis frame.

The working paper therefore reads near-identical peak-stress values cautiously and treats governance-observer divergence as the more informative public comparison.

## Proposed test design

A later public release should run the same public governance profiles while varying peak-stress mapping and saturation conditions. The test should include at least:

1. the high-friction baseline;
2. the frictionless counterfactual;
3. the minimum brake package;
4. the friction-spectrum overlays;
5. selected theme overlays.

The following parameters or equivalent mapping choices should be varied where the public runner exposes them:

- threshold values;
- clamp behavior;
- peak-stress mapping function;
- dynamic range width;
- saturation or ceiling behavior;
- any public stress-composite weighting that affects peak values.

## Required outputs

The test should report:

- peak-stress delta under each setting;
- spread/range across governance profiles;
- whether profile ranking changes;
- whether governance overlays still show compressed peak-stress variation;
- whether governance-observer diagnostics remain directionally stable.

## Safe conclusion language

If peak-stress variation remains compressed under widened dynamic range, the public release can more confidently describe flat peak stress as a stable feature of the current comparison surface.

If peak-stress variation increases under widened dynamic range, the current v25.9 interpretation should remain narrower:

> In the bounded v25.9 public observer release, peak-stress variation remains compressed; future dynamic-range tests should examine whether this flatness reflects substantive stress similarity, observer-boundary design, or saturation-prone calibration.

## Non-claim

This test plan does not turn MESSINA into a forecasting model, a calibrated physical crisis simulator, or a real-world probability engine. It is a robustness check for the public diagnostic surface.
