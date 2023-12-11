from scipy.spatial import distance


def offset(value, indexes, expand):
    return len([x for x in indexes if x < value]) * (expand-1)


def calculate_distances(data, expand):
    empty_rows = [i for i, row in enumerate(data) if '#' not in row]
    empty_cols = [i for i, col in enumerate(zip(*data)) if all(cell == '.' for cell in col)]

    galaxies = [(row_id + offset(row_id, empty_rows, expand),
                 col_id + offset(col_id, empty_cols, expand))
                for row_id, row in enumerate(data)
                for col_id, col in enumerate(row) if col == '#']

    distances_between_pairs = [int(distance.cityblock(galaxies[i], galaxies[j]))
                               for i in range(len(galaxies))
                               for j in range(i+1, len(galaxies))]

    return sum(distances_between_pairs)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = [[item for item in line.strip()] for line in input_file]

    print(f"Part 1 answer: {calculate_distances(lines, 2)}")
    print(f"Part 2 answer: {calculate_distances(lines, 1000000)}")
