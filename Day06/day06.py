import re
import numpy as np

if __name__ == "__main__":

    with open("input.txt", "r") as input_file:
        races = [list(map(int, re.findall(r'\b\d+\b', line))) for line in input_file] # parse numbers
        races = [numbers + [int(''.join(map(str, numbers)))] for numbers in races] # concatenate numbers and append
        races = list(zip(*races)) # zip time and distance

    records_broken = [sum(((race[0]-time)*time) > race[1] for time in range(race[0])) for race in races]

    print(f"Part 1 answer: {np.prod(records_broken[:-1])}")
    print(f"Part 2 answer: {records_broken[-1]}")
