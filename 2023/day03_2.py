numbers = [f"{i}" for i in range(10)]

# Just read file into an array:
# Make it short, because it's gonna be used often
c = []  # content
with open("input.txt") as handle:
    for line in handle:
        c.append([c for c in line.strip()])
# print(c)

def is_symbol(char):
    return not (char in numbers + ["."])


# def finalize(i, j, k):
#     # c[]
#     left = max(j - 1, 0)
#     right = min(k, len(c[i]) - 1)
#     # Left:
#     if is_symbol(c[i][left]):
#         print("left")
#         include = True
#     # Right:
#     elif is_symbol(c[i][right]):
#         print("right")
#         include = True
#     # Row up:
#     elif i > 0 and any([is_symbol(e) for e in c[i - 1][left:right + 1]]):
#         print("up")
#         include = True
#     # Row down:
#     elif i < len(c) - 1 and any([is_symbol(e) for e in c[i + 1][left: right + 1]]):
#         print("down")
#         include = True

#     print(number, i, j, k, include)
#     if include:
#         return int(number)
#     return 0


# Fill whole numbers into the array:
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
                for n in range(j, k + 1):
                    c[i][n] = int(number)

        else:
            if number:
                # End of a number:
                # At this point, we have the number and it's positional info
                for n in range(j, k):
                    c[i][n] = int(number)

            # In any case, let's set the number to empty now
            number = ""

        k += 1
#


sum = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        if c[i][j] == "*":
            prods = []
            left = max(j - 1, 0)
            right = min(j + 1, len(c[i]) - 1)
            up = max(i - 1, 0)
            down = min(i + 1, len(c) - 1)
            # Up left
            if isinstance(c[up][left], int):
                prods.append(c[up][left])
            # Up
            if isinstance(c[up][j], int):
                prods.append(c[up][j])
            # Up right
            if isinstance(c[up][right], int):
                prods.append(c[up][right])
            # Left
            if isinstance(c[i][left], int):
                prods.append(c[i][left])
            # Right
            if isinstance(c[i][right], int):
                prods.append(c[i][right])
            # Down left
            if isinstance(c[down][left], int):
                prods.append(c[down][left])
            # Down
            if isinstance(c[down][j], int):
                prods.append(c[down][j])
            # Down right
            if isinstance(c[down][right], int):
                prods.append(c[down][right])

            # if len(prods) >= 3 and len(set(prods)) < 2:
            #     print(prods, i, j)
            prods = list(set(prods))
            if len(prods) == 2:
                print(prods, i, j)
                sum += prods[0] * prods[1]

# Manually detected the two that are equal :-)
# Fuck it, I need to go to sleep :-)
print(sum + 443**2 + 950**2)