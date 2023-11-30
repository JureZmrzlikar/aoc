def parse_input(fname):
    data = []
    with open(fname) as handle:
        for line in handle:
            data.append(list(map(int, line.strip().split())))
    return data


def checksum1(data):
    checksum = 0
    for line in data:
        checksum += max(line) - min(line)
    return checksum


def get_even_div_pair(row):
    row = sorted(row, reverse=True)  # Ensure that always i > j
    for i, n1 in enumerate(row):
        for n2 in row[i + 1:]:
            if n1 % n2 == 0:
                return n1 / n2


def checksum2(data):
    checksum = 0
    for row in data:
        checksum += get_even_div_pair(row)
    return checksum


data = parse_input('/home/jure/devel/adventofcode/day2/input.txt')
print(checksum1(data))
print(checksum2(data))
