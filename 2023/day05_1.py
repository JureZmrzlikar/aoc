blocks = []
seeds = []
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()

        if line.startswith("seeds"):
            seeds = line.split(":")[1].strip().split(" ")
            seeds = [int(s) for s in seeds]
        elif line == "":
            continue
        elif line.endswith("map:"):
            # Start of a line
            block = []
            line = handle.readline().strip()
            while line != "":
                block.append([int(e) for e in line.split(" ")])
                line = handle.readline().strip()

            blocks.append(block)

locations = []
for seed in seeds:
    for block in blocks:
        for (dst, src, rng) in block:
            if seed >= src and seed < src + rng:
                # Translate as desired
                destination = dst + (seed - src)
                break
        else:
            destination = seed

        seed = destination
    locations.append(destination)

print(min(locations))