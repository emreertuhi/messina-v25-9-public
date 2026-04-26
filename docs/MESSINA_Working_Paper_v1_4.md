# MESSINA v25.9:
# A Mechanism-Encoding Stress-Testing Framework
# for Chokepoint Crisis Governance

**Working Paper v1.4 - Not Peer Reviewed**  
**Emre Ertuhi**  
**April 2026**  
**Code and data:** https://github.com/emreertuhi/messina-v25-9-public

## Abstract

MESSINA is a non-predictive, mechanism-encoding stress-testing framework for exploring how chokepoint crises propagate through tightly coupled systems under explicit assumptions. It does not forecast real-world events, assign reliable real-world probabilities, or claim to replace historical judgment. Instead, it compares how crisis pathways, visible stress, control quality, and hidden institutional deterioration behave across structured governance conditions.

This working paper documents the theoretical foundations, methodological architecture, citation base, public-release boundary, and bounded demonstration surface of the v25.9 release, centered on a Hormuz chokepoint crisis frame. The broader internal v25.x architecture tracks 72 core variables across six layers using a mixed-resolution, agent-based architecture, a phase-regime system, dispersion-aware processing, and two dozen functional modules. The public v25.9 repository releases a narrower observer-only comparison surface: public formulas, governance overlays, scenario configs, reproducibility artifacts, and a bounded runner that reproduces documented governance-observer outputs. The public claims in this paper rest on that exposed observer surface, not on requiring readers to trust a non-public full engine.

The core finding is not that reduced institutional friction necessarily makes the opening shock larger. In the public v25.9 comparison, peak stress barely moves across friction conditions. What changes is governability: governance erosion rises, decision friction falls, platform dependency increases, and mosaic response remains elevated. The same broad chokepoint shock can therefore look similar at first contact while becoming harder to govern afterward. This paper accompanies a public code repository and a separately submitted policy article, "The Strait Is Not the Crisis." Version 1.4 adds a stricter public/internal reproducibility boundary, an operationalization bridge from theory to variables, a public worked example for the governance diagnostic, and explicit limitations on non-public module-engine claims and design-prior confirmation risk.

**Keywords:** chokepoint crisis, institutional friction, governance erosion, stress testing, Hormuz, circulation crisis, maritime coercion, securitization, normal accidents, agent-based modeling, platform dependency, aggregation

**JEL Classification:** F51, F52, H56

## AI Disclosure Statement

AI-assisted tools were used for editorial support, language refinement, structural review, and consistency checks. The stress-testing framework (MESSINA), its theoretical design, methodology, governance formulas, scenario configurations, and all analytical conclusions are the author's original work. The author retained full responsibility for the research design, analysis, source selection, and final text.

**Architecture and reproducibility boundary note:** The 72-variable, six-layer, two-dozen-module architecture refers to the broader internal v25.x design lineage. The public v25.9 release exposes a narrower governance-observer subset: comparison configs, explicit formulas, overlay artifacts, documentation, and a bounded runner. The article-facing and working-paper claims that depend on public reproducibility rest on this exposed observer surface, not on requiring readers to treat the non-public full engine as a black box.

## 1. Introduction

MESSINA studies a simple but easily missed problem: in a tightly coupled crisis system, the opening shock and the crisis that follows are not the same object.

A maritime chokepoint shock may begin with a threat, a strike, an interdiction, a shipping warning, or a legal notice. But the wider crisis moves through other systems: insurance, routing, fertilizer cargoes, food inputs, payment channels, alliance politics, domestic authorization, and the practical ability of a state to keep track of what it has set in motion. The initial act may be visible and bounded. The propagated crisis may be lateral, delayed, and harder to control.

This paper documents MESSINA v25.9, a mechanism-encoding framework designed to compare such crisis worlds under explicit assumptions. It accompanies a public repository and a policy article. The policy article is written for a general foreign-policy audience. This working paper is narrower and more technical. It explains what the model is, what the public release actually exposes, what it does not expose, and how its results should be read.

The central claim is that institutional friction can be a strategic variable rather than mere procedural drag. Legal review, congressional scrutiny, allied consultation, professional military objection, and internal dissent do not guarantee prudence. They can delay necessary action. But they also force contradiction into the decision cycle before tactical motion hardens into strategic drift. In a chokepoint crisis, that friction can help preserve control over second-order effects.

The public v25.9 release supports a narrow governance argument. It compares a common Hormuz crisis frame under higher-friction and reduced-friction governance conditions. The comparison shows that visible stress can remain broadly similar while governance diagnostics deteriorate materially. In plain terms: a state can still strike first and strike hard while losing its ability to govern what follows.

## 1.1 Contribution

MESSINA's contribution is not a forecast. It is a structured comparison surface. It helps separate four things that are often collapsed in policy debate:

1. the opening shock;
2. the propagated crisis;
3. visible system stress;
4. the actor's governability after the first move.

This distinction matters because public debate often concentrates on first-contact intensity: whether a strait closes, whether oil prices rise, whether a force package can strike, or whether shipping can be escorted. Those are important questions. MESSINA asks a different question: once the shock enters a coupled system, what happens to the mechanisms that control the aftermath?

The v25.9 release therefore uses governance diagnostics as observer-only signals. These diagnostics do not rewrite core stress dynamics. They annotate the comparison surface and make visible a pattern that ordinary peak-stress metrics may hide.

## 1.2 Public and Internal Boundary

The public repository should be read carefully. It is not a full release of the historical internal engine. It is a bounded, publication-safe release of the v25.9 public comparison surface behind the policy article's core governance argument. The public repository is available at the URL listed in the header.

That means the public repository includes public theory notes, methodology notes, formulas, configs, overlay comparisons, artifacts, and a bounded runner that reproduces documented governance-observer outputs. It does not include every internal design memo, historical engine branch, full multi-theater scenario family, future causal governance layer, or the complete two-dozen-module dynamic engine.

This is the central reproducibility boundary. The public release does not ask readers to accept non-public module outputs as independently validated. It asks a narrower question: if the governance-observer formulas, profiles, and overlays are made explicit, do the documented comparisons support the article-facing claim that visible stress and governability can diverge?

This boundary is deliberate. It prevents the public release from making claims that outrun what can be inspected and rerun. It also keeps the policy article and the repository aligned: the article is broader in prose, chronology, and policy interpretation; the repository exposes the bounded comparison surface behind the article's central argument.

The safe reading rule is therefore:

**The public repository supports the claim that, under documented v25.9 governance overlays, visible stress can remain broadly similar while governance diagnostics worsen under reduced-friction conditions. It does not prove every policy sentence in the article and should not be treated as a complete release of the historical internal engine.**


## 1.3 Source and Citation Boundary

Version 1.2 adds a formal reference base. The sources serve three different functions and should not be collapsed.

First, theory references anchor the conceptual vocabulary: securitization, normal accidents, coercive diplomacy, loss sensitivity, sunk-cost escalation, complex interdependence, organizational decision-making, hegemonic change, agent-based modeling, sensitivity analysis, and simulation validation.

Second, empirical and institutional sources anchor the external context: maritime chokepoints, Hormuz oil and LNG exposure, freight and rerouting dynamics, fertilizer and food-input vulnerability, war-risk insurance listing logic, the Suez historical parallel, and U.S. war-powers procedure.

Third, repository provenance anchors the internal MESSINA claim surface: formulas, configs, overlays, validation artifacts, and public/internal boundaries.

