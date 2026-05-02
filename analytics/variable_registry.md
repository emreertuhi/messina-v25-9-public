# Variable Registry
## Current Public Variables and Proxies in MESSINA

Unless otherwise stated, the quantities in this file should be read as normalized comparative variables rather than direct measurements.

## Core public outputs

| Variable name | Type | Meaning | Public example value(s) |
|---|---|---|---|
| `peak_stress` | Internal normalized index | Visible crisis stress at the system level | `0.7978167899148008` baseline; `0.7999721678974817` frictionless comparison |
| `epistemic_integrity_proxy` | Comparative proxy | Comparative indicator of informational integrity under crisis pressure | `0.2530525370312938` baseline; `0.25197814535826113` frictionless comparison |
| `decision_friction_proxy` | Comparative proxy | Comparative indicator of institutional and procedural braking | `0.4751743814347482` high-friction; `0.4464707461464616` frictionless |
| `platform_dependency_proxy` | Profile-assigned comparative proxy | Comparative indicator of reliance on commercial or technical infrastructures outside direct public control; read directly from the governance profile | `0.0` baseline; `0.15` high-friction; `0.65` frictionless |
| `mosaic_response_proxy` | Comparative proxy | Comparative indicator of distributed and uneven response structure | `0.8400201657921639` baseline; `0.840049602722785` frictionless |
| `governance_erosion_score` | Comparative composite proxy | Comparative indicator of hidden deterioration in governability | `0.5232946766903576` baseline; `0.5607946766903575` high-friction; `0.6932987904004633` frictionless |

## Output bundles
- `governance_signals`
- `single_run`
- `comparison`

## Formula inputs currently exposed in the public runner
- `intelligence_reliability_gap`
- `info_distortion`
- `intelligence_contamination`
- `negotiation_credibility`
- `congressional_constraint`
- `legal_cohesion`
- `religious_moral_constraint`
- `delegated_command_depth`
- `local_unit_autonomy`
- `strategic_control_gap`
- `ceasefire_lag`
- `governance_profile["platform_dependency"]`

## Reading rule
These variables are public diagnostic quantities for comparative interpretation. They should not be treated as direct measurements of real-world institutional truth.

## Platform-dependency note

`platform_dependency_proxy` is assigned directly in public governance profiles. It should not be described as dynamically discovered by the public runner.
