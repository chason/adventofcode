import fileinput


class FreqCalc:
    def __init__(self, start: int=0):
        self._changes = [start]

    def append(self, nv: int):
        self._changes.append(nv)

    @property
    def value(self):
        return sum(self._changes)


if __name__ == "__main__":
    calc = FreqCalc()
    for line in fileinput.input():
        calc.append(int(line))
    print(calc.value)
