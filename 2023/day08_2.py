data = {}
with open("input.txt") as handle:
    instructions = next(handle).strip()
    # Skip empty line
    next(handle)
    for line in handle:
        line = line.strip()
        split = line.split(" = ")
        start, ends = split[0], split[-1]
        ends = ends.strip().strip("()").split(",")
        data[start.strip()] = {"L": ends[0].strip(), "R": ends[1].strip()}

# Just brute-forcing takes too much time (I quit after an hour).
# Key realization: each node has a certain roundtrip size, we need to find LCM of all roundtrips

# Find: Smallest common multiple of all the roundtrips of a node
start_nodes = [n for n in data.keys() if n.endswith("A")]
roundtrips = []
for start_node in start_nodes:
    node = start_node
    node_z_ends = {}
    node = None
    i = 0
    while not (node == start_node and i % len(instructions) == 0):
        node = node or start_node
        ins = instructions[i % len(instructions)]
        node = data[node][ins]
        i += 1
        if node.endswith("Z"):
            roundtrips.append(i)
            break

print(roundtrips)
import math
print(math.lcm(*roundtrips))
