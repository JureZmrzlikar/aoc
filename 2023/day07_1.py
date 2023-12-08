letters = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strengths = {l: i for i, l in enumerate(letters[::-1])}


def get_type(hand):
    # Five of a kind
    s = set(hand)
    counts = sorted([hand.count(e) for e in s], reverse=True)
    if len(s) == 1:
        return 6
    # four of a kind
    elif len(s) == 2 and counts[0] == 4:
        return 5
    # Full house
    elif len(s) == 2 and counts[0] == 3:
        return 4
    # Three of a kind
    elif len(s) == 3 and counts[0] == 3:
        return 3
    # Two pair
    elif len(s) == 3 and counts[0] == 2:
        return 2
    # One pair
    elif len(s) == 4 and counts[0] == 2:
        return 1
    else:
        return 0


def get_strength(hand):
    strength = [get_type(hand)]
    for ltr in hand:
        strength.append(strengths[ltr])
    return strength


data = []
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()
        split = line.split(" ")
        hand, bid = split[0], split[-1]
        data.append(tuple(get_strength(hand) + [bid]))

data = sorted(data)

sum = 0
for i, d in enumerate(data, start=1):
    sum += i * int(d[-1])

print(sum)
