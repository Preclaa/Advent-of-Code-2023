import math

def count_steps(node, nodes, instructions, end_node=None, end_char=None):
    steps = 0
    while (node != end_node) if end_node else (not node.endswith(end_char)):
        node = nodes[node][int(instructions[steps % len(instructions)])]
        steps += 1
    return steps

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
    instructions = lines[0].replace("L", "0").replace("R", "1")
    nodes = {
        key: tuple(values.strip("()").split(", "))
        for key, values in [line.split(" = ") for line in lines[2:]]
    }

    part1 = count_steps("AAA", nodes, instructions, end_node='ZZZ')

    ghost_nodes = [node for node in nodes if node.endswith('A')]
    ghost_nodes = [count_steps(node, nodes, instructions, end_char='Z') for node in ghost_nodes]
    part2 = math.lcm(*ghost_nodes)

    print(f"Part 1 answer: {part1}")
    print(f"Part 2 answer: {part2}")
