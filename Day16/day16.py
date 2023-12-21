import numpy as np


def switch(symbol, direction):
    match (symbol, direction):
        case ("/", _):
            return [list(np.multiply(np.flip(direction), -1))]
        case ("\\", _):
            return [list(np.flip(direction))]
        case ("|", [0, 1]) | ("|", [0, -1]):
            return [[1, 0], [-1, 0]]
        case ("-", [1, 0]) | ("-", [-1, 0]):
            return [[0, 1], [0, -1]]
        case (_, _):
            return [direction]


def path(data, start_position, start_direction):
    # (position, direction)
    beams = [(start_position, start_direction)]
    loop = []
    visited = []

    while beams:
        beam = beams.pop(0)
        if beam in loop:
            continue
        loop.append(beam)
        if beam[0] not in visited:
            visited.append(beam[0])

        directions = switch(data[beam[0][0]][beam[0][1]], beam[1])
        for direction in directions:
            new_position = list(np.array(beam[0]) + np.array(direction))
            if -1 in new_position or new_position[0] > len(data) - 1 or new_position[1] > len(data[0]) - 1:
                continue
            beams.append((new_position, direction))
    return len(visited)


def main():
    with open("input.txt", "r") as input_file:
        data = [list(line.strip()) for line in input_file]

    part1 = path(data, [0, 0], [0, 1])

    # brute force ¯\_(ツ)_/¯
    part2 = []
    for row in range(len(data)):
        part2.append(path(data, [row, 0], [0, 1]))
        part2.append(path(data, [row, len(data[0])-1], [0, -1]))
    for col in range(1, len(data[0])-1):
        part2.append(path(data, [0, col], [1, 0]))
        part2.append(path(data, [len(data)-1, col], [-1, 0]))

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {max(part2)}")


if __name__ == "__main__":
    main()
