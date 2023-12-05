import re
from collections import defaultdict

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file] + ['']

    seeds = [int(match) for match in re.findall(r'\b\d+\b', lines[0])]
    separators = [index for index, line in enumerate(lines) if line == '']
    maps = [lines[separators[i] + 1:separators[i + 1]] for i in range(len(separators) - 1)]

    maps_dict = defaultdict(list)
    for map in maps:
        maps_dict[tuple(map[0].split()[0].split('-to-'))] = [
            [int(match) for match in re.findall(r'\b\d+\b', line)] for line in map[1:]
        ]

    locations = []
    for seed in seeds:
        source = seed
        for map in maps_dict:
            for _range in maps_dict[map]:
                if _range[1] <= source < _range[1] + _range[2]:
                    source = _range[0] + (source - _range[1])
                    break
        locations.append(source)
    part1 = min(locations)

    ranges = [range(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]
    for location in range(max(_range.stop for _range in ranges)):
        source = location
        for map in reversed(maps_dict):
            for _range in maps_dict[map]:
                if _range[0] <= source < _range[0] + _range[2]:
                    source = _range[1] + (source - _range[0])
                    break
        if any(source in _range for _range in ranges):
            part2 = location
            break

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
    