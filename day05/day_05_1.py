def bisect(string):
    min = 0
    max = 2 ** len(string)
    for letter in string:
        if letter in ["F", "L"]:
            max = min + (max - min) / 2
        if letter in ["B", "R"]:
            min = max - (max - min) / 2
        # print(letter, max, min)

    return min

def get_pass_id(string):
    row = bisect(string[:7])
    column = bisect(string[7:])
    return (row, column, row * 8 + column)


pids = []
with open("input.txt") as handle:
    for line in handle:
        _, _, pid = get_pass_id(line.strip())
        pids.append(pid)

print(max(pids))