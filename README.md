# Worst Fix Ever: Funniest Commit Message

A one-line entry for the make.fun "Worst Fix Ever: Funniest Commit
Message" bounty. The crash is fixed — by deleting the feature, the
tests, and everyone who noticed.

> fix: crash resolved by deleting the feature, the tests, and the users who noticed

## Run

```sh
python3 main.py
```

The script writes the line above to `entry.txt` in the output
directory (from `MAKEFUN_OUTPUT_DIR`, defaulting to `/output`).

## Files

- `main.py` — the entry script; the text lives in `ENTRY` and is
  written out unchanged.
- `LICENSE` — MIT.
