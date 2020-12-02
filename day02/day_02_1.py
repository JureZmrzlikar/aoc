import re

correct = 0
for line in open("input.txt"):
    n1, n2, letter, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).group(1, 2, 3, 4)
    if int(n1) <= password.count(letter) <= int(n2):
        correct +=1

print(correct)
