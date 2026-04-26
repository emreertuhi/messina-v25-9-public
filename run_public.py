#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from public_safe.scenario_loader import load_scenario
from public_safe.public_runner import run_single, compare_runs
from public_safe.report_writer import write_json, write_single_run_report, write_compare_summary


def cmd_single(args: argparse.Namespace) -> int:
    cfg = load_scenario(args.config)
    result = run_single(cfg)
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    write_json(outdir / "governance_signals.json", result["governance_signals"])
    write_json(outdir / "single_run.json", result)
    write_single_run_report(outdir / "full_run_report.md", result["scenario_name"], result["description"], result["peak_stress"], result["governance_signals"])
    print(f"Wrote single-run outputs to {outdir}")
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    left = load_scenario(args.left)
    right = load_scenario(args.right)
    result = compare_runs(left, right, args.left_label, args.right_label)
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    write_json(outdir / "comparison.json", result)
    write_compare_summary(outdir / "summary.md", args.left_label, args.right_label, result)
    print(f"Wrote comparison outputs to {outdir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Public-safe MESSINA runner for v25.9 governance diagnostics.")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("single", help="Run one public-safe scenario config.")
    s.add_argument("--config", required=True)
    s.add_argument("--out", required=True)
    s.set_defaults(func=cmd_single)

    c = sub.add_parser("compare", help="Compare two public-safe scenario configs.")
    c.add_argument("--left", required=True)
    c.add_argument("--right", required=True)
    c.add_argument("--left-label", default="high_friction")
    c.add_argument("--right-label", default="frictionless")
    c.add_argument("--out", required=True)
    c.set_defaults(func=cmd_compare)
    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
