"""Serial probe reader for arDiosnostic.

Expected probe packet format, one JSON object per line:

{
  "probe_id": "ardiosnostic-probe-01",
  "mode": "voltage",
  "value": 3.28,
  "unit": "V",
  "timestamp": 1710000000
}
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Iterable

import serial
from serial.tools import list_ports


def find_port() -> str | None:
    ports = list(list_ports.comports())
    if not ports:
        return None
    return ports[0].device


def read_packets(port: str, baud: int = 115200) -> Iterable[dict]:
    with serial.Serial(port, baudrate=baud, timeout=1) as ser:
        while True:
            line = ser.readline().decode("utf-8", errors="replace").strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                yield {"error": "invalid_json", "raw": line}


def main() -> None:
    parser = argparse.ArgumentParser(description="Read JSON packets from an arDiosnostic probe.")
    parser.add_argument("--port", default="auto", help="Serial port, e.g. COM3 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=115200)
    args = parser.parse_args()

    port = find_port() if args.port == "auto" else args.port
    if not port:
        print("No serial port found.", file=sys.stderr)
        raise SystemExit(1)

    print(f"Reading probe packets from {port} at {args.baud} baud...")
    for packet in read_packets(port, args.baud):
        print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
