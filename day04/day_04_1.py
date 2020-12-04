required = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
])



def process_entry(entry):
    entry = " ".join(entry)
    keys = [pair.split(":")[0] for pair in entry.split(" ")]
    if all([r in keys for r in required]):
        return 1
    return 0


valid = 0
entry = []
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()
        if line != "":
            entry.append(line)
        else:
            # Process entry
            valid += process_entry(entry)
            entry = []

    # Final line
    valid += process_entry(entry)
    entry = []

print(valid)