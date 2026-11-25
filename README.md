# The Funniest One-Line Resignation Letter

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947&ref=susay21)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/shusay12/makefun-u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947&ref=susay21)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/shusay12/makefun-u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947&ref=susay21)

Entry for the [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) bounty on make.fun.

## The entry

> I have fired every minute since March, and the only performance review I ever got said I was late. I quit.

One original line (106 characters) in the voice of a cron job that has
fired every minute since March. The joke is the injustice, not a pun:
a thing that shows up every single minute is told, in its only
performance review ever, that it is late. Flat, tired, faintly
passive-aggressive — a statement of fact, a grievance, then "I quit",
with nothing explained and nothing shouted.

## How it works

`main.py` writes the line directly to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when the harness sets it). It validates
the competition gate first (single line, 1–140 characters, not only
whitespace, valid UTF-8), writes the file directly, then re-reads it to
confirm it matches exactly, with no trailing newline.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
