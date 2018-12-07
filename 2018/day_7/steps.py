import fileinput
from typing import List, Dict, Set
from collections import deque, defaultdict
from bisect import insort
import string


def create_graph(data: List[str]) -> Dict[str, Set[str]]:
    result = defaultdict(set)
    for step in data:
        _, pre, _, _, _, _, _, post, _, _ = step.split()
        result[pre] = {*result[pre]}
        result[post] = {*result[post], pre}
    return result

def process_graph(graph: Dict[str, Set[str]]) -> str:
    visited = set()
    result = ''
    stack = deque(sorted(filter(lambda n: not graph[n], graph.keys()), reverse=True))
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result += vertex
            stack.extend(sorted(filter(lambda n: not (graph[n] - visited), set(graph.keys()) - visited), reverse=True))
    return result

def workers(graph: Dict[str, Set[str]], workers: int, offset: int) -> int:
    visited = set()
    time_passed = offset
    stack = deque(sorted(filter(lambda n: not graph[n], graph.keys()), reverse=True))
    workers_busy = [0] * workers
    workers_job = [''] * workers
    while len(visited) < len(graph.keys()):
        for worker in range(workers):
            if workers_busy[worker]:
                workers_busy[worker] -= 1
            else:
                if workers_job[worker]:
                    visited.add(workers_job[worker])
                    stack.extend(sorted(filter(lambda n: not (graph[n] - visited), set(graph.keys()) - visited), reverse=True))
                    workers_job[worker] = ''
                if stack:
                    vertex = stack.pop()
                    if vertex not in visited and vertex not in workers_job:
                        workers_busy[worker] = string.ascii_uppercase.index(vertex)
                        workers_job[worker] = vertex
        time_passed += 1
    return time_passed - 1
                        

test_data = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
]

graph = create_graph(test_data)
answer = process_graph(graph)
try:
    assert answer == "CABDFE"
except AssertionError:
    print(answer)
seconds = workers(graph, 2, 0)
try:
    assert seconds == 15
except AssertionError:
    print(seconds)


if __name__ == "__main__":
    data = [line.strip() for line in fileinput.input()]
    graph = create_graph(data)
    print(process_graph(graph))
    print(workers(graph, 5, 60))
