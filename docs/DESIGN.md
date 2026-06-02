# arDiosnostic Design System

## Product Identity

**arDiosnostic** is a bench-first diagnostic platform for PCB and motherboard repair.

It should feel like a serious engineering tool, not a toy AI demo.

## Design Principles

1. **Evidence first**  
   Every visual alert must be connected to a measurable reason.

2. **Technician friendly**  
   The interface should support fast inspection at a workbench.

3. **Low noise**  
   Do not overload the user with fake confidence or decorative UI.

4. **Traceable output**  
   Every report should explain what was seen, measured, compared, and suggested.

5. **AR later, reliability first**  
   Static image overlays come before live augmented reality.

## Visual Language

### Mood

- dark lab interface
- high contrast inspection overlays
- precise component labels
- warning zones in clear bounding boxes
- repair-bench seriousness

### Keywords

- diagnostic
- evidence
- voltage rail
- board map
- probe path
- suspicious zone
- technician workflow

## Suggested Palette

```txt
Background:      #0B0F14
Panel:           #111827
Grid:            #1F2937
Text:            #E5E7EB
Muted Text:      #9CA3AF
Signal Green:    #22C55E
Warning Yellow:  #FACC15
Danger Red:      #EF4444
Probe Blue:      #38BDF8
AR Violet:       #8B5CF6
```

## Typography

Use a technical sans-serif for UI and a monospaced font for measurements.

Recommended:

- Inter / system-ui for UI
- JetBrains Mono / SF Mono for readings

## Dashboard Layout

```txt
┌────────────────────────────────────────────────────────────┐
│ arDiosnostic                                                │
│ Measure → Compare → Locate → Confirm                       │
├───────────────┬────────────────────────────┬───────────────┤
│ Board Profile │ Visual Diff Viewer          │ Evidence Log  │
│               │                            │               │
│ Rails         │ [Reference / Candidate]     │ Measurements  │
│ Components    │ [Overlay / Suspicious Zone] │ Rules Fired   │
│ Test Points   │                            │ Next Steps    │
├───────────────┴────────────────────────────┴───────────────┤
│ Report: export JSON / PNG / PDF                             │
└────────────────────────────────────────────────────────────┘
```

## Core Screens

### 1. Board Intake

- load reference image
- load suspect image
- select board profile
- choose board side: top / bottom

### 2. Visual Diff

- aligned board view
- highlighted suspicious zones
- component label overlay
- confidence indicator based on evidence count

### 3. Measurement Session

- guided test point list
- expected voltage
- measured voltage
- pass/fail status
- notes

### 4. Diagnostic Report

- board metadata
- image evidence
- measurement evidence
- fired rules
- suggested next steps
- safety warnings

## UX Rule

Never show diagnosis as absolute truth.

Use:

```txt
Possible short on PP3V3 rail.
Evidence: measured 0.12V, current draw 0.48A, thermal hotspot near C245.
Next step: current-limited injection and localized thermal inspection.
```

Avoid:

```txt
C245 is bad.
```

## Brand Line

```txt
No adivina. Mide. Compara. Localiza. Confirma.
```
