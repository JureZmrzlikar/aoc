import re


mapping = {}

with open("input.txt") as handle:
    for line in handle:
        line = line.strip().rstrip(".")

        bag, children_string = line.split(" bags contain ")

        children = []
        if children_string != 'no other bags':
            for child in children_string.split(", "):
                count, bag_name = re.match(r"(\d+) (\w+ \w+) bags?", child).group(1, 2)
                children.append((int(count), bag_name))

        mapping[bag] = children


def iterate_bags(bag):
    ancestors = [bag]
    bag_count = 1
    if mapping[bag] != []:
        for multiple, child in mapping[bag]:
            child_bag_count, child_ancestors = iterate_bags(child)

            ancestors.extend(child_ancestors)
            bag_count += multiple * child_bag_count

    return bag_count, ancestors

count, _ = iterate_bags("shiny gold")
# Subract one for the "root" bag.
print(count - 1)


