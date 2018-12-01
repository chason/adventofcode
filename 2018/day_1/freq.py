import fileinput
from itertools import cycle


class FreqCalc:
    def __init__(self):
        self._changes = [0]

    def append(self, nv: int):
        self._changes.append(nv)

    @property
    def value(self):
        return sum(self._changes)

    @property
    def first_double(self):
        cv, changes = self._changes[0], self._changes[1:]
        seen = set([cv])
        for n in cycle(changes):
            cv += n
            if cv in seen:
                return cv
            seen.add(cv)

if __name__ == "__main__":
    calc = FreqCalc()
    for line in fileinput.input():
        calc.append(int(line))
    print(calc.value)
    print(calc.first_double)
