# Roadmap — arDiosnostic

This roadmap prioritizes a useful bench tool before advanced AR or AI.

---

## M0 — Repository Foundation

Status: in progress

```txt
[ ] README
[ ] ROADMAP
[ ] docs/safety.md
[ ] docs/board-profile-format.md
[ ] demo board profile
[ ] basic Python modules
```

---

## M1 — Board Profile MVP

Goal: represent one board in a clean, extensible JSON format.

```txt
[ ] Choose first demo board
[ ] Add reference top image
[ ] Add candidate/suspect image
[ ] Map 10 components manually
[ ] Map 3 rails
[ ] Map 5 test points
[ ] Add expected voltage values
```

Deliverable:

```txt
data/boards/demo_board_001/board_profile.json
```

---

## M2 — Image Diff Engine

Goal: compare a healthy board image with a suspect image.

```txt
[ ] Load two images
[ ] Resize/normalize
[ ] Align images
[ ] Compute difference mask
[ ] Filter noise
[ ] Draw bounding boxes
[ ] Export PNG report
[ ] Export JSON report
```

Output example:

```json
{
  "regions": [
    {
      "x": 302,
      "y": 180,
      "w": 32,
      "h": 18,
      "confidence": 0.76,
      "reason": "visual_difference"
    }
  ]
}
```

---

## M3 — Manual Component Mapper

Goal: create board metadata without needing automatic recognition.

```txt
[ ] Click component on image
[ ] Add refdes: C1, R1, U1
[ ] Add type
[ ] Add value/package
[ ] Add rail/net
[ ] Save to board profile
```

---

## M4 — Static Overlay

Goal: draw labels on still board images.

```txt
[ ] Load board profile
[ ] Draw components
[ ] Draw test points
[ ] Highlight failed rails
[ ] Highlight suspicious regions
[ ] Export annotated image
```

---

## M5 — Hardware Probe Reader

Goal: read basic measurements from an external probe.

Supported initially:

```txt
- voltage DC
- current DC
- continuity / low impedance
- basic HIGH/LOW activity
```

```txt
[ ] Serial reader
[ ] Auto port detection
[ ] JSON packet parser
[ ] Measurement logging
[ ] Calibration config
```

Expected packet:

```json
{
  "probe_id": "ardiosnostic-probe-01",
  "mode": "voltage",
  "value": 3.28,
  "unit": "V",
  "timestamp": 1710000000
}
```

---

## M6 — Diagnostic Rules Engine

Goal: use data-driven rules for repeatable suggestions.

```txt
[ ] Load rules JSON
[ ] Match measurement conditions
[ ] Produce diagnosis candidates
[ ] Include evidence
[ ] Include next step
[ ] Include confidence/priority
```

---

## M7 — Report Generator

Goal: generate repair evidence.

```txt
[ ] Board info
[ ] Images
[ ] Diff regions
[ ] Measurements
[ ] Failed rails
[ ] Suspected components
[ ] Next steps
[ ] Export JSON
[ ] Export HTML/PDF later
```

---

## M8 — Thermal Assist

Goal: detect likely hotspots.

Initial low-cost mode:

```txt
- isopropyl alcohol evaporation visible through camera
- freeze spray visual assist
- manual hotspot annotation
```

Later:

```txt
- MLX90640 support
- USB thermal camera support
- thermal-to-component mapping
```

---

## M9 — Continuity Assistant

Goal: help build board profiles without boardview files.

```txt
[ ] Ask user to place probe A
[ ] Ask user to place probe B
[ ] Record continuity yes/no
[ ] Group points into nets
[ ] Export discovered nets
```

---

## M10 — Revision Diff

Goal: compare board revisions.

```txt
[ ] Load two board profiles
[ ] Show component changes
[ ] Show rail/test-point differences
[ ] Mark optional/not-populated components
```

---

## M11 — Live AR Overlay

Goal: camera-based live overlay.

```txt
[ ] Detect board in camera
[ ] Compute homography
[ ] Track orientation
[ ] Project board profile coordinates
[ ] Show components/test points live
```

---

## M12 — Oscilloscope Bridge

Goal: integrate real scope data.

Not an ESP32/ADS1115 feature. This requires either external scope integration or dedicated analog frontend.

```txt
[ ] USB scope bridge
[ ] CSV waveform import
[ ] Ripple analysis
[ ] PWM detection
[ ] Clock presence checks
```

---

## Build Order

```txt
M0 → M1 → M2 → M4 → M5 → M6 → M7
```

Only after that:

```txt
Thermal → Continuity → AR → Scope Bridge
```
