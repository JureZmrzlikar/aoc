from tqdm import trange

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


min_loc = 10**10
for seed_start, range_ in zip(seeds[::2], seeds[1::2]):
    for seed in range(seed_start, seed_start + range_):
        for block in blocks:
            for (dst, src, rng) in block:
                if seed >= src and seed < src + rng:
                    # Translate as desired
                    destination = dst + (seed - src)
                    break
            else:
                destination = seed

            seed = destination
        if destination < min_loc:
            min_loc = destination

print(min_loc)


# How to speed this up?
# - Brute force will take 24 hours. Not Ok
# - We can use multiprocessing, but this only brings me to ~hours. There must be a better way
