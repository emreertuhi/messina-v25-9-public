# Platform Dependency Sensitivity Note
## Public v25.9 Diagnostic Surface

## Purpose

This note records a small sensitivity check for the public governance-erosion diagnostic. It is not a new model run and should not be read as empirical calibration. It shows how much of the documented governance-erosion delta depends on the width of the platform-dependency spread assigned in the public governance profiles.

## Formula context

The public governance-erosion score is:

```python
governance_erosion_score = (
    0.30 * (1.0 - epistemic_integrity_proxy) +
    0.25 * (1.0 - decision_friction_proxy) +
    0.25 * platform_dependency_proxy +
    0.20 * mosaic_response_proxy
)
```

Platform dependency is read directly from the public governance profile. It is profile-assigned rather than dynamically discovered by the public runner.

## Core public comparison

| Scenario | Platform dependency | Governance erosion |
|---|---:|---:|
| High friction | 0.15 | 0.560795 |
| Frictionless | 0.65 | 0.693299 |
| Delta | +0.50 | +0.132504 |

The platform-dependency term contributes `0.50 * 0.25 = 0.125000`, or approximately 94% of the total governance-erosion delta.

## Equalized platform-dependency stress check

If platform dependency is equalized across the two profiles, the platform-dependency contribution to the delta disappears. The remaining governance-erosion delta is approximately `0.007504`.

This does not invalidate the comparison. It narrows the interpretation: the public v25.9 governance-erosion divergence depends heavily on the platform-dependency profile assumption.

## Compressed-spread illustration

If the platform-dependency spread is compressed from `0.15 -> 0.65` to `0.25 -> 0.45`, while holding the other public component deltas constant, the estimated governance-erosion delta falls from approximately `0.132504` to approximately `0.057504`.

| Scenario | Platform dependency | Governance erosion estimate |
|---|---:|---:|
| Original high friction | 0.15 | 0.560795 |
| Original frictionless | 0.65 | 0.693299 |
| Original delta | +0.50 | +0.132504 |
| Compressed high friction | 0.25 | 0.585795 |
| Compressed frictionless | 0.45 | 0.643299 |
| Compressed delta | +0.20 | +0.057504 |

This compressed-spread illustration leaves a visible but more moderate governance-erosion divergence. It should be read as a sensitivity check, not as a replacement scenario.

## Minimum brake package under simple compression

The public policy overlay summary reports a minimum brake package governance-erosion value of approximately `0.651485`, with platform dependency assigned at `0.52`. Under a simple linear compression from the original platform-dependency range `[0.15, 0.65]` to `[0.25, 0.45]`, the platform value `0.52` maps to approximately `0.398`.

Using only the platform-dependency term adjustment, the minimum brake package estimate becomes approximately `0.620985`, compared with a compressed frictionless estimate of approximately `0.643299`. The benefit remains visible, but falls from about `-0.041814` to about `-0.022314`.

| Comparison | Governance erosion difference |
|---|---:|
| Original minimum-brake benefit vs frictionless | -0.041814 |
| Compressed-spread estimate | -0.022314 |

## Interpretation rule

The sensitivity check supports a narrower reading: platform dependency remains important under compressed assumptions, but effect size depends on the assigned spread. The public contribution is that the assumption is exposed and rerunnable, not that the current profile values are empirically final.
