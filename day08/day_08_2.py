odata = []

with open("input.txt") as handle:
    for line in handle:
        operation, argument = line.strip().split(" ")
        odata.append((operation, int(argument)))


def loop(data):
    accumulator = 0
    i = 0
    already = set()
    while True:
        if i in already:
            return 0
        if i == len(data):
            return accumulator
        already.add(i)

        operation, argument = data[i]

        if operation == "acc":
            accumulator += argument
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "nop":
            i += 1


for j, (opr, arg) in enumerate(odata):
    if opr == "jmp":
        data = odata[:]
        data[j] = ("nop", arg)
    if opr == "nop":
        data = odata[:]
        data[j] = ("jmp", arg)

    result = loop(data)
    if result:
        print(result)
