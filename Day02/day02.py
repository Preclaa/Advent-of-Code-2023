import re
import itertools
import numpy as np

if __name__ == "__main__":
    part1 = part2 = 0
    max_values = {"red": 12, "green": 13, "blue": 14}
    with open("input.txt", "r") as input:
        for i, line in enumerate(input, start=1):
            picks = [pick.split()
                     for pick in re.split(r'[;,]', line.split(':')[1])]
            picks.sort(key=lambda x: x[1])

            picks_grouped_color = {key: max(int(
                item[0]) for item in group) for key, group in itertools.groupby(picks, key=lambda x: x[1])}

            if all(picks_grouped_color[key] <= max_values[key] for key in picks_grouped_color):
                part1 += i
            part2 += np.prod(list(picks_grouped_color.values()))

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
