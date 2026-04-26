from __future__ import annotations

import math
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from public_safe.scenario_loader import load_scenario
from public_safe.public_runner import run_single, compare_runs


class TestPublicSafeRunner(unittest.TestCase):
    def test_single_run_reproduces_baseline_governance_signals(self):
        cfg = load_scenario(ROOT / 'configs' / 'hormuz_v25_9_baseline.json')
        result = run_single(cfg)
        gs = result['governance_signals']
        self.assertTrue(math.isclose(result['peak_stress'], 0.7978167899148008, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(gs['epistemic_integrity_proxy'], 0.2530525370312938, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(gs['decision_friction_proxy'], 0.4751743814347482, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(gs['platform_dependency_proxy'], 0.0, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(gs['mosaic_response_proxy'], 0.8400201657921639, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(gs['governance_erosion_score'], 0.5232946766903576, rel_tol=0.0, abs_tol=1e-15))

    def test_compare_reproduces_documented_governance_comparison(self):
        left = load_scenario(ROOT / 'configs' / 'governance_high_friction.json')
        right = load_scenario(ROOT / 'configs' / 'governance_frictionless.json')
        comp = compare_runs(left, right, 'high_friction', 'frictionless')
        c = comp['comparison']
        self.assertTrue(math.isclose(c['high_friction']['decision_friction_proxy'], 0.4751743814347482, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['frictionless']['decision_friction_proxy'], 0.4464707461464616, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['high_friction']['governance_erosion_score'], 0.5607946766903575, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['frictionless']['governance_erosion_score'], 0.6932987904004633, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['delta']['peak_stress'], 0.0021553779826809505, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['delta']['governance_erosion_score'], 0.13250411371010573, rel_tol=0.0, abs_tol=1e-15))
        self.assertTrue(math.isclose(c['delta']['platform_dependency_proxy'], 0.5, rel_tol=0.0, abs_tol=1e-15))

    def test_all_public_configs_load_and_proxies_are_bounded(self):
        for path in sorted((ROOT / 'configs').glob('*.json')):
            cfg = load_scenario(path)
            result = run_single(cfg)
            self.assertGreaterEqual(result['peak_stress'], 0.0, path.name)
            self.assertLessEqual(result['peak_stress'], 1.0, path.name)
            gs = result['governance_signals']
            for key in ['epistemic_integrity_proxy', 'decision_friction_proxy', 'platform_dependency_proxy', 'mosaic_response_proxy', 'governance_erosion_score']:
                self.assertGreaterEqual(gs[key], 0.0, f"{path.name}:{key}")
                self.assertLessEqual(gs[key], 1.0, f"{path.name}:{key}")


if __name__ == '__main__':
    unittest.main()
