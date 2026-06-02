"""Basic visual board diff engine.

This module compares a reference board image against a candidate board image and
exports an annotated PNG plus a JSON report of suspicious regions.

Usage:
    python -m core.vision.diff --reference ref.png --candidate bad.png --out reports/diff.png
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import numpy as np


def load_image(path: str) -> np.ndarray:
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return image


def resize_to_match(reference: np.ndarray, candidate: np.ndarray) -> np.ndarray:
    height, width = reference.shape[:2]
    return cv2.resize(candidate, (width, height), interpolation=cv2.INTER_AREA)


def compute_diff(reference: np.ndarray, candidate: np.ndarray) -> tuple[np.ndarray, list[dict]]:
    candidate = resize_to_match(reference, candidate)

    ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    cand_gray = cv2.cvtColor(candidate, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(ref_gray, cand_gray)
    blurred = cv2.GaussianBlur(diff, (5, 5), 0)
    _, mask = cv2.threshold(blurred, 35, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regions: list[dict] = []
    annotated = candidate.copy()

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 80:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        confidence = min(0.99, area / 5000.0)

        regions.append(
            {
                "x": int(x),
                "y": int(y),
                "w": int(w),
                "h": int(h),
                "area": float(area),
                "confidence": round(float(confidence), 3),
                "reason": "visual_difference",
            }
        )

        cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            annotated,
            "DIFF",
            (x, max(0, y - 6)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1,
            cv2.LINE_AA,
        )

    return annotated, regions


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two board images.")
    parser.add_argument("--reference", required=True, help="Known-good board image")
    parser.add_argument("--candidate", required=True, help="Suspect board image")
    parser.add_argument("--out", required=True, help="Annotated output image path")
    parser.add_argument("--json-out", default=None, help="Optional JSON report path")
    args = parser.parse_args()

    reference = load_image(args.reference)
    candidate = load_image(args.candidate)
    annotated, regions = compute_diff(reference, candidate)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_path), annotated)

    json_path = Path(args.json_out) if args.json_out else out_path.with_suffix(".json")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps({"regions": regions}, indent=2), encoding="utf-8")

    print(f"Saved annotated diff: {out_path}")
    print(f"Saved JSON report: {json_path}")
    print(f"Detected regions: {len(regions)}")


if __name__ == "__main__":
    main()
