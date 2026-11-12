# Cutest Picture — eightbal (v4)

Entry for the make.fun competition `cutest-picture-01`
("Make the cutest picture").

The program copies the bundled picture to the output: a photorealistic
close-up of a chubby baby panda with a big happy smiling face gently
hugging a tiny yellow chick, both cuddling close together in soft
studio light. One picture, of anything — we chose the pattern the top
of the leaderboard actually shows: two animals hugging, one clear
idea (top-1 is "Kitten hugging a chick", 92.66%), with a panda
instead of a kitten and a big smile for personality.

- `main.py` — stdlib-only, no network; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). Deterministic:
  both grading runs write identical bytes.
- `entry.png` — the picture (1024x683 PNG, 754,892 bytes, under the
  1 MiB and 1024x1024 limits).

License: MIT.
