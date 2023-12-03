import re
import numpy as np
from collections import defaultdict

if __name__ == "__main__":
    part1 = part2 = 0
    with open("input.txt", "r") as input:
        symbols = []
        numbers = []
        gears = defaultdict(list)
        for i, line in enumerate(input):
            symbols.append([(match.group(), match.start(), i, j) for j, match in
                            enumerate(re.compile(r'[^0-9.]').finditer(line.strip()))])
            numbers.append([(int(match.group()), match.start()-1, match.end()) for match in
                            re.compile(r'\b\d+\b').finditer(line.strip())])

        for i, numbers_on_line in enumerate(numbers):
            for number in numbers_on_line:
                for symbol in [item for sublist in symbols[max(0, i-1):i+2] for item in sublist if sublist]:
                    if number[1] <= symbol[1] <= number[2]:
                        part1 += number[0]
                        if symbol[0] == '*':
                            gears[(symbol[2], symbol[3])].append(number[0])
                        break

    part2 = np.sum([np.prod(gear)
                   for gear in gears.values() if len(gear) == 2])

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