The references do not convert MESSINA into a calibrated forecasting model. They show where the framework's concepts come from, which empirical background assumptions are externally grounded, and which claims remain internal design choices.

## 2. Theoretical Framework

## 2.1 Central Claim and Propositions

MESSINA's central claim is that, in tightly coupled systems, the decisive variable is often not the size of the opening shock but the durability of the mechanisms that govern what follows.

That claim rests on five linked propositions.

First, an opening shock and the propagated crisis it produces are different objects. A strike, warning, or interdiction may be local; its consequences may move laterally across commercial, financial, legal, and political systems.

Second, visible stress and control quality can diverge. A crisis may not look dramatically worse on a peak-stress metric while still becoming less governable.

Third, institutional friction can function as braking architecture. It is not automatically wise or sufficient, but it can preserve time, contradiction, review, and accountability inside the decision cycle.

Fourth, chokepoint crises spread laterally as well as vertically. The escalation-ladder metaphor captures some conflict dynamics, but it underplays network propagation through shipping, insurance, routing, food inputs, finance, and allied consent.

Fifth, governance conditions are structural variables. They are not decorative background. A crisis behaves differently when oversight is compressed, legal review is rushed, dissent is punished, allied objections are bypassed, or public authority depends on private monitoring systems it does not control.

## 2.2 Circulation Crisis

A circulation crisis is a crisis in which a local shock spreads through the mechanisms that keep trade, pricing, supply, coordination, and political confidence functioning. It is not simply an escalation crisis.

An escalation ladder implies primarily vertical movement: one rung higher, one rung lower, retaliation, counter-retaliation. A circulation crisis includes vertical escalation but adds lateral spread. The shock moves through ship availability, insurance premia, port calls, cargo timing, fertilizer and food input availability, sovereign-risk perceptions, alliance consultations, and the practical credibility of enforcement.

Hormuz is a useful case frame because a local maritime shock can become a circulation problem quickly. Oil matters, but the crisis does not stop at oil. Fertilizer cargoes, war-risk insurance, shipping schedules, Asian buyer behavior, Gulf basing politics, and neutral-flag enforcement all matter. Official energy reporting treats Hormuz as a critical oil and LNG chokepoint, UNCTAD documents the wider cost and food-security effects of chokepoint pressure, and FAO/USDA/World Bank materials support the link between fertilizer disruption, input costs, and food-security stress (EIA 2026; IEA 2026; UNCTAD 2024; FAO 2022; USDA FAS 2022; World Bank 2026). A state may have the military capacity to act at the chokepoint while lacking the institutional capacity to keep the consequences bounded.

## 2.3 Primary Theory Anchors

The public theory line is deliberately narrow and hierarchical. MESSINA does not claim that every theory explains everything. Different theories perform different jobs inside the architecture.

### Securitization Theory

Securitization Theory is the primary political anchor. It explains how disputes become emergency-coded problems, how normal review can be compressed, and how dissent can be delegitimized once an issue is framed as existential (Wæver 1995; Buzan, Wæver, and de Wilde 1998). In MESSINA, this supports the treatment of institutional friction, legal review, legitimacy strain, political hardening, and reduced room for contradiction as central variables rather than decorative background.

### Normal Accident Theory

Normal Accident Theory is the primary systems anchor. It explains why tightly coupled, interactively complex systems can propagate disruption in nonlinear ways (Perrow 1999). In MESSINA, this supports the circulation-crisis logic: local shocks do not remain local when shipping, insurance, routing, food inputs, finance, law, and alliance politics are coupled.

### Coercive Logic and Damage-Control Separation

A Pape-informed coercive logic contributes a narrower but important proposition: damage does not equal control (Schelling 1966; George and Simons 1994; Pape 1996). Tactical destruction may alter capabilities, but it does not automatically produce political compliance. This matters for selective interdiction, coercive signaling, regime rally effects, buyer testing, and the gap between operational action and strategic governability.

Together, these anchors support the framework's central split between the capacity to act and the capacity to govern the consequences of action.

## 2.4 Wider Design Influences

MESSINA also incorporates mechanisms from wider literatures as design influences. These influences are not presented as independently validated submodels in the public release. They shape mechanism encoding and interpretation.

Organizational delay, including Badewanne-style lag, informs the idea that institutions do not update instantly after central decisions. The term is used here as an internal modeling shorthand for lagged organizational response rather than as a separately validated public metric; the broader mechanism is anchored in organizational decision-making and bureaucratic-politics literatures (March and Simon 1958; Cyert and March 1963; Allison and Zelikow 1999). This supports ceasefire lag, delegated command depth, local unit autonomy, and slow institutional response.

Prospect-style loss sensitivity informs escalation under perceived loss, prestige pressure, and credibility threat (Kahneman and Tversky 1979). Actors facing loss may accept risks they would reject under neutral expected-utility logic.

Rally-round-the-flag dynamics explain why external pressure can harden rather than weaken a target system (Mueller 1973). This supports regime rally effects and opposition suppression under external threat.

Sunk-cost escalation explains why prior visible costs make reversal politically harder (Staw 1976; Arkes and Blumer 1985). This supports lock-in, branch irreversibility, and escalation traps.

Complex interdependence supports the circulation-crisis logic by linking shipping, insurance, routing, food inputs, finance, alliances, credibility, and platform dependencies (Keohane and Nye 2012).

Hegemonic erosion explains how a crisis can weaken the ordering capacity of the strongest actor even when that actor retains material power (Gilpin 1981). This supports anchor-power credibility loss, alliance drift, strategic-buyer autonomy, and regional power-center rebalancing.

Coercive diplomacy explains why pressure can operate through selective and conditional enforcement rather than full war (George and Simons 1994; Baldwin 1985). This supports selective interdiction, monitored passage, toll-like regimes, and maritime-legality ambiguity.

## 2.5 Institutional Friction as Strategic Variable

MESSINA treats institutional friction as part of the control architecture of power. Friction refers to delays, review structures, objections, and internal checks that force contradiction into the decision process before tactical motion hardens into strategic drift.

Friction is not a moral category. It can be misused. Delay can help adversaries adapt, disperse, exploit hesitation, or shape the diplomatic field. But a system that strips out friction may become better at starting crises and worse at governing them.

The framework therefore distinguishes between two capacities:

- the capacity to act;
- the capacity to contain the consequences of action.

A lower-friction system may move first, strike harder, and compress decision cycles. What tends to degrade is its ability to absorb contradiction, process bad news, coordinate allies, maintain legal standing, and prevent second-order effects from outrunning intent.

## 2.6 Decision Sovereignty as Deferred Causal Layer

The Decision Sovereignty Layer is a planned V26 / Corvus research branch, not a dynamics-affecting part of the v25.9 public release. It should still be explained here because the v25.9 governance diagnostics are best understood as precursor signals for that future layer.

Decision sovereignty means the ability of a political system to make, revise, and stop strategic decisions without losing control to filtered information, compressed review, private platform dependencies, fragmented command behavior, or capability illusions. It is not the same as executive speed. It is the ability to govern action over time.

The future Decision Sovereignty Layer would model six mechanisms:

1. **epistemic collapse** - filtered information and suppressed bad news reduce decision accuracy;
2. **decision velocity trap** - procedural friction is removed faster than error checking can adapt;
3. **platform dependency asymmetry** - state functions depend on external private-stack capabilities;
4. **mosaic response** - centralized deterrence or negotiation breaks into decentralized response patterns;
5. **legitimacy erosion** - repeated governance failure weakens institutional trust and raises blowback risk;
6. **capability illusion** - more sensing, computation, or targeting does not necessarily mean better political control.

