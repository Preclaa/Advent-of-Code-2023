def expand(sequence, backwards=False):
    while sum(sequence[-1]) != 0:
        diff = [sequence[-1][i+1] - sequence[-1][i]
                for i in range(len(sequence[-1])-1)]
        sequence.append(diff)
    for i in range(len(sequence)-1):
        if backwards:
            index = 0
            value = sequence[-2-i][0] - sequence[-1-i][0]
        else:
            index = len(sequence[-2-i])
            value = sequence[-2-i][-1] + sequence[-1-i][-1]
        sequence[-2-i].insert(index, value)
    return sequence[0][0] if backwards else sequence[0][-1]


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]

    oasis = [[int(number) for number in line.split()] for line in lines]
    next_values = [expand([sequence.copy()]) for sequence in oasis]
    previous_values = [expand([sequence.copy()], True) for sequence in oasis]

    print(f"Part 1 answer: {sum(next_values)}")
    print(f"Part 2 answer: {sum(previous_values)}")
