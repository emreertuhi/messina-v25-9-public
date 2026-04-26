# Scenarios
## Public Scenario Logic in MESSINA

MESSINA distinguishes between:
- the **engine**, and
- the **case layer / scenario pack**.

The current public release includes a narrow case surface through:
- public scenario configs for v25.9 governance diagnostics,
- public actor and assumption registries,
- a human-readable case file,
- documentation on scenario-pack dependence.

## Included public configs
- `configs/hormuz_v25_9_baseline.json`
- `configs/governance_high_friction.json`
- `configs/governance_frictionless.json`

These support:
- a baseline single run,
- a same-shock / different-governance comparison.

## Human-readable case file
- `scenarios/hormuz_v25_9_case.md`

This file explains the public case logic in prose so a reader does not have to infer the full comparison design from JSON alone.

## Historical lineage note

Historically, the publication-safe Hormuz case layer was associated with **ODYSSEUS Scenario Pack v1.0**. The current public repository does not re-release that full historical scenario-pack surface. It exposes a narrower v25.9 public case surface derived from the broader lineage.

## Reading rule

A scenario output belongs first to the encoded assumptions of the case layer under study.
That means:
- one scenario pack does not prove a universal law,
- same-shock comparison is an analytic device,
- governance overlays should be interpreted comparatively.

## Cross-theater caution

The broader MESSINA lineage has considered other chokepoints and corridor contexts, including Bab el-Mandeb and wider cross-theater comparison ambitions. Historical comparison language may also invoke Suez as a mechanism-level parallel.

Those references should be handled carefully.

The safest rule is:
- treat the current public case as a Hormuz-centered comparison surface,
- use historical or cross-theater references as mechanism analogies or future comparison targets,
- do **not** treat the current public outputs as directly portable to Bab el-Mandeb, Suez, Panama, Taiwan / SCS, or other theaters with different structures.

## Reuse note

This public repository exposes only a bounded scenario surface. It does not claim to expose every historical scenario family or every internal branch used across older development lines.


## Additional public overlay configs
This release also includes:
- partial-friction spectrum overlays,
- illustrative governance-restoration overlays,
- selected thematic overlays such as stronger allied legal objections, food/fertilizer carve-outs, and buyer-testing emphasis.

These are comparative config extensions built on the public-safe runner. They are not full legal simulators or cross-theater executable packs.

## Non-executable scenario breadth
The `scenarios/briefs/` folder contains non-executable public scenario briefs for:
- Bab el-Mandeb
- Suez (mechanism brief)
- Panama
- Taiwan / South China Sea

These widen scenario readability without claiming that the current runner already executes those theaters.