V25.9 does not implement this as a causal engine because the proxy weights remain design choices, replay invariants must be protected, and politicization risk is high if causal claims outrun calibration. Instead, V25.9 uses observer-only diagnostics to surface governance deterioration without allowing those diagnostics to change core stress dynamics.

This is a conservative design choice. It makes the public release weaker in causal ambition but stronger in interpretability.

## 2.7 Platform Dependency and Rented Visibility

Platform dependency deserves separate theoretical treatment. In modern maritime crises, states often depend on commercial or semi-commercial systems to see, route, monitor, insure, and interpret the operational environment. Satellite tracking, private ship-tracking systems, commercial routing data, vendor dashboards, and private intelligence or monitoring feeds can become part of the state's practical visibility stack.

This creates a distinction between public authority and rented visibility. A government may issue an order, but its practical enforcement picture may depend on systems outside direct democratic accountability. Those systems may be excellent, but they are not neutral public institutions. They have owners, incentives, gaps, terms of service, data limits, and legal exposure.

In MESSINA, platform dependency does not mean private platforms caused the crisis. It means degraded public governance can lean more heavily on private visibility systems because it has to. When this dependency rises, the gap between formal coercive intent and practical control can widen. In a chokepoint crisis, that gap appears in insurance quotes, flag-state behavior, routing decisions, and burden-sharing disputes before it appears as a formal strategic failure.

## 2.8 Aggregation as Theory of Interpretation

Aggregation is not merely a reporting convenience in MESSINA. It is part of the theory of interpretation.

A terminal average can hide the crisis structure that matters most. Two runs may produce similar peak stress while arriving there through different paths. One may climb gradually with broad coordination; another may remain superficially stable until a late fragmented lock-in. These cases may look similar in a table and mean very different things strategically.

MESSINA therefore treats aggregation as a bridge between raw dynamics and defensible interpretation. Several forms matter:

- **summary aggregation**, which gives high-level comparable outputs;
- **path aggregation**, which asks how runs arrive at outcomes over time;
- **regime aggregation**, which groups runs into behaviorally meaningful phase classes;
- **dispersion-sensitive comparison**, which exposes hidden unevenness across blocs, layers, and channels;
- **sensitivity reporting**, which identifies which assumptions drive interpretation.

The public v25.9 release exposes only part of this ambition. It includes documented comparison surfaces and public governance diagnostics. The broader internal lineage contains richer path, regime, replay, threshold, and sensitivity artifacts. Those should not be overclaimed in the public release, but the theory is important: the meaning of a crisis output depends on the path, distribution, and regime texture behind it.

## 2.9 Cross-Scale Recurrence Without Formal Fractality

MESSINA is multiscale and complex-systems aware. It includes heterogeneity, path dependence, threshold behavior, cross-domain propagation, and dispersion. It should not yet be described as a formal fractal analytics system.

The correct description is narrower: cross-scale recurrence is an interpretive discipline. Similar patterns may appear at different scales - fragmented discourse at the Nano layer, polarized agent behavior at the Micro layer, uneven institutional resilience at the Mezzo layer, network-channel dispersion at the Network layer, and fragmented phase texture at the Macro layer. But the current public release does not measure formal fractal signatures.

This distinction prevents overstatement. MESSINA can use cross-scale recurrence as a reading discipline without claiming to have a stabilized fractal-diagnostics stack. A future observer layer could add formal cross-scale similarity metrics, but that belongs to later research.

## 2.10 Chokepoint Topology

Not all chokepoints propagate stress the same way. A useful public theory line must distinguish chokepoint topology.

Hormuz is an energy-security chokepoint with strong oil, LNG, insurance, Gulf basing, strategic-buyer, and fertilizer-input connections. EIA and IEA reporting confirm the scale of Hormuz oil and LNG exposure, while UNCTAD's maritime transport reporting shows how chokepoint disruption can reroute shipping, raise costs, and pressure food and energy systems (EIA 2026; IEA 2026; UNCTAD 2024). Bab el-Mandeb has a stronger rerouting, Red Sea, Suez-linkage, and intermittent-disruption profile. Suez is a canal chokepoint with different legal, logistical, and infrastructure constraints. Panama is an infrastructure and climate-sensitive chokepoint. Taiwan / South China Sea is a higher-intensity strategic and technology-dependent environment with stronger alliance and escalation implications.

This means Hormuz-centered outputs should not be transferred mechanically to other theaters. The public scenario briefs mark future comparison targets and mechanism cues. They are not executable claims that the current Hormuz output generalizes across all chokepoints.

## 2.11 Theory-Layer Mapping

Theories in MESSINA are not prestige labels applied uniformly. They perform different jobs at different layers.

At the **Nano layer**, securitization and prospect-style pressure are most relevant. They shape signal injections, fear, outrage, legitimacy language, moral-restraint dynamics, and discourse-level pressure.

At the **Micro layer**, prospect logic, rally dynamics, sunk-cost escalation, and hope dynamics shape agent-level choices under threat and perceived loss.

At the **Mezzo layer**, organizational delay and coercive diplomacy shape institutional lag, coordination stress, legitimacy, resilience, throughput, and clustered response.

At the **Network layer**, Normal Accident Theory and complex interdependence shape lateral propagation across shipping, finance, food, humanitarian, legal, diplomatic, digital, cyber, and military channels.

At the **Macro layer**, hysteresis, plateau-versus-cascade logic, phase texture, and hegemonic erosion shape the relationship between visible stress and governability.

At the **Module layer**, multiple theory influences combine according to functional purpose. A shipping module may be mostly circulation logic. An escalation-trap module may draw more on sunk-cost and prospect dynamics. A diplomacy module may draw on securitization, legal cohesion, alliance friction, and organizational delay.

## 2.12 Operationalization Bridge: From Theory to Variables

The theories above do not enter MESSINA as prestige labels. They are translated into observable or inspectable mechanism families. This bridge is deliberately explicit because the model's main vulnerability would be to encode theory without showing how conceptual claims become variables, proxies, or overlays.

- **Securitization theory** maps into legal cohesion, congressional constraint, negotiation credibility, information distortion, legitimacy strain, and the compression of dissent. In the public observer surface, these appear most directly through decision friction and epistemic integrity.
- **Normal Accident Theory** maps into cross-channel propagation, coupling, threshold behavior, phase texture, and dispersion. It supports the circulation-crisis claim that a local chokepoint shock can propagate laterally across shipping, insurance, food, finance, law, diplomacy, and alliance politics.
- **Coercive logic and damage-control separation** map into selective interdiction credibility, buyer testing, target hardening, enforcement ambiguity, and the gap between tactical action and strategic control.
- **Complex interdependence** maps into the interaction of shipping, insurance, routing, fertilizer and food inputs, finance, alliance consent, and platform dependency.
- **Organizational delay** maps into ceasefire lag, delegated command depth, local unit autonomy, institutional response lag, and the mosaic-response diagnostic.
- **Prospect, rally, and sunk-cost mechanisms** map into escalation under perceived loss, domestic hardening, commitment lock-in, and reduced reversibility after visible costs have been paid.
- **Hegemonic erosion** maps into anchor-power credibility loss, alliance drift, strategic-buyer autonomy, regional power-center rebalancing, and the decline of enforcement credibility under selective or inconsistent control.

This bridge does not claim full empirical calibration. It defines the path from theory to encoded mechanism so that readers can identify where they agree, disagree, or would alter assumptions.

## 3. Methodology

