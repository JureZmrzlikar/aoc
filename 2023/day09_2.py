# Key realization:
# part 2 is same as part 1, just reverse the input. :-)

def extrapolate(line):
    # Define the diffs to desired depth
    diffs = [line]
    k = 0
    while any([d != 0 for d in diffs[k]]):
        diff = [ j - i for i, j in zip(diffs[k], diffs[k][1:])]
        diffs.append(diff)
        k += 1
    while k > 0:
        diffs[k-1].append(diffs[k-1][-1] + diffs[k][-1])
        k -= 1
    nxt = diffs[0][-1]
    return nxt


sum = 0
with open("input.txt") as handle:
    for line in handle:
        line = line.strip().split(" ")
        line = [int(e) for e in line if e != " "]
        line = line[::-1]
        sum += extrapolate(line)
print(sum)
