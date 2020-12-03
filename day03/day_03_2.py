topo = []
with open("input.txt") as handle:
    for line in handle:
        row = []
        for char in line.strip():
            row.append(char)
        topo.append(row)

def count_trees(inc_i, inc_j):
    trees = 0
    i = 0
    j = 0
    while i < len(topo):
        if topo[i][j] == "#":
            trees += 1
        i += inc_i
        j += inc_j
        if j >= len(topo[0]):
            j -= len(topo[0])
    return trees

r1_d1 = count_trees(1, 1)
r3_d1 = count_trees(1, 3)
r5_d1 = count_trees(1, 5)
r7_d1 = count_trees(1, 7)
r1_d2 = count_trees(2, 1)

print(r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2)
