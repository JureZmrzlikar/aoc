def process_group(group):
    common = set(group[0])
    for one in group[1:]:
        common = common & set(one)

    return len(set(common))


group = []
all_sum = 0
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()
        if line != "":
            group.append(line)
        else:
            # Process group
            all_sum += process_group(group)
            group = []

    # Final line
    all_sum += process_group(group)
    group = []

print(all_sum)