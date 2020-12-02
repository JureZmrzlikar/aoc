import re

correct = 0
for line in open("input.txt"):
    n1, n2, letter, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).group(1, 2, 3, 4)
    if (letter == password[int(n1) - 1] and letter != password[int(n2) - 1]) or (letter != password[int(n1) - 1] and letter == password[int(n2) - 1]):
        correct +=1

print(correct)
