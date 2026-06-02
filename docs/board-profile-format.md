# Board Profile Format

A board profile describes the physical and electrical map of a PCB.

## File Location

```txt
data/boards/<board_id>/board_profile.json
```

## Minimal Schema

```json
{
  "board_id": "demo_board_001",
  "name": "Demo Board",
  "revision": "A",
  "units": "px",
  "scale_mm_per_px": null,
  "images": {
    "top": "reference_top.png",
    "bottom": "reference_bottom.png"
  },
  "components": [],
  "rails": [],
  "test_points": [],
  "repair_history": []
}
```

## Component Object

```json
{
  "ref": "C245",
  "type": "capacitor",
  "value": "10uF",
  "package": "0603",
  "x": 420.2,
  "y": 180.6,
  "rotation": 90,
  "net": "PP3V3_G3H",
  "optional": false
}
```

## Rail Object

```json
{
  "name": "PP3V3_G3H",
  "expected_voltage": 3.3,
  "tolerance_percent": 10,
  "max_current": 0.5,
  "test_points": ["TP1", "TP2"]
}
```

## Test Point Object

```json
{
  "id": "TP1",
  "x": 120.5,
  "y": 80.1,
  "rail": "PP3V3_G3H",
  "expected_voltage": 3.3,
  "notes": "standby rail"
}
```

## Repair History Object

```json
{
  "date": "2026-06-02",
  "symptom": "no_power",
  "diagnosis": "shorted C245 on PP3V3_G3H",
  "fix": "replaced C245",
  "confidence": "confirmed"
}
```

## Scale Calibration

If `scale_mm_per_px` is unknown, leave it as `null`.

Recommended calibration methods:

- known board dimension
- known component package size, for example 0603 = approximately 1.6 mm x 0.8 mm
- fiducial distance
- ruler in photo

## Optional Components

Many PCBs have unpopulated footprints by design. Mark them explicitly:

```json
"optional": true
```

This prevents false missing-component alerts.
