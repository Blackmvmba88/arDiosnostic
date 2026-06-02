# arDiosnostic

**AR-assisted PCB and motherboard diagnostics.**

arDiosnostic is a bench-first diagnostic platform for electronics repair. It combines computer vision, board profiles, guided measurements, and later augmented reality to help technicians inspect, compare, measure, and confirm faults on PCBs and motherboards.

> Philosophy: **Measure → Compare → Locate → Suggest → Confirm**

The first goal is not magic AI diagnosis. The first goal is a reliable workshop tool that produces evidence.

---

## Product Positioning

Do not sell this as:

```txt
AI that repairs motherboards automatically
```

Sell it as:

```txt
Visual board diff + measurement assistant for PCB repair.
```

---

## Bench MVP

The MVP intentionally avoids live AR, full AI diagnosis, and oscilloscope-level analysis at the beginning.

### MVP Scope

```txt
1. Load healthy board image
2. Load damaged board image
3. Align both images
4. Detect visual differences
5. Mark suspicious zones
6. Attach manual component/test-point metadata
7. Read basic voltage/current measurements
8. Generate a JSON/PNG report
```

### Evidence Sources

arDiosnostic should never diagnose without evidence. A suggestion must be backed by at least one of:

- visual difference
- electrical measurement
- board profile data
- repair history
- thermal evidence

---

## Core Features

### 1. Visual Board Diff

Compare a known-good board image against a suspect board image.

Detects:

- missing components
- moved components
- burnt zones
- lifted pads
- solder irregularities
- revision differences

### 2. Board Profile JSON

A board profile stores component positions, rails, test points, expected voltages, and metadata.

### 3. Static Overlay

Before live AR, the system draws labels and warnings on a still image:

```txt
[TP1 3.3V]    [C245 suspicious]
[U3 PMIC]     [PP3V3 rail]
```

### 4. Measurement Assistant

Initial measurement support:

- DC voltage
- DC current
- continuity / low impedance checks
- basic digital HIGH/LOW activity

Oscilloscope-level ripple, PWM, clocks, and buses are future features.

### 5. Rule-Based Diagnostics

Diagnosis starts as structured rules, not vague AI responses.

Example:

```json
{
  "rule_id": "short_on_rail_01",
  "condition": {
    "rail": "PP3V3_G3H",
    "measured_voltage": {"lt": 0.5},
    "current": {"gt": 0.3}
  },
  "action": {
    "diagnosis": "possible_short",
    "next_step": "inject_limited_current",
    "priority": 1
  }
}
```

---

## Repository Structure

```txt
arDiosnostic/
├── apps/
│   └── web/
├── core/
│   ├── vision/
│   ├── diagnostics/
│   ├── measurements/
│   └── board_db/
├── data/
│   └── boards/
│       └── demo_board_001/
├── docs/
├── tools/
├── requirements.txt
├── ROADMAP.md
└── README.md
```

---

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run a visual diff demo:

```bash
python -m core.vision.diff \
  --reference data/boards/demo_board_001/reference_top.png \
  --candidate data/boards/demo_board_001/candidate_top.png \
  --out reports/demo_diff.png
```

Read a hardware probe:

```bash
python -m core.measurements.serial_reader --port auto
```

Windows example:

```bash
python -m core.measurements.serial_reader --port COM3
```

macOS/Linux example:

```bash
python -m core.measurements.serial_reader --port /dev/ttyUSB0
```

---

## Safety

This project can interact with powered electronics. Use strict safety practices:

- do not inject voltage without current limit
- discharge large capacitors before probing
- avoid measuring high voltage without isolation
- do not use liquid nitrogen in MVP workflows
- avoid condensation on energized boards
- use ESD protection
- treat in-circuit resistance readings as unreliable unless confirmed

---

## Long-Term Vision

The full platform may later include:

- mobile AR overlay
- thermal hotspot detection
- repair history intelligence
- continuity assistant
- OpenBoardView export
- oscilloscope bridge
- collaborative board profile database
- training mode for technicians

---

## Slogan

```txt
No adivina.
Mide.
Compara.
Localiza.
Confirma.
```
