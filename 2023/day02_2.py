def power(subsets):
    min_red, min_blue, min_green = None, None, None
    for subset in subsets:
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
        if min_red is None or red > min_red:
            min_red = red
        if min_blue is None or blue > min_blue:
            min_blue = blue
        if min_green is None or green > min_green:
            min_green = green

    power = min_red * min_blue * min_green
    return power


sum = 0
with open("input.txt") as handle:
    for line in handle:
        _, subset_part = line.split(":")
        sum += power(subset_part.split(";"))

print(sum)
