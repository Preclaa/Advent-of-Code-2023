import re


def hash(string):
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


def main():
    with open("input.txt", "r") as input_file:
        sequence = input_file.read().strip().split(',')

    part1 = sum(hash(string) for string in sequence)

    boxes = {}
    for string in sequence:
        label = re.split(re.compile(r'[-=]'), string)
        box = hash(label[0])
        if box not in boxes:
            boxes[box] = {}
        if label[1]:
            boxes[box][label[0]] = int(label[1])
        elif label[0] in boxes[box]:
            del boxes[box][label[0]]

    part2 = sum((box + 1) * slot * strength
                for box, labels in boxes.items()
                for slot, strength in enumerate(labels.values(), start=1))

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")


if __name__ == "__main__":
    main()
