def roll(rows):
    return ['#'.join(['O' * group.count('O') + '.' * group.count('.')
                      for group in row.split('#')]) for row in rows]


def roll_north(rows):
    rows = [''.join(x) for x in zip(*rows)]
    rows = roll(rows)
    rows = [''.join(x) for x in zip(*rows)]
    return rows


def roll_west(rows):
    rows = roll(rows)
    return rows


def roll_south(rows):
    rows = list(reversed(rows))
    rows = [''.join(x) for x in zip(*rows)]
    rows = roll(rows)
    rows = [''.join(x) for x in zip(*rows)]
    rows = list(reversed(rows))
    return rows


def roll_east(rows):
    rows = [''.join(x[::-1]) for x in rows]
    rows = roll(rows)
    rows = [''.join(x[::-1]) for x in rows]
    return rows


def cycle(rows):
    rows = roll_north(rows)
    rows = roll_west(rows)
    rows = roll_south(rows)
    rows = roll_east(rows)
    return rows


def count_load(rows):
    return sum(row.count('O') * (len(rows) - i) for i, row in enumerate(rows))


def main():
    with open("input.txt", "r") as input_file:
        rows = [line.strip() for line in input_file]

    part1 = count_load(roll_north(rows))

    cycles = 1000000000
    history = [rows]
    for i in range(cycles):
        rows = cycle(rows)
        if rows in history:
            loop_start = history.index(rows)
            loop_size = i - history.index(rows) + 1
            break
        else:
            history.append(rows)

    for i in range((cycles - loop_start) % loop_size):
        rows = cycle(rows)
    part2 = count_load(rows)

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")


if __name__ == "__main__":
    main()
