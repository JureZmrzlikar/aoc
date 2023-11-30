def cycle(pos, cycle_size):
    while True:
        if pos < cycle_size - 1:
            pos += 1
        else:
            pos = 0
        yield pos


def redistrubute(bank, start, blocks):
    bank = list(bank)
    bank[start] = 0
    for i in cycle(start, len(bank)):
        bank[i] += 1
        blocks -= 1
        if blocks <= 0:
            break
    return tuple(bank)


def main1(bank):
    count = 0
    already_seen = {bank: count}
    while True:
        # Get index of bank with highest number of blocks:
        max_value = max(bank)
        pos = bank.index(max_value)

        # Redistribute bank and get updated values:
        bank = redistrubute(bank=bank, start=pos, blocks=max_value)
        count += 1

        if bank in already_seen:
            # Return both answers (for part 1 and part 2) simultaneously
            return count, count - already_seen[bank]
        already_seen[bank] = count


INPUT = (14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4)
# INPUT = (0, 2, 7, 0)
print(main1(INPUT))
