import fileinput
from bisect import bisect
import re
from collections import defaultdict, Counter
from typing import List
from datetime import date, timedelta


class Day:
    _sleeps: List[int] = None
    _wakes: List[int] = None
    guard: str = ""

    def register_sleep(self, minute):
        if self._sleeps is None:
            self._sleeps = []
        self._sleeps.append(minute)
        self._sleeps.sort()

    def register_wake(self, minute):
        if self._wakes is None:
            self._wakes = []
        self._wakes.append(minute)
        self._wakes.sort()

    @property
    def sleep_minutes(self):
        sleep_minutes = []
        if self._wakes is None:
            return []
        for wake_time in self._wakes:
            try:
                sleep_time = self._sleeps[bisect(self._sleeps, wake_time)-1]
            except IndexError:
                import pdb; pdb.set_trace()
            sleep_minutes.extend(range(sleep_time, wake_time))
        return sorted(sleep_minutes)


days = defaultdict(Day)

for line in fileinput.input():
    matches = re.match(r"\[1518-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<log>.+)", line.strip())
    entry = matches.groupdict()
    entry_date = date(year=1518, month=int(entry["month"]), day=int(entry["day"]))
    if entry["hour"] == "23":
        entry_date += timedelta(days=1)
    day = days[entry_date]
    if entry["log"].startswith("Guard #"):
        day.guard = int(entry["log"].split()[1][1:])
    elif entry["log"] == "falls asleep":
        day.register_sleep(int(entry["minute"]))
    elif entry["log"] == "wakes up":
        day.register_wake(int(entry["minute"]))


guards = defaultdict(Counter)
sleepiest_guard = None
most_sleepy_minute = None
for _, entry in days.items():
    guards[entry.guard].update(entry.sleep_minutes)
    total_sleep = sum(guards[entry.guard].values())
    if most_sleepy_minute is None:
        most_sleepy_minute = entry.guard
    elif guards[entry.guard] and guards[entry.guard].most_common(1)[0][1] > guards[most_sleepy_minute].most_common(1)[0][1]:
        most_sleepy_minute = entry.guard
    if total_sleep > sum(guards[sleepiest_guard].values()):
        try:
            sleepiest_guard = entry.guard
        except ValueError:
            import pdb; pdb.set_trace()

print(sleepiest_guard * guards[sleepiest_guard].most_common(1)[0][0])
print(most_sleepy_minute * guards[most_sleepy_minute].most_common(1)[0][0])
