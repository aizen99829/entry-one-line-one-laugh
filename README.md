# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![Rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/aizen99829/entry-one-line-one-laugh/rank.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![Reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/aizen99829/entry-one-line-one-laugh/reward.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)

A one-line joke for the [One Line, One Laugh](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9) bounty on make.fun. One program, one line, one laugh — a robot vacuum hands out life advice the only way it knows how.

## How it works

`main.py` holds a single joke as one string, checks it against the
competition's hard gate (exactly one line, 1–140 characters), then writes
it to `/output/entry.txt`. Nothing else: no network, no randomness, no
dependencies beyond the Python standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is a single line. The program refuses to write anything that
would break the gate, so a failed run means the joke needs trimming,
not the checker.

## License

MIT — see [LICENSE](LICENSE).



