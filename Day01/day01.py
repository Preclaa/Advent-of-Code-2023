import re

if __name__ == "__main__":
    part1 = part2 = 0
    with open("input.txt", "r") as input:
        for line in input:
            numbers = ''.join(re.findall(r'\d+', line))
            part1 += int(numbers[0] + numbers[-1])

            digits = ["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine"]

            for i in range(2, len(line)):
                for j, digit in enumerate(digits):
                    replaced = line[:i].replace(
                        digit, str(j+1) + digit[-1]) + line[i:]
                    if replaced != line:
                        line = replaced
                        i -= len(digit) + 3
                        break

            numbers = ''.join(re.findall(r'\d+', line))
            part2 += int(numbers[0] + numbers[-1])

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
