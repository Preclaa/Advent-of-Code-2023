import numpy as np

if __name__ == "__main__":
    part1 = part2 = 0
    with open("input.txt", "r") as input:
        lines = input.readlines()
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        winning_numbers, owned_numbers = [[int(number) for number in numbers.split()]
                                          for numbers in line.strip().split(':')[1].split('|')]
        intersection = list(set(winning_numbers) & set(owned_numbers))
        part1 += int(2 ** (len(intersection)-1))
        for j in range(len(intersection)):
            cards[i+j+1] += cards[i]
    part2 = np.sum(cards)

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