## 3.1 Design Aim and Output Philosophy

MESSINA is a mechanism-encoding, research-oriented stress-testing framework. It is designed to compare structured crisis worlds under controlled assumptions. It treats computational modeling as a disciplined map of complex adaptive social behavior rather than a literal reproduction of the world (Miller and Page 2007).

It is not built to answer: "What will happen next?" It is built to answer questions such as:

- what kinds of downstream patterns become more visible under one governance setting than another;
- which pathways dominate under specific assumptions;
- how much crisis structure is hidden by terminal averages;
- which dimensions of control deteriorate before visible collapse occurs;
- whether a policy interpretation is consistent with a transparent comparison surface.

Outputs should be read as comparative structured signals rather than literal forecasts.

## 3.2 Architecture, Analytics, Protocol, and Case

MESSINA is organized around four components.

**Architecture** builds structured crisis worlds under encoded assumptions. It contains the logic for layers, variables, propagation, agents, phases, modules, and state updates.

**Analytics** reads repeated runs and comparative differences. It includes branch dominance, scenario comparison, governance-diagnostic interpretation, aggregation-aware reading, sensitivity reporting, and validation surfaces.

**Protocol** translates analytical readings into policy-facing crisis-navigation implications. Protocol is not command logic. It is a translation discipline from diagnostics to safeguards: what kind of review, consultation, exception, or braking mechanism would respond to the exposed failure mode?

**Case** contains scenario-specific assumptions, chronology encoding, overlays, actor settings, and provenance. The case is separable from the engine.

This distinction matters. If the Architecture is confused with the Case, a scenario assumption can be mistaken for a general law. If Analytics is confused with Protocol, a diagnostic can be mistaken for a policy command. If Protocol is confused with prediction, the framework is overstated.

## 3.3 Engine and Case Separation

A central rule is that the engine and the case are never confused.

The engine contains general crisis logic: layer interactions, propagation structure, aggregation machinery, phase rules, validation surfaces, and output contracts.

The case contains scenario-specific assumptions: initial values, event chronology, actor settings, region mapping, overlay conditions, parameter rationales, evidence references, and assumption records.

The public v25.9 release preserves this separation in narrower form. The public-safe runner does not expose the full internal engine. It reproduces the public governance formulas and comparison outputs from included configs. That is enough to inspect the article-facing governance argument, but it is not a full historical-engine replay.

## 3.4 Scenario Pack Structure

A scenario pack in the broader MESSINA architecture contains:

- **start_core**, the initial values for all 72 core variables;
- **region_map**, mapping actors or countries to analytical regions;
- **discourse_priors**, initial sentiment distributions across regions;
- **baseline_floor**, equilibrium values toward which variables revert in the absence of shocks;
- **event_specs**, time-stamped events with effects, confidence, decay mode, and tags;
- **tail_risks**, conditional low-probability events triggered by threshold conditions;
- **parameter_records**, recording source and rationale for coefficients;
- **evidence_records**, recording claims and citations backing key assumptions;
- **assumption_records**, recording scope and risk-if-wrong for structural assumptions.

This structure is meant to make the case auditable and separable from the engine. The public repository exposes a simplified public-facing version of this discipline through configs, ledgers, schemas, and documentation.

## 3.5 Layered Mixed-Resolution Structure

The broader v25.x architecture uses six layers.

### Nano Layer

The Nano layer handles discrete triggers, signal injections, and discourse-level dynamics. It includes eight discourse dimensions: shipping security, market panic, diplomacy, moral peace, food exposure, anti-blockade sentiment, strategic autonomy, and alliance friction. These are distributed across analytical regions.

### Micro Layer

The Micro layer is agent-based. It uses a configurable population size, from smaller test settings to larger full-mode runs. Agents are distributed across eight blocs: anchor center, Europe, Middle East security, Gulf hedgers, Asia importers, Eurasia revisionists, global shipping-finance, and global south food. They also sit across eleven sectors: voter, executive, military, energy, shipping, finance, media, diplomat, religious, humanitarian, and agriculture.

Agents choose among four actions: comply, resist, escalate, and mediate. The utility structure uses prospect-style logic, bandit learning, loss sensitivity, honor commitment, and hope dynamics. The use of agent-level heterogeneity and bottom-up emergence follows the general agent-based modeling tradition rather than claiming direct behavioral calibration (Epstein 2006; North and Macal 2007; Macal and North 2010; Wilensky and Rand 2015).

### Mezzo Layer

The Mezzo layer clusters agents into institutional aggregates. It includes organizational delay with configurable lag. It produces pressure, resilience, coordination, legitimacy, throughput, base exposure, infrastructure integrity, and dispersion signals.

### Network Layer

The Network layer propagates stress laterally across twelve coupled channels: physical, shipping, energy, financial, digital, legal, diplomatic, humanitarian, food, climate, cyber, and military. It uses sparse adjacency structure and cross-channel interaction terms.

### Macro Layer

The Macro layer tracks phase transitions, variance, autocorrelation, order resilience, and phase texture. It is responsible for high-level regime reading rather than tactical detail.

### Module Layer

The Module layer evaluates functional mechanism bundles that synthesize cross-layer signals. It is where shipping, finance, diplomacy, food, command delegation, strategic buyer dynamics, and fragmentation become readable as named mechanism families.

## 3.6 Phase System

The engine operates an eight-phase regime system:

1. stable;
2. tension;
3. coercive contest;
4. managed attrition;
5. shipping crisis;
6. blockade regime;
7. regional cascade;
8. hegemonic fracture.

Each phase is defined by an entry threshold and a lower hysteresis threshold. Hysteresis prevents rapid oscillation between phases. This threshold-and-regime logic is consistent with the wider critical-transition literature, though MESSINA does not claim full empirical tipping-point calibration (Scheffer 2009; Scheffer et al. 2009). A lock-duration parameter prevents phase changes within a configurable window after the last transition.

The V25.4 extension adds phase-texture annotation, marking whether a phase is **uniform** or **fragmented**. This matters because two runs can occupy the same phase label while having very different internal stress distributions.

## 3.7 Module Architecture

The internal v25.9 architecture contains two dozen functional modules. Earlier draft language referring to 22 modules is too narrow for the current internal architecture and should not be used.

The 24 modules are:

1. shipping module;
2. finance module;
3. diplomacy module;
4. humanitarian module;
5. food module;
6. autonomy module;
7. cyber module;
8. media module;
9. military-political module;
10. base-alliance module;
11. escalation-trap module;
12. infrastructure-humanitarian module;
13. hegemonic-shift module;
14. strategic-deterrence module;
15. command-delegation module;
16. horizontal-escalation module;
17. Gulf-fragmentation module;
18. domestic-legitimacy module;
19. strategic-deterrence-dynamics module;
20. intelligence-coordination module;
21. economic-cascade module;
22. branch-point module;
23. strategic-buyer-interdiction module;
24. fragmentation module.

These modules are weighted composites of core variables and cross-layer signals. They are not independent theories. They are functional bundles designed to make mechanism families readable.

The fragmentation module, introduced in the V25.4-V25.5 development path, aggregates dispersion signals as a first-class output and contributes a small weight to systemic stress in the internal merge step. This reflects the idea that fragmentation is not only a descriptive property; in the internal engine, under bounded rules, it can contribute to crisis stress.

The public-safe repository does not expose the full internal module engine. It documents public module families and releases observer-only governance diagnostics.

