from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class GovernanceProfile:
    platform_dependency: float = 0.0


@dataclass
class ScenarioConfig:
    scenario_name: str
    description: str
    seed: int
    peak_stress: float
    archetype: str
    regime: str
    governance_profile: GovernanceProfile
    core: Dict[str, float]
