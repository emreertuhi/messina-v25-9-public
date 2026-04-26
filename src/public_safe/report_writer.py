from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def write_json(path: str | Path, payload: Dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_single_run_report(path: str | Path, scenario_name: str, description: str, peak_stress: float, governance_signals: Dict) -> None:
    text = f"""# Public-Safe Single Run Report

## Scenario
- name: `{scenario_name}`
- description: {description}

## Summary
- `peak_stress`: `{peak_stress}`
- `epistemic_integrity_proxy`: `{governance_signals['epistemic_integrity_proxy']}`
- `decision_friction_proxy`: `{governance_signals['decision_friction_proxy']}`
- `platform_dependency_proxy`: `{governance_signals['platform_dependency_proxy']}`
- `mosaic_response_proxy`: `{governance_signals['mosaic_response_proxy']}`
- `governance_erosion_score`: `{governance_signals['governance_erosion_score']}`

## Note
This public-safe run reproduces the documented governance-observer surface of MESSINA v25.9. It is not a full historical-engine release and should not be treated as a forecasting system.

## Weight disclaimer
{governance_signals['weight_disclaimer']}
"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_compare_summary(path: str | Path, left_name: str, right_name: str, comparison: Dict) -> None:
    hf = comparison["comparison"][left_name]
    fr = comparison["comparison"][right_name]
    d = comparison["comparison"]["delta"]
    text = f"""# Public-Safe Comparison Summary

This comparison holds the chokepoint crisis frame broadly constant while varying governance conditions.

## {left_name}
- `peak_stress`: `{hf['peak_stress']}`
- `governance_erosion_score`: `{hf['governance_erosion_score']}`
- `decision_friction_proxy`: `{hf['decision_friction_proxy']}`
- `platform_dependency_proxy`: `{hf['platform_dependency_proxy']}`

## {right_name}
- `peak_stress`: `{fr['peak_stress']}`
- `governance_erosion_score`: `{fr['governance_erosion_score']}`
- `decision_friction_proxy`: `{fr['decision_friction_proxy']}`
- `platform_dependency_proxy`: `{fr['platform_dependency_proxy']}`

## Delta
- `peak_stress`: `{d['peak_stress']}`
- `governance_erosion_score`: `{d['governance_erosion_score']}`
- `decision_friction_proxy`: `{d['decision_friction_proxy']}`
- `platform_dependency_proxy`: `{d['platform_dependency_proxy']}`

## Weight disclaimer
{comparison['weight_disclaimer']}
"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
