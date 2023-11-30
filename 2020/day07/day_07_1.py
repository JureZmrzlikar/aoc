import re


mapping = {}

with open("input.txt") as handle:
    for line in handle:
        line = line.strip().rstrip(".")

        bag, children_string = line.split(" bags contain ")

        children = []
        if children_string != 'no other bags':
            for child in children_string.split(", "):
                bag_name = re.match(r"\d+ (\w+ \w+) bags?", child).group(1)
                children.append(bag_name)

        mapping[bag] = children


def iterate_bags(bag):
    ancestors = [bag]
    if mapping[bag] != []:
        for child in mapping[bag]:
            child_ancestors = iterate_bags(child)
            ancestors.extend(child_ancestors)

    return ancestors


count = 0
for bag in mapping:
    # Ignore first bag as it is the "root" bag
    if "shiny gold" in iterate_bags(bag)[1:]:
        count += 1

print(count)


