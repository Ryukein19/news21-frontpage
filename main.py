#!/usr/bin/env python3
"""news-image-20261121 entrypoint.

Stdlib-only. The graded image is shipped in this repo as entry.png
(a 1024x1024 front page rendered from frontpage.html). This program
validates the asset and copies it to /output/entry.png.

Grading env: Python 3.13-slim, no Pillow/fonts, no network, read-only
repo, writable /output, 60 s limit.
"""

import os
import struct
import sys

MAX_BYTES = 1024 * 1024  # 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECT_W, EXPECT_H = 1024, 1024


def png_dimensions(data):
    """Return (width, height) from the PNG IHDR chunk, or None."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        return None
    if data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def find_asset():
    here = os.path.dirname(os.path.abspath(__file__))
    for candidate in (
        os.path.join(here, "entry.png"),
        os.path.join(os.getcwd(), "entry.png"),
    ):
        if os.path.isfile(candidate):
            return candidate
    return None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    asset = find_asset()
    if asset is None:
        print("error: entry.png not found next to main.py or in cwd",
              file=sys.stderr)
        return 1
    with open(asset, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: entry.png is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    dims = png_dimensions(data)
    if dims is None:
        print("error: entry.png has no readable IHDR chunk", file=sys.stderr)
        return 1
    if dims != (EXPECT_W, EXPECT_H):
        print(f"error: entry.png is {dims[0]}x{dims[1]}, "
              f"expected {EXPECT_W}x{EXPECT_H}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)
    print(f"wrote {out_path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
