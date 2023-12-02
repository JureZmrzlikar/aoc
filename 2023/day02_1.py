def is_valid(subset):
    parts = subset.split(',')
    red, blue, green = 0, 0, 0
    for part in parts:
        part = part.strip()
        if "red" in part:
            red = int(part.split(" ")[0])
        elif "blue" in part:
            blue = int(part.split(" ")[0])
        if "green" in part:
            green = int(part.split(" ")[0])
    if red > 12:
        return False
    elif blue > 14:
        return False
    elif green > 13:
        return False

    return True

sum = 0
with open("input.txt") as handle:
    for line in handle:
        id_part, subset_part = line.split(":")
        id = id_part.split(" ")[1]
        if all(is_valid(subset) for subset in subset_part.split(";")):
            sum += int(id)

print(sum)