For that reason, the module list in this paper is an architectural inventory, not a public reproducibility claim. The Section 4 demonstration does not require the reader to rerun the full two-dozen-module engine. It rests on public governance profiles, explicit observer formulas, overlay configs, and rerunnable comparison artifacts. Future releases can strengthen the bridge by adding module-level pseudocode, minimal executable module fixtures, or public test cases for selected modules such as shipping, finance, food, and diplomacy.

## 3.8 Governance Proxies

Five governance proxies form the diagnostic surface of the public v25.9 release.

**Epistemic integrity** measures informational quality:

```
epistemic_integrity =
1.0 - (
    0.35 * intelligence_reliability_gap
  + 0.30 * info_distortion
  + 0.20 * intelligence_contamination
  + 0.15 * (1.0 - negotiation_credibility)
)
```

**Decision friction** measures institutional braking:

```
decision_friction =
    0.40 * congressional_constraint
  + 0.30 * negotiation_credibility
  + 0.20 * legal_cohesion
  + 0.10 * religious_moral_constraint
```

**Platform dependency** is set directly in the governance profile and measures reliance on commercial monitoring infrastructure outside state control.

**Mosaic response** measures distributed and uneven crisis response:

```
mosaic_response =
    0.35 * delegated_command_depth
  + 0.25 * local_unit_autonomy
  + 0.20 * strategic_control_gap
  + 0.20 * ceasefire_lag
```

**Governance erosion** integrates all four:

```
governance_erosion =
    0.30 * (1.0 - epistemic_integrity)
  + 0.25 * (1.0 - decision_friction)
  + 0.25 * platform_dependency
  + 0.20 * mosaic_response
```

The weights are design choices, not empirical estimates. The labels are conceptually informed and the formulas are explicit, but the outputs should not be mistaken for calibrated real-world measurements.

## 3.9 Worked Example: Public Governance Erosion Diagnostic

The public release should be judged first by the calculations it actually exposes. The governance-erosion diagnostic is the clearest worked example because it uses public formulas and public governance-profile values rather than non-public module code.

For any given governance profile, the public calculation proceeds in four steps:

1. compute **epistemic integrity** from intelligence reliability gap, information distortion, intelligence contamination, and negotiation credibility;
2. compute **decision friction** from congressional constraint, negotiation credibility, legal cohesion, and religious or moral constraint;
3. read **platform dependency** directly from the governance profile;
4. compute **mosaic response** from delegated command depth, local unit autonomy, strategic control gap, and ceasefire lag.

The composite governance erosion score then combines those components:

```
governance_erosion =
    0.30 * (1.0 - epistemic_integrity)
  + 0.25 * (1.0 - decision_friction)
  + 0.25 * platform_dependency
  + 0.20 * mosaic_response
```

In the high-friction public comparison, the resulting governance erosion is 0.561. In the frictionless public comparison, it is 0.693. The point is not that either number is an empirical measurement of the real world. The point is that the public assumptions are inspectable: a reader can change the weights, alter platform dependency, increase legal cohesion, or reduce mosaic response and then rerun the comparison. This is the public claim surface. It is deliberately narrower than the internal architecture but more defensible because it is visible and reproducible.

## 3.10 Dispersion Architecture

V25.4 introduced dispersion-aware processing into the broader architecture. It added per-bloc dispersion signals at the Mezzo layer, including standard deviation and selected percentile markers for state dimensions. It also added per-layer dispersion at the Network layer, a cross-layer dispersion index, and macro-level phase texture.

V25.5 made selected modules dispersion-aware. The diplomacy module consumes coordination standard deviation and diplomatic-layer tail pressure. The humanitarian module consumes legitimacy dispersion and humanitarian-layer tail pressure. The economic-cascade module consumes financial-layer tail pressure and low-end resilience.

Dispersion matters because similar mean scores can conceal different crisis shapes. A bloc where half the actors have severe stress and half remain stable can look similar in mean to one with uniform mid-level stress. The strategic implications differ. Dispersion exposes that gap.

## 3.11 Monte Carlo and Stochastic Discipline

The broader MESSINA lineage includes bounded Monte Carlo use. The historical MC512 reference point should be defended narrowly and should not be treated as a public validation claim for the v25.9 repository.

The public v25.9 demonstration does not rely on MC512 ensemble claims. It relies on explicit governance formulas, public configs, overlay comparisons, and a bounded runner. MC512 belongs to the broader internal lineage and is retained here only as development-history context until the relevant stochastic runner, sampling assumptions, seed protocol, and ensemble artifacts are released.

Monte Carlo repetition can be useful for branch stability, phase consistency, scenario comparison, and publication-level stress-testing under encoded assumptions. The use of repeated runs and sensitivity discipline follows standard simulation and global sensitivity-analysis practice (Saltelli et al. 2008; Sargent 2013). But stochastic repetition does not justify rare-event frequency claims about the external world, and unpublished ensemble machinery should not be used to strengthen public claims.

Three principles apply:

1. repeated runs can stabilize comparative interpretation when the sampling protocol is public;
2. replay and seed discipline matter for reproducibility;
3. stochastic repetition does not convert model outputs into real-world probabilities.

## 3.12 Aggregation and Provenance

Aggregation is the interpretive bridge between raw model dynamics and defensible outputs. This reflects a systems-thinking concern with feedback, delay, accumulation, and path-dependent interpretation rather than static snapshot reading (Sterman 2000). The current architecture direction includes summary aggregation, path aggregation, regime aggregation, dispersion-sensitive comparison, and sensitivity reporting.

Provenance is equally important. Scenario inputs should distinguish source type, reference, rationale, confidence, and calibration status. A value may be sourced, estimated, stylized, or placeholder. These categories should not be collapsed.

The public release includes schema and ledger files that support this discipline. It should not be read as a fully calibrated empirical model.

## 3.13 Public Release Validation Contract

The public release validates a bounded set of claims:

- the public-safe runner executes;
- required scenario keys are checked before execution;
- documented public formulas reproduce the published governance-observer outputs;
- same-frame, different-governance comparison files can be rerun from included configs;
- included public unit tests pass;
- public artifacts match the documented observer surface.

The public release does not validate:

- full external empirical calibration;
- full historical-engine replay;
- public execution of the complete two-dozen-module internal engine;
- rare-event probability estimation;
- a complete causal governance layer;
- a first-class public fractal-diagnostics stack;
- real-time early warning through live data feeds.

This validation contract is central. Without it, the framework can be overstated. With it, the public release remains inspectable and appropriately bounded.

## 4. Demonstration

## 4.1 Public Evidence Surface

The bounded public demonstration holds the broad Hormuz crisis frame constant while varying governance conditions. The public runner reproduces governance-observer outputs from included configs. It should be described as an observer-only comparison surface, not as a full dynamic proof of every policy interpretation.

The key public comparison is between a high-friction governance condition and a frictionless counterfactual. Extended configs then create a friction spectrum, policy overlays, and thematic overlays.

## 4.2 Core Comparison: High Friction vs. Frictionless

- Peak stress: high friction 0.798; frictionless 0.800; delta +0.002.
- Governance erosion: high friction 0.561; frictionless 0.693; delta +0.132.
- Decision friction: high friction 0.475; frictionless 0.446; delta -0.029.
- Platform dependency: high friction 0.15; frictionless 0.65; delta +0.50.

The headline finding is not that the opening crisis becomes dramatically larger. Peak stress barely moves. The more important change is hidden governability. Governance erosion rises by 0.132. Decision friction falls. Platform dependency rises from 0.15 to 0.65.

