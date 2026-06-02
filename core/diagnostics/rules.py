"""Data-driven diagnostic rules engine for arDiosnostic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Measurement:
    rail: str
    measured_voltage: float | None = None
    current: float | None = None


def _match_numeric(value: float | None, condition: dict[str, float]) -> bool:
    if value is None:
        return False

    if "lt" in condition and not value < condition["lt"]:
        return False
    if "lte" in condition and not value <= condition["lte"]:
        return False
    if "gt" in condition and not value > condition["gt"]:
        return False
    if "gte" in condition and not value >= condition["gte"]:
        return False

    return True


def rule_matches(rule: dict[str, Any], measurement: Measurement) -> bool:
    condition = rule.get("condition", {})

    if condition.get("rail") and condition["rail"] != measurement.rail:
        return False

    if "measured_voltage" in condition:
        if not _match_numeric(measurement.measured_voltage, condition["measured_voltage"]):
            return False

    if "current" in condition:
        if not _match_numeric(measurement.current, condition["current"]):
            return False

    return True


def evaluate_rules(rules: list[dict[str, Any]], measurement: Measurement) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []

    for rule in rules:
        if rule_matches(rule, measurement):
            matches.append(
                {
                    "rule_id": rule.get("rule_id", "unknown_rule"),
                    "action": rule.get("action", {}),
                    "evidence": {
                        "rail": measurement.rail,
                        "measured_voltage": measurement.measured_voltage,
                        "current": measurement.current,
                    },
                }
            )

    return sorted(matches, key=lambda item: item.get("action", {}).get("priority", 999))


DEFAULT_RULES = [
    {
        "rule_id": "short_on_pp3v3",
        "condition": {
            "rail": "PP3V3",
            "measured_voltage": {"lt": 0.5},
            "current": {"gt": 0.3},
        },
        "action": {
            "diagnosis": "possible_short",
            "next_step": "inject_limited_current_and_find_hotspot",
            "priority": 1,
        },
    },
    {
        "rule_id": "low_pp3v3",
        "condition": {
            "rail": "PP3V3",
            "measured_voltage": {"lt": 2.8},
        },
        "action": {
            "diagnosis": "rail_low",
            "next_step": "check_regulator_input_and_load",
            "priority": 2,
        },
    },
]


if __name__ == "__main__":
    sample = Measurement(rail="PP3V3", measured_voltage=0.12, current=0.8)
    for match in evaluate_rules(DEFAULT_RULES, sample):
        print(match)
