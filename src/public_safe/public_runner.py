from __future__ import annotations

from typing import Dict

from .observer_formulas import compute_governance_signals
from .types import ScenarioConfig


def run_single(config: ScenarioConfig) -> Dict:
    signals = compute_governance_signals(config)
    return {
        "scenario_name": config.scenario_name,
        "description": config.description,
        "peak_stress": config.peak_stress,
        "archetype": config.archetype,
        "regime": config.regime,
        "governance_signals": signals,
    }


def compare_runs(left: ScenarioConfig, right: ScenarioConfig, left_label: str = 'left', right_label: str = 'right') -> Dict:
    left_run = run_single(left)
    right_run = run_single(right)
    lgs = left_run['governance_signals']
    rgs = right_run['governance_signals']
    comp = {
        left_label: {
            "peak_stress": left_run["peak_stress"],
            "governance_erosion_score": lgs["governance_erosion_score"],
            "epistemic_integrity_proxy": lgs["epistemic_integrity_proxy"],
            "decision_friction_proxy": lgs["decision_friction_proxy"],
            "platform_dependency_proxy": lgs["platform_dependency_proxy"],
            "mosaic_response_proxy": lgs["mosaic_response_proxy"],
            "archetype": left_run["archetype"],
            "regime": left_run["regime"],
        },
        right_label: {
            "peak_stress": right_run["peak_stress"],
            "governance_erosion_score": rgs["governance_erosion_score"],
            "epistemic_integrity_proxy": rgs["epistemic_integrity_proxy"],
            "decision_friction_proxy": rgs["decision_friction_proxy"],
            "platform_dependency_proxy": rgs["platform_dependency_proxy"],
            "mosaic_response_proxy": rgs["mosaic_response_proxy"],
            "archetype": right_run["archetype"],
            "regime": right_run["regime"],
        },
        "delta": {
            "peak_stress": right_run["peak_stress"] - left_run["peak_stress"],
            "governance_erosion_score": rgs["governance_erosion_score"] - lgs["governance_erosion_score"],
            "epistemic_integrity_proxy": rgs["epistemic_integrity_proxy"] - lgs["epistemic_integrity_proxy"],
            "decision_friction_proxy": rgs["decision_friction_proxy"] - lgs["decision_friction_proxy"],
            "platform_dependency_proxy": rgs["platform_dependency_proxy"] - lgs["platform_dependency_proxy"],
            "mosaic_response_proxy": rgs["mosaic_response_proxy"] - lgs["mosaic_response_proxy"],
        },
    }
    return {
        "comparison": comp,
        "seed_warning": "Same seed set does NOT imply identical stochastic conditions.",
        "weight_disclaimer": lgs["weight_disclaimer"],
    }