The opening punch looks similar. The ability to absorb contradiction, preserve review, and manage consequences after the first move deteriorates.

## 4.3 Friction Spectrum

The extended comparison widens the binary contrast into a bounded gradient.

- High friction: peak 0.798; decision friction 0.475; governance erosion 0.561; platform dependency 0.15.
- Mildly reduced friction: peak 0.798; decision friction 0.468; governance erosion 0.594; platform dependency 0.28.
- Moderately reduced friction: peak 0.799; decision friction 0.461; governance erosion 0.627; platform dependency 0.40.
- Severely reduced friction: peak 0.799; decision friction 0.454; governance erosion 0.660; platform dependency 0.53.
- Frictionless: peak 0.800; decision friction 0.446; governance erosion 0.693; platform dependency 0.65.

The gradient matters because it prevents an all-or-nothing interpretation. Governance degradation is progressive rather than visible only at extremes. Each reduction in friction produces higher governance erosion and platform dependency while peak stress remains nearly flat.

## 4.4 Policy Overlays

Four policy overlays test illustrative braking mechanisms against the frictionless counterfactual.

- 12h notification: decision friction 0.459; governance erosion 0.672; platform dependency 0.58; delta erosion -0.021.
- Structured dissent: decision friction 0.459; governance erosion 0.675; platform dependency 0.60; delta erosion -0.018.
- Automatic sunset: decision friction 0.455; governance erosion 0.675; platform dependency 0.59; delta erosion -0.018.
- Minimum brake package: decision friction 0.472; governance erosion 0.651; platform dependency 0.52; delta erosion -0.042.

The overlays are illustrative governance-condition experiments, not direct legal simulations. The 12-hour notification overlay is deliberately stricter than the current U.S. War Powers Resolution baseline; current law includes a 48-hour reporting requirement when U.S. forces are introduced into hostilities or comparable situations, so the overlay should be read as a modeled safeguard rather than a description of existing law (50 U.S.C. § 1543). Individual mechanisms produce modest improvements. The minimum brake package - combining congressional notification, sunset clauses, and structured dissent - produces the largest reduction in governance erosion and the most substantial recovery of decision friction.

The interpretation is narrow: bundled braking mechanisms outperform isolated measures in the public comparison surface.

## 4.5 Theme Overlays

Thematic overlays make selected mechanisms more visible without claiming to reproduce a full historical engine.

- Allied legal objections: decision friction 0.466; governance erosion 0.668; platform dependency 0.57; delta erosion -0.025.
- Food/fertilizer carveout: decision friction 0.456; governance erosion 0.667; platform dependency 0.56; delta erosion -0.026.
- Buyer testing emphasis: decision friction 0.436; governance erosion 0.704; platform dependency 0.68; delta erosion +0.011.

The buyer-testing emphasis overlay worsens governance erosion relative to the frictionless counterfactual. That is important. Not every engagement mechanism functions as a brake. Some interactions expose credibility gaps and accelerate governance deterioration.

Allied legal objections and food/fertilizer carve-outs produce modest improvements, consistent with the policy article's argument that allied consultation and pre-negotiated civilian exceptions can function as control mechanisms.

## 4.6 Reading the Demonstration Correctly

The public demonstration should be read as a disciplined comparison, not a prediction. It does not say that a particular real-world crisis will produce these values. It says that, under the documented v25.9 public configs and formulas, similar visible stress can coexist with materially different governance diagnostics.

That is enough to support the article's core claim: a chokepoint crisis can reveal a gap between coercive intent and systemic control.

## 5. Limitations and Validation

## 5.1 Structural Limits

MESSINA is a comparative stress-testing framework, not a forecasting engine.

Indicators such as decision friction, governance erosion, platform dependency, and mosaic response are comparative proxies. They are not natural-unit measurements and should not be read as direct empirical observations.

Scenario results depend on input construction. The framework is stronger on coupled-system stress than on fine-grained combat realism. It is better suited to representing shipping disruption, insurance repricing, fertilizer and food-input stress, sovereign-risk transmission, alliance hesitation, and governance friction decay than detailed targeting dynamics or tactical attrition rates.

Actor behavior is stylized. It is not psychologically complete.

Hormuz-centered outputs should not be transferred mechanically to other chokepoint theaters with different legal, logistical, alliance, commodity, and infrastructure structures.

## 5.2 Public-Release Limits

The public reproducibility surface is narrower than the full historical internal engine. The bounded public runner reproduces documented governance-observer formulas, single-run governance signals, comparison outputs, and overlay summaries. It should not be described as a complete release of the historical codebase.

The public release also does not expose a full first-class fractal diagnostics stack, a full Decision Sovereignty causal layer, or live-data early-warning functions.

## 5.3 Validation Status

The public package validates successful runner execution, required scenario-key checks, documented formula reproduction, included comparison outputs, and public unit-test passage. This language follows simulation-validation practice by distinguishing code verification, conceptual validity, operational validity, and external calibration (Sargent 2013).

The broader internal lineage includes richer validation and audit artifacts, including replay checks, threshold stability, baseline sensitivity ranking, scenario comparison, and same-horizon pack comparison. These artifacts inform the development history, but they should not be presented as if they were freshly reproduced by the bounded public runner.

The validation language must therefore stay conservative. The framework is inspectable and reproducible in bounded public form. It is not externally calibrated as a forecasting model.

## 5.4 Proxy and Weight Limits

The governance proxy weights are design choices. They reflect conceptual importance and make assumptions explicit. They are not estimated coefficients.

The correct defense is transparency, not calibration. A reader can inspect the formulas, challenge the weights, alter configs, and rerun comparisons. That makes the framework useful for structured argument. It does not make the weights empirically final.

## 5.5 Friction Is Not Always Good

Institutional friction is strategically meaningful, but not infinitely beneficial. Delay can help adversaries adapt. Legal review can be abused. Allied consultation can become cover for inaction. Bureaucratic review can create responsibility diffusion.

The claim is not that more friction is always better. The claim is that a system with too little friction may lose control over second-order effects, especially in a tightly coupled chokepoint crisis.

## 5.6 Non-Public Module Engine and Reproducibility Boundary

A likely criticism of MESSINA is that the paper describes a broader 72-variable, six-layer, two-dozen-module architecture while the public repository exposes a narrower governance-observer surface. That criticism is valid unless the status of each claim is kept separate.

The public release should not be read as a complete executable release of the internal module engine. The 24 modules are documented as architecture and mechanism families. They are not all independently rerunnable from the public package. The public demonstration in Section 4 therefore does not claim: "the full internal crisis engine has been publicly reproduced." It claims something narrower: "the article-facing governance-observer comparison can be inspected and rerun from public formulas, profiles, configs, and artifacts."

This boundary reduces ambition but increases honesty. It also defines the next reproducibility target. A later public release should add at least one minimal executable module fixture, preferably for a core mechanism such as shipping disruption, finance/insurance repricing, food/fertilizer exposure, or diplomacy/allied legal objection. Until then, the two-dozen-module list should be treated as an architectural inventory and future specification target, not as a public validation surface.

## 5.7 Design Priors and Confirmation Risk

Several MESSINA weights are design priors rather than empirically estimated coefficients. Used carelessly, this creates confirmation risk: a model can appear to confirm the theoretical assumptions embedded in its own design.

The defense is not neutrality by assertion. The defense is transparency. Formulas, configs, assumptions, weights, overlays, and interpretation rules must be visible enough for readers to challenge, alter, and rerun the comparison. The public v25.9 release should therefore be read as a structured argument under explicit assumptions, not as an objective geopolitical measurement instrument.

