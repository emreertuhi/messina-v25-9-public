# Module Registry
## Public Modules, Functional Families, and Internal Architecture Boundary

## Purpose

This file records the mechanism families that can be discussed from the current public release and distinguishes them from the broader internal two-dozen-module architecture.

## Public reproducibility boundary

This registry is an architectural and conceptual map, not a claim that all internal module code is released here.

The public v25.9 repository exposes:

- observer-only governance diagnostics,
- public formulas,
- public configs,
- public comparison artifacts,
- a bounded runner.

The broader internal v25.x design lineage contains two dozen functional module families. Those module families are documented in the working paper as an **architectural inventory**, not as a public reproducibility claim.

## Publicly executable module surface

### 1. Observer-only governance diagnostics

Purpose:

- compute governance-diagnostic signals from public config values without rewriting core peak-stress dynamics.

Public outputs:

- `epistemic_integrity_proxy`
- `decision_friction_proxy`
- `platform_dependency_proxy`
- `mosaic_response_proxy`
- `governance_erosion_score`

Public code:

- `src/public_safe/observer_formulas.py`

## Public functional families documented but not fully executed as internal modules

### 2. Strategic-buyer logic

Purpose:

- represent how major buyers can turn selective coercion into a credibility and burden-sharing problem.

### 3. Shipping / routing / repricing logic

Purpose:

- capture how pressure spreads from maritime disruption into shipping, insurance, and routing channels.

### 4. Propagation and comparison logic

Purpose:

- compare how a similar crisis frame behaves under different governance conditions,
- distinguish visible stress from hidden governability deterioration.

## Internal architecture inventory

The broader internal architecture includes two dozen module families:

1. shipping;
2. finance;
3. diplomacy;
4. humanitarian;
5. food;
6. autonomy;
7. cyber;
8. media;
9. military-political;
10. base-alliance;
11. escalation trap;
12. infrastructure-humanitarian;
13. hegemonic shift;
14. strategic deterrence;
15. command delegation;
16. horizontal escalation;
17. Gulf fragmentation;
18. domestic legitimacy;
19. strategic deterrence dynamics;
20. intelligence coordination;
21. economic cascade;
22. branch point;
23. strategic buyer interdiction;
24. fragmentation.

This list documents mechanism families in the broader architecture. It should not be cited as proof that the public repository executes the full two-dozen-module engine.

## Reading rule

The public repository validates the observer-only governance surface. The two-dozen-module list is architectural documentation and a future public-release target, not the current executable claim surface.
