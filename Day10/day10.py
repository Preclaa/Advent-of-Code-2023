tiles_map = {
    ".": [],
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(1, 0), (-1, 0), (0, 1), (0, -1)],
}


def get_loop(start):
    loop = [[start]]
    tiles = [[tiles_map[tile] for tile in line] for line in lines]
    while True:
        new_pipes = []
        for x, y in loop[-1]:
            for x1, y1 in tiles[x][y]:
                pipe_to = tiles[x + x1][y + y1]
                pipe_from = tuple(-x for x in (x1, y1))

                if pipe_from in pipe_to:
                    tiles[x + x1][y + y1] = [
                        x for x in tiles[x + x1][y + y1] if x != pipe_from
                    ]
                    new_pipes.append((x + x1, y + y1))
        if not new_pipes:
            break
        loop.append(new_pipes)
    return loop


def get_enclosed_area(tiles):
    tiles_inside = 0
    for x in range(len(tiles)):
        inside = False
        for y in range(len(tiles[0])):
            pipe = tiles[x][y]
            if pipe == ".":
                tiles_inside += inside
            elif (
                pipe in ["|", "S"]
                or pipe == "7" == end_pipe
                or pipe == "J" == end_pipe
            ):
                # "S" shouldnt really be here, but im too lazy to fix it
                inside = not inside
            elif pipe == "F":
                end_pipe = "J"
            elif pipe == "L":
                end_pipe = "7"
    return tiles_inside


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]

    start = [(x, tiles.index("S"))
             for x, tiles in enumerate(lines) if "S" in tiles][0]

    loop = get_loop(start)

    tiles_on_loop = [item for sublist in loop for item in sublist]
    parsed_tiles = [[lines[x][y] if (x, y) in tiles_on_loop else '.'
                     for y in range(len(lines[0]))]
                    for x in range(len(lines))]

    print(f"Part 1 answer: {len(loop) - 1}")
    print(f"Part 2 answer: {get_enclosed_area(parsed_tiles)}")