This limitation does not make the framework useless. It defines its proper role. MESSINA is strongest when used to compare mechanism-sensitive scenarios, expose hidden governability differences, and discipline policy claims against documented assumptions. It is weakest when used as if it were a calibrated oracle.

## 6. Future Directions

## 6.1 Decision Sovereignty Layer: V26 / Corvus

The planned V26 / Corvus branch would move from observer-only governance diagnostics toward a dynamics-affecting Decision Sovereignty Layer. This should not be added casually.

Before implementation, several conditions should be met:

- historical backtest surfaces should exist;
- coefficient estimation or disciplined prior selection should be developed;
- observer-only diagnostics should prove useful first;
- replay and plateau safety should be replaced by a new V26 contract;
- article-facing claims should remain weaker than model-facing assumptions.

The six candidate mechanisms are epistemic collapse, decision velocity trap, platform dependency asymmetry, mosaic response, legitimacy erosion, and capability illusion.

## 6.2 Cross-Theater Extensibility

The current public case surface is Hormuz-centered. Future comparison work can extend toward Bab el-Mandeb, Suez, Panama, and Taiwan / South China Sea. The existing non-executable briefs should remain clearly marked as mechanism sketches rather than executable scenario packs.

Cross-theater work should begin with topology, not analogy. Each chokepoint has different coupling structure. Energy dependence, canal infrastructure, climate constraints, military escalation risk, alliance commitments, legal regimes, and commodity exposure vary sharply.

## 6.3 Aggregation and Critical-Transition Work

Future MESSINA work should strengthen aggregation and critical-transition monitoring. Useful extensions include:

- lead-lag aggregation;
- event-chain aggregation;
- uncertainty decomposition by source;
- robust cross-pack discrimination;
- explicit critical-transition monitoring;
- observer-level cross-scale recurrence diagnostics.

These should be added conservatively, preferably as observer layers before changing engine dynamics. The current public release does not implement a formal fractal-metric layer; cross-scale recurrence remains an interpretive discipline and a future research target.

## 6.4 Platform Dependency Measurement

Platform dependency is currently a proxy value in the governance profile. Future work should separate its components:

- sensing dependency;
- routing dependency;
- insurance-data dependency;
- private intelligence or monitoring dependency;
- cloud and compute dependency;
- legal accountability gap;
- substitutability under crisis conditions.

This would make the platform-dependency concept more defensible and less monolithic.

## 6.5 Empirical Calibration

Empirical calibration should be layered rather than assumed. Candidate historical comparison surfaces include OPEC 1973, Suez 1956, tanker-war episodes, Aramco 2019, Ever Given 2021, Houthi/Red Sea disruptions, and selected sanctions or interdiction episodes.

The purpose of calibration would not be to convert MESSINA into a precise forecasting machine. It would be to discipline ranges, weights, and mechanism assumptions.

## 7. Conclusion

This working paper documents the theoretical foundations, methodological architecture, public-release boundary, and bounded demonstration surface of MESSINA v25.9.

The framework's central contribution is a structured way to compare how similar chokepoint shocks behave under different governance conditions. The public v25.9 comparison shows that peak stress can remain nearly flat while governance erosion, platform dependency, and loss of institutional braking worsen materially.

That is the core article-facing insight: the strait is not the crisis by itself. It is the place where a gap becomes visible - the gap between coercive intent and systemic control.

MESSINA does not claim to predict crises or assign reliable probabilities to real-world events. It claims something narrower: governance conditions are structural variables. They shape whether coercion at a chokepoint remains a limited instrument or becomes an accelerant of wider disorder.

The public code repository, scenario configurations, governance formulas, comparison artifacts, and overlay suite are available at: https://github.com/emreertuhi/messina-v25-9-public


## 8. References

Allison, Graham, and Philip D. Zelikow. 1999. *Essence of Decision: Explaining the Cuban Missile Crisis*. 2nd ed. New York: Longman.

Arkes, Hal R., and Catherine Blumer. 1985. "The Psychology of Sunk Cost." *Organizational Behavior and Human Decision Processes* 35 (1): 124-140. https://doi.org/10.1016/0749-5978(85)90049-4.

Baldwin, David A. 1985. *Economic Statecraft*. Princeton, NJ: Princeton University Press.

Buzan, Barry, Ole Wæver, and Jaap de Wilde. 1998. *Security: A New Framework for Analysis*. Boulder, CO: Lynne Rienner.

Cyert, Richard M., and James G. March. 1963. *A Behavioral Theory of the Firm*. Englewood Cliffs, NJ: Prentice-Hall.

Epstein, Joshua M. 2006. *Generative Social Science: Studies in Agent-Based Computational Modeling*. Princeton, NJ: Princeton University Press.

George, Alexander L., and William E. Simons, eds. 1994. *The Limits of Coercive Diplomacy*. 2nd ed. Boulder, CO: Westview Press.

Gilpin, Robert. 1981. *War and Change in World Politics*. Cambridge: Cambridge University Press. https://doi.org/10.1017/CBO9780511664267.

Kahneman, Daniel, and Amos Tversky. 1979. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47 (2): 263-292. https://doi.org/10.2307/1914185.

Keohane, Robert O., and Joseph S. Nye Jr. 2012. *Power and Interdependence*. 4th ed. Boston: Longman.

Macal, Charles M., and Michael J. North. 2010. "Tutorial on Agent-Based Modelling and Simulation." *Journal of Simulation* 4: 151-162. https://doi.org/10.1057/jos.2010.3.

March, James G., and Herbert A. Simon. 1958. *Organizations*. New York: John Wiley & Sons.

Miller, John H., and Scott E. Page. 2007. *Complex Adaptive Systems: An Introduction to Computational Models of Social Life*. Princeton, NJ: Princeton University Press.

Mueller, John E. 1973. *War, Presidents, and Public Opinion*. New York: John Wiley & Sons.

North, Michael J., and Charles M. Macal. 2007. *Managing Business Complexity: Discovering Strategic Solutions with Agent-Based Modeling and Simulation*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195172119.001.0001.

Pape, Robert A. 1996. *Bombing to Win: Air Power and Coercion in War*. Ithaca, NY: Cornell University Press.

Perrow, Charles. 1999. *Normal Accidents: Living with High-Risk Technologies*. Updated ed. Princeton, NJ: Princeton University Press.

Saltelli, Andrea, Marco Ratto, Terry Andres, Francesca Campolongo, Jessica Cariboni, Debora Gatelli, Michaela Saisana, and Stefano Tarantola. 2008. *Global Sensitivity Analysis: The Primer*. Chichester: John Wiley & Sons.

Sargent, Robert G. 2013. "Verification and Validation of Simulation Models." *Journal of Simulation* 7 (1): 12-24. https://doi.org/10.1057/jos.2012.20.

Scheffer, Marten. 2009. *Critical Transitions in Nature and Society*. Princeton, NJ: Princeton University Press. https://doi.org/10.1515/9781400833276.

Scheffer, Marten, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, and George Sugihara. 2009. "Early-Warning Signals for Critical Transitions." *Nature* 461: 53-59. https://doi.org/10.1038/nature08227.

Schelling, Thomas C. 1966. *Arms and Influence*. New Haven, CT: Yale University Press.

Staw, Barry M. 1976. "Knee-Deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action." *Organizational Behavior and Human Performance* 16 (1): 27-44. https://doi.org/10.1016/0030-5073(76)90005-2.

