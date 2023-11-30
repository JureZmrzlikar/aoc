def parse_input(fname):
    data = []
    with open(fname) as handle:
        for line in handle:
            data.append(int(line.strip()))
    return data


def main1(seq):
    steps = 0
    pos = 0
    try:
        while True:
            offset = seq[pos]
            seq[pos] += 1
            pos += offset
            steps += 1

    except IndexError:
        return steps


def main2(seq):
    steps = 0
    pos = 0
    try:
        while True:
            offset = seq[pos]
            if offset >= 3:
                seq[pos] -= 1
            else:
                seq[pos] += 1
            pos += offset
            steps += 1

    except IndexError:
        return steps


print(main1(parse_input('/home/jure/devel/adventofcode/day5/input.txt')))
print(main2(parse_input('/home/jure/devel/adventofcode/day5/input.txt')))
