import fileinput
from itertools import chain, islice
import string

test_data = "dabAcCaCBAcCcaDA"
test_result = 10

COMBINATIONS = [''.join([x, y]) for x, y in chain(zip(string.ascii_lowercase, string.ascii_uppercase), zip(string.ascii_uppercase, string.ascii_lowercase))]

def process_string(polymer):
    i = 0
    while i < len(polymer):
        unit_pair = polymer[i:i+2]
        if unit_pair in COMBINATIONS:
            string_left, _, string_right = polymer.partition(unit_pair)
            polymer = ''.join([string_left, string_right])
            i -= 1
        else:
            i += 1
    return len(polymer)

def find_shortest(polymer):
    shortest = len(polymer)
    for letter in string.ascii_lowercase:
        new_candidate = process_string(polymer.replace(letter, '').replace(letter.upper(), ''))
        if new_candidate < shortest:
            shortest = new_candidate
            shortest_letter = '{}/{}'.format(letter.upper(), letter)
    return shortest

try:
    assert process_string(test_data) == test_result
except AssertionError:
    print("Error in string process: {}".format(process_string(test_data)))

try:
    assert find_shortest(test_data) == 4
except AssertionError:
    print("Error in find shortest routine: {}".format(find_shortest(test_data)))

if __name__ == "__main__":
    for line in fileinput.input():
        print(process_string(line.strip()))
        print(find_shortest(line.strip()))