Sterman, John D. 2000. *Business Dynamics: Systems Thinking and Modeling for a Complex World*. Boston: Irwin/McGraw-Hill.

Wæver, Ole. 1995. "Securitization and Desecuritization." In *On Security*, edited by Ronnie D. Lipschutz, 46-87. New York: Columbia University Press.

Wilensky, Uri, and William Rand. 2015. *An Introduction to Agent-Based Modeling: Modeling Natural, Social, and Engineered Complex Systems with NetLogo*. Cambridge, MA: MIT Press.

## 9. Evidence and Data Sources

Britannica. 2026. "Suez Crisis." Updated January 12, 2026. Used only for a compact public-history check; the primary Suez documentary anchor remains the U.S. State Department FRUS collection.

Energy Information Administration. 2023. "The Strait of Hormuz Is the World's Most Important Oil Transit Chokepoint." *Today in Energy*, November 21, 2023.

Energy Information Administration. 2025. "Amid Regional Conflict, the Strait of Hormuz Remains Critical Oil Chokepoint." *Today in Energy*, June 16, 2025.

Energy Information Administration. 2026. "World Oil Transit Chokepoints." U.S. Energy Information Administration, updated 2026.

Food and Agriculture Organization of the United Nations. 2022. "The Importance of Ukraine and the Russian Federation for Global Agricultural Markets and the Risks Associated with the Current Conflict." Information Note, March 11, 2022.

International Energy Agency. 2026. "Strait of Hormuz." Factsheet, last updated February 2026.

Lloyd's Market Association. 2026. "JWLA-033: JWC Listed Areas - Hull War, Piracy, Terrorism and Related Perils." Joint War Committee Circular, March 3, 2026.

Lloyd's Market Association. 2026. "Listed Areas." Joint War Committee listed areas page. Used to verify that the JWC list identifies perceived enhanced-risk areas and that rating remains a matter for individual negotiation.

UN Trade and Development. 2024. *Review of Maritime Transport 2024: Navigating Maritime Chokepoints*. Geneva: United Nations.

UN Trade and Development. 2024. "Vulnerability of Supply Chains Exposed as Global Maritime Chokepoints Come under Pressure." Press Release UNCTAD/PRESS/PR/2024/024, October 22, 2024.

U.S. Code. 2026. 50 U.S.C. § 1543, "Reporting Requirement." Used for the War Powers Resolution reporting baseline.

U.S. Department of Agriculture, Foreign Agricultural Service. 2022. "Impacts and Repercussions of Price Increases on the Global Fertilizer Market." International Agricultural Trade Report, June 30, 2022.

U.S. Department of State, Office of the Historian. 1955-1957. *Foreign Relations of the United States, 1955-1957, Suez Crisis, July 26-December 31, 1956, Volume XVI*. Used as the primary documentary collection for the Suez comparison.

World Bank. 2026. "Commodity Markets." Commodity price data and Commodity Markets Outlook portal, updated April 2026.

## 10. Reference Verification Statement

This working paper separates theory references from empirical and institutional evidence sources. The theory sources in Section 8 were checked against publisher, university, DOI, library, or reputable disciplinary records. The empirical and institutional sources in Section 9 were checked against official or primary-source pages where available, including EIA, IEA, UNCTAD, FAO, USDA FAS, World Bank, Lloyd's / LMA, U.S. Code, and the U.S. Department of State Office of the Historian.

The source-verification log is not a substitute for the repository's parameter ledger or evidence ledger. It records bibliographic verification and the role each source plays in the working paper. The full log should be included in the public repository together with the scenario configs, governance formulas, comparison artifacts, and overlay suite.

Three citation-hygiene checks were applied in v1.3. First, Gilpin (1981) is now included in the source-verification log because it is used inline for hegemonic erosion. Second, Miller and Page (2007) is used inline in the methodology section to support the complex-adaptive-systems modeling frame. Third, Sterman (2000) is used inline in the aggregation/provenance section to support feedback, delay, and systems-thinking logic.

The legal basis for the 12-hour notification overlay is intentionally conservative. Current U.S. law includes a 48-hour reporting requirement under 50 U.S.C. § 1543 when U.S. forces are introduced into hostilities or comparable situations. MESSINA's 12-hour notification overlay is therefore a modeled safeguard stricter than current law, not a description of existing statutory timing.

## 11. Repository Provenance Note

The references above anchor the theoretical and empirical background. They do not replace the repository's internal provenance system. Scenario-specific assumptions, parameter choices, evidence records, validation artifacts, and overlay configurations should remain documented in the repository through `parameter_sources.md`, `article_relation.md`, `validation_status.md`, config files, generated artifacts, and any future citation or release notes.

The public reader should therefore treat this paper as having three layers of traceability: external literature, external empirical evidence, and internal repository provenance.

## Appendix A. Governance Proxy Formulas

### A.1 Epistemic Integrity

```
epistemic_integrity =
1.0 - (
    0.35 * intelligence_reliability_gap
  + 0.30 * info_distortion
  + 0.20 * intelligence_contamination
  + 0.15 * (1.0 - negotiation_credibility)
)
```

### A.2 Decision Friction

```
decision_friction =
    0.40 * congressional_constraint
  + 0.30 * negotiation_credibility
  + 0.20 * legal_cohesion
  + 0.10 * religious_moral_constraint
```

### A.3 Mosaic Response

```
mosaic_response =
    0.35 * delegated_command_depth
  + 0.25 * local_unit_autonomy
  + 0.20 * strategic_control_gap
  + 0.20 * ceasefire_lag
```

### A.4 Governance Erosion

```
governance_erosion =
    0.30 * (1.0 - epistemic_integrity)
  + 0.25 * (1.0 - decision_friction)
  + 0.25 * platform_dependency
  + 0.20 * mosaic_response
```

## Appendix B. Public / Internal Boundary Checklist

The public repository includes:

- public theory and methodology notes;
- public limits and interpretation rules;
- a bounded public-safe runner;
- public scenario configs;
- public formulas and registries;
- public artifacts for the v25.9 governance-observer surface;
- validation tests for the bounded public runner;
- friction-spectrum, policy-overlay, and theme-overlay summaries.

The public repository does not include:

- the full historical internal engine;
- every prior scenario family;
- a dynamics-affecting Decision Sovereignty Layer;
- a first-class public fractal-diagnostics layer;
- private working notes or internal design-memory materials;
- live-data early-warning functionality;
- external empirical calibration sufficient for probabilistic forecasting.

## Appendix C. Two Dozen Functional Modules in the Internal Architecture

This appendix is an architectural inventory, not a public reproducibility claim. The modules listed below document the broader internal model design and mechanism families. The public v25.9 release does not expose all module code or claim that Section 4 outputs are generated by independently rerunning the full two-dozen-module engine. Section 4 outputs are reproduced through the public governance-observer formulas, profiles, configs, and artifacts.

1. shipping module;
2. finance module;
3. diplomacy module;
4. humanitarian module;
5. food module;
6. autonomy module;
7. cyber module;
8. media module;
9. military-political module;
10. base-alliance module;
11. escalation-trap module;
12. infrastructure-humanitarian module;
13. hegemonic-shift module;
14. strategic-deterrence module;
15. command-delegation module;
16. horizontal-escalation module;
17. Gulf-fragmentation module;
18. domestic-legitimacy module;
19. strategic-deterrence-dynamics module;
20. intelligence-coordination module;
21. economic-cascade module;
22. branch-point module;
23. strategic-buyer-interdiction module;
24. fragmentation module.
