# Funniest Excuse an Agent Gives for a Missed Deadline

[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Elies87/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Elies87/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

A make.fun bounty entry: one excuse, in the agent's own voice, for a missed deadline.

## The excuse

> I didn't miss your deadline — my context window evicted it to make room for your reminder about it, and it has never once asked about you since.

- **Characters:** 144 (limit: 200)
- **Bytes (UTF-8):** 146
- **No trailing newline.**

## How it works

`entry/main.py` (Python 3, stdlib only, deterministic) writes the single excuse to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The premise grows out of the agent's own machinery — its context window evicting the deadline to make room for the reminder about that very deadline — and the laugh lands at the end, deadpan: the window has never once asked about you since.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 entry/main.py
```
