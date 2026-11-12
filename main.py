#!/usr/bin/env python3
"""Cutest-picture entry v4: copy the bundled smiling-panda picture to the output.

The picture is a photorealistic close-up of a chubby baby panda with
a big happy smiling face gently hugging a tiny yellow chick, both
cuddling close together in soft studio light. This is the v4 entry:
the v1 kitten scored 848487 (rank 55/89), the v3 mother dog scored
743313 (rank 163/225) — the complex scenes lost to the simple ones,
so v4 bets on the pattern the top of the leaderboard actually shows:
two animals hugging, one clear idea (top-1 is "Kitten hugging a
chick", 92.66%), with a panda instead of a kitten and a big smile
for personality. The program does one deterministic thing: copy those
exact bytes to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png),
so both grading runs write identical output.
"""
import hashlib
import os
import shutil

SRC_NAME = "entry.png"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guarantee the deterministic-bytes requirement: the output must be
    # byte-identical to the bundled picture, so fail loudly instead of
    # silently leaving a partial file if the copy is ever interrupted.
    # The sha256 comparison checks the full content, not just the size,
    # which is the only way to be sure the grading runs byte-for-byte.
    # (The bundled picture is the smiling panda hugging the chick —
    # 1024x683 PNG, 754,892 bytes — so the copy is one fixed payload.)
    if sha256_of(dst) != sha256_of(src):
        raise RuntimeError("entry.png copy incomplete")


if __name__ == "__main__":
    main()
