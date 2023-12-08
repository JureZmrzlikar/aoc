nodes = {}
with open("input.txt") as handle:
    instructions = next(handle).strip()
    # Skip empty line
    next(handle)
    for line in handle:
        line = line.strip()
        split = line.split(" = ")
        start, ends = split[0], split[-1]
        ends = ends.strip().strip("()").split(",")
        nodes[start] = {"L": ends[0].strip(), "R": ends[1].strip()}

i = 0
node = "AAA"
while node != "ZZZ":
    ins = instructions[i % len(instructions)]
    node = nodes[node][ins]
    i += 1

print(i)
