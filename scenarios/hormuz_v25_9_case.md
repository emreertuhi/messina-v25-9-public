# Hormuz v25.9 Case File
## Human-Readable Public Scenario Note

## Purpose

This file translates the current public scenario and comparison surface into prose so that a reader does not have to infer the case logic from JSON files alone.

## What this case file represents

The public v25.9 release works with a narrow Hormuz-style chokepoint comparison frame.

It includes:
- one baseline public run,
- one higher-friction comparison condition,
- one reduced-friction comparison condition.

The point is not to simulate all of Hormuz history.
The point is to compare how a broadly similar chokepoint shock behaves when governance conditions change.

## Baseline public run

The baseline public run is:
- `configs/hormuz_v25_9_baseline.json`

This supports the documented baseline governance-observer surface for v25.9.

## Comparison overlays

The comparison pair is:
- `configs/governance_high_friction.json`
- `configs/governance_frictionless.json`

These are not meant to prove that one exact real-world polity had these exact values.
They are bounded comparison overlays used to stress-test the effect of stronger versus weaker institutional braking under a similar crisis frame.

## What is being held broadly constant

The comparison is designed to keep the chokepoint crisis frame broadly stable:
- maritime stress remains high,
- the archetype remains `rapid_shock_plateau`,
- the visible peak-stress profile changes only slightly.

## What is being changed

The comparison changes governance-facing conditions such as:
- institutional braking,
- negotiation credibility,
- legal cohesion,
- platform dependency,
- distributed response structure.

## Why this matters

The documented public comparison is built to illustrate a narrow claim:
a system can remain similarly stressed at the visible level while becoming much less governable underneath.

That is why the public release compares:
- `peak_stress`
with
- governance-observer signals such as decision friction, platform dependency, and governance erosion.

## Reading rule

This case file explains the public comparison surface only.
It should not be mistaken for a full release of every historical scenario pack, branch family, or internal scenario archive in the broader MESSINA lineage.
