def compute_distances(time):
    distances = []
    for hold_time in range(time + 1):
        speed = hold_time
        distance = speed * (time - hold_time)
        distances.append(distance)

    return distances


with open("input.txt") as handle:
    times = handle.readline().strip().split(":")[1].strip().split(" ")
    distances = handle.readline().strip().split(":")[1].strip().split(" ")

# Remove empty strings
times = [int(e) for e in times if e != ""]
distances = [int(e) for e in distances if e != ""]

prod = []
for time, distance in zip(times, distances):
    my_distances = compute_distances(time)
    ways_to_win = 0
    for my_dist in my_distances:
        if my_dist > distance:
            ways_to_win += 1

    prod.append(ways_to_win)

final = 1
for p in prod:
    final *= p
print(final)