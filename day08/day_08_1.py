data = []

with open("input.txt") as handle:
    for line in handle:
        operation, argument = line.strip().split(" ")
        data.append((operation, int(argument)))


i = 0
accumulator = 0
already = set()
while True:
    if i in already:
        print(accumulator)
        break
    already.add(i)

    operation, argument = data[i]

    if operation == "acc":
        accumulator += argument
        i += 1
    elif operation == "jmp":
        i += argument
    elif operation == "nop":
        i += 1

