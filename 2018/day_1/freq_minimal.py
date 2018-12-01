#minimal version with stdlib
import fileinput
from itertools import cycle

freqs = [int(line) for line in fileinput.input()]
print(f"Part 1: {sum(freqs)}")
_seen = set()
_cv = 0
for n in cycle(freqs):
    _cv += n
    if _cv in _seen:
        print(f"Part 1: {_cv}")
        break
    _seen.add(_cv)
