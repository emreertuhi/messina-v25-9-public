from __future__ import annotations

from typing import Dict
from .types import ScenarioConfig

WEIGHT_DISCLAIMER = "Governance proxy weights are design choices, not empirical estimates."


def epistemic_integrity(core: Dict[str, float]) -> float:
    return 1.0 - (
        0.35 * core["intelligence_reliability_gap"]
        + 0.30 * core["info_distortion"]
        + 0.20 * core["intelligence_contamination"]
        + 0.15 * (1.0 - core["negotiation_credibility"])
    )


def decision_friction(core: Dict[str, float]) -> float:
    return (
        0.40 * core["congressional_constraint"]
        + 0.30 * core["negotiation_credibility"]
        + 0.20 * core["legal_cohesion"]
        + 0.10 * core["religious_moral_constraint"]
    )


def mosaic_response(core: Dict[str, float]) -> float:
    return (
        0.35 * core["delegated_command_depth"]
        + 0.25 * core["local_unit_autonomy"]
        + 0.20 * core["strategic_control_gap"]
        + 0.20 * core["ceasefire_lag"]
    )


def governance_erosion(epistemic: float, friction: float, platform_dep: float, mosaic: float) -> float:
    return (
        0.30 * (1.0 - epistemic)
        + 0.25 * (1.0 - friction)
        + 0.25 * platform_dep
        + 0.20 * mosaic
    )


def compute_governance_signals(config: ScenarioConfig) -> Dict[str, float | str]:
    epi = epistemic_integrity(config.core)
    fric = decision_friction(config.core)
    plat = config.governance_profile.platform_dependency
    mosaic = mosaic_response(config.core)
    eros = governance_erosion(epi, fric, plat, mosaic)
    return {
        "epistemic_integrity_proxy": epi,
        "decision_friction_proxy": fric,
        "platform_dependency_proxy": plat,
        "mosaic_response_proxy": mosaic,
        "governance_erosion_score": eros,
        "weight_disclaimer": WEIGHT_DISCLAIMER,
    }
