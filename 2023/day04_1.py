sum = 0
with open("input.txt") as handle:
    for line in handle:
        winning, my = line.strip().split(":")[1].split("|")
        winning = winning.strip().split(" ", )
        my = my.strip().split(" ")
        intersect = []
        for m in my:
            for w in winning:
                if m == w and m != "":
                    intersect.append(m)

        if intersect:
            print(my)
            print(winning)
            print(intersect)
            print(2**(len(intersect) - 1))
            print()
            sum += 2**(len(intersect) - 1)

print(sum)