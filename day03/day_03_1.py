topo = []
with open("input.txt") as handle:
    for line in handle:
        row = []
        for char in line.strip():
            row.append(char)
        topo.append(row)

trees = 0
i = 0
j = 0
while i < len(topo):
    if topo[i][j] == "#":
        trees += 1
    i += 1
    j += 3
    if j >= len(topo[0]):
        j -= len(topo[0])

print(trees)
