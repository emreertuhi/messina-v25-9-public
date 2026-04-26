from __future__ import annotations

import json
from pathlib import Path
from .types import GovernanceProfile, ScenarioConfig


REQUIRED_CORE_KEYS = {
    "intelligence_reliability_gap",
    "info_distortion",
    "intelligence_contamination",
    "negotiation_credibility",
    "congressional_constraint",
    "legal_cohesion",
    "religious_moral_constraint",
    "delegated_command_depth",
    "local_unit_autonomy",
    "strategic_control_gap",
    "ceasefire_lag",
}


def _as_float(value: object, label: str, path: Path) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid numeric value for {label} in {path.name}: {value!r}") from exc


def _bounded(value: float, label: str, path: Path) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"Value for {label} in {path.name} must be in [0, 1], got {value!r}")
    return value


def load_scenario(path: str | Path) -> ScenarioConfig:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))

    if "scenario_name" not in data:
        raise ValueError(f"Missing scenario_name in {path.name}")
    if "peak_stress" not in data:
        raise ValueError(f"Missing peak_stress in {path.name}")
    if "core" not in data or not isinstance(data["core"], dict):
        raise ValueError(f"Missing or invalid core block in {path.name}")

    missing = REQUIRED_CORE_KEYS - set(data.get("core", {}).keys())
    if missing:
        raise ValueError(f"Missing required core keys in {path.name}: {sorted(missing)}")

    core: dict[str, float] = {}
    for key, raw_value in data["core"].items():
        value = _as_float(raw_value, f"core.{key}", path)
        # Public governance-observer configs use normalized values.
        core[key] = _bounded(value, f"core.{key}", path)

    gp = data.get("governance_profile", {})
    if not isinstance(gp, dict):
        raise ValueError(f"Invalid governance_profile block in {path.name}")
    platform_dependency = _bounded(
        _as_float(gp.get("platform_dependency", 0.0), "governance_profile.platform_dependency", path),
        "governance_profile.platform_dependency",
        path,
    )

    peak_stress = _bounded(_as_float(data["peak_stress"], "peak_stress", path), "peak_stress", path)

    return ScenarioConfig(
        scenario_name=str(data["scenario_name"]),
        description=data.get("description", ""),
        seed=int(data.get("seed", 0)),
        peak_stress=peak_stress,
        archetype=data.get("archetype", ""),
        regime=data.get("regime", ""),
        governance_profile=GovernanceProfile(platform_dependency=platform_dependency),
        core=core,
    )
