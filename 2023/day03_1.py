numbers = [f"{i}" for i in range(10)]

# Just read file into an array:
# Make it short, because it's gonna be used often
c = []  # content
with open("input.txt") as handle:
    for line in handle:
        c.append([c for c in line.strip()])

def is_symbol(char):
    return not (char in numbers + ["."])

def finalize(i, j, k):
    include = False
    left = max(j - 1, 0)
    right = min(k, len(c[i]) - 1)
    # Left:
    if is_symbol(c[i][left]):
        print("left")
        include = True
    # Right:
    elif is_symbol(c[i][right]):
        print("right")
        include = True
    # Row up:
    elif i > 0 and any([is_symbol(e) for e in c[i - 1][left:right + 1]]):
        print("up")
        include = True
    # Row down:
    elif i < len(c) - 1 and any([is_symbol(e) for e in c[i + 1][left: right + 1]]):
        print("down")
        include = True

    print(number, i, j, k, include)
    if include:
        return int(number)
    return 0





sum = 0
for i in range(len(c)):
    # if i == 10:
    #     break
    j = 0  # Starting digit of current number
    k = 0  # Ending digit of current number
    number = ""
    while k < len(c[i]):
        if c[i][k] in numbers:
            # Start or continuation of a number
            if not number:
                # Mark the start of a new number
                j = k

            number = f"{number}{c[i][k]}"
            # TODO: End of line!
            if k == len(c[i]) - 1:
                sum += finalize(i, j, k)
        else:
            if number:
                # End of a number:

                # At this point, we have the number and it's positional info
                # Need to decide whether include it or not

                sum += finalize(i, j, k)

            # In any case, let's set the number to empty now
            number = ""

        k += 1

print(sum)