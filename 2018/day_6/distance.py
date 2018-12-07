import fileinput
import sys
from typing import List, Tuple
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Coords:
    points: List[Tuple[int]]

    @staticmethod
    def _get_md(pos1: Tuple[int], pos2: Tuple[int]) -> int:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def closest_point(self, pos: Tuple[int]) -> int:
        closest = (-1, sys.maxsize)
        for idx, pt in enumerate(self.points):
            d = self._get_md(pos, pt)
            if d < closest[1]:
                closest = (idx, d)
            elif d == closest[1]:
                closest = (-1, d)
        return closest[0]

    @property
    def largest_area(self) -> int:
        candidates = self.points.copy()
        areas = defaultdict(int)
        for x in range(self.min_point[0] - 1, self.max_point[0] + 2):
            for y in range(self.min_point[1] - 1, self.max_point[1] + 2):
                cp = self.closest_point((x, y))
                if cp == -1:
                    continue
                areas[cp] += 1
                if (
                    x < self.min_point[0]
                    or x > self.max_point[0]
                    or y < self.min_point[1]
                    or y > self.max_point[1]
                ):
                    try:
                        candidates.remove(self.points[cp])
                    except ValueError:
                        continue
        max_area = 0
        for candidate in candidates:
            idx = self.points.index(candidate)
            area = areas[idx]
            if area > max_area:
                max_area = area
        return max_area

    def total_point_distance(self, point: Tuple[int]) -> int:
        acc = 0
        for pt in self.points:
            acc += self._get_md(pt, point)
        return acc

    def closest_area(self, max_dist: int) -> int:
        valid_points = 0
        for x in range(self.min_point[0], self.max_point[1]):
            for y in range(self.min_point[1], self.max_point[1]):
                if self.total_point_distance((x, y)) < max_dist:
                    valid_points += 1
        return valid_points

    @property
    def min_point(self) -> Tuple[int]:
        return (min([pt[0] for pt in self.points]), min([pt[1] for pt in self.points]))

    @property
    def max_point(self) -> Tuple[int]:
        return (max([pt[0] for pt in self.points]), max([pt[1] for pt in self.points]))


sample_data = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
test_coords = Coords(sample_data)
try:
    assert test_coords.largest_area == 17
except AssertionError:
    print(test_coords.largest_area)

assert test_coords.total_point_distance((4, 3)) == 30
assert test_coords.closest_area(32) == 16


if __name__ == "__main__":
    coords = [tuple(map(int, coord.strip().split(","))) for coord in fileinput.input()]
    c = Coords(coords)
    print(c.largest_area)
    print(c.closest_area(10000))
