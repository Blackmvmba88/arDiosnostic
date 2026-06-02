# Safety Guidelines

arDiosnostic is intended for electronics repair assistance. It must not encourage unsafe probing, uncontrolled injection, or high-voltage work without proper equipment.

## Core Rules

```txt
No uncontrolled power injection.
No high-voltage probing without isolation.
No liquid nitrogen workflows in MVP.
No blind diagnosis without evidence.
```

## Electrical Safety

- Use a current-limited bench supply when injecting voltage.
- Start with low voltage and low current limits.
- Never inject voltage into an unknown rail without identifying likely voltage domain.
- Discharge large capacitors before measuring resistance or continuity.
- Use isolated equipment when working near mains or primary-side power supplies.
- Avoid connecting USB-grounded devices to unknown high-energy circuits.

## ESD Safety

- Use an ESD mat and wrist strap when possible.
- Avoid touching exposed BGA/IC pins directly.
- Store boards in ESD-safe bags.

## Thermal / Cooling Safety

Safe early techniques:

- visible inspection
- thermal camera
- isopropyl alcohol evaporation observation
- electronics-grade freeze spray

Avoid in MVP:

- liquid nitrogen
- aggressive cooling of powered boards
- creating condensation on energized boards

## Measurement Notes

In-circuit resistance measurements are often misleading because parallel components affect readings. Treat them as clues, not final proof.

Recommended evidence hierarchy:

```txt
visual evidence + electrical measurement + board profile + thermal behavior + confirmation after repair
```

## Software Responsibility

The app should prefer language like:

```txt
possible short
suspected component
recommended next measurement
```

Avoid unsupported language like:

```txt
definitely broken
replace this now
confirmed failure
```

unless the user explicitly confirms the repair result.
