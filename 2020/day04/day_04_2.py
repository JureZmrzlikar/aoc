import re

required = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",  # is optional
])


def is_year_valid(year, min_value, max_value):
    match = re.match(r"^\d{4}$", year)
    if not match:
        return 0
    year = int(year)
    if not (min_value <= year <= max_value):
        return 0
    return 1

def is_year_valid(year, min_value, max_value):
    match = re.match(r"^\d{4}$", year)
    if not match:
        return 0
    year = int(year)
    if not (min_value <= year <= max_value):
        return 0
    return 1


def is_entry_valid(entry):
    entry = " ".join(entry)
    key_vals = {pair.split(":")[0]: pair.split(":")[1] for pair in entry.split(" ")}

    #Validate all keys are present:
    if not all([r in list(key_vals.keys()) for r in required]):
        return 0

    # Birth year
    if not is_year_valid(key_vals["byr"], 1920, 2002):
        return 0
    # Issue year
    if not is_year_valid(key_vals["iyr"], 2010, 2020):
        return 0
    # Expire year
    if not is_year_valid(key_vals["eyr"], 2020, 2030):
        return 0

    # Height
    match = re.match(r"^(\d{2,3})(cm|in)$", key_vals["hgt"])
    if not match:
        return 0
    value, unit = match.group(1, 2)
    if unit == "cm" and 150 <= int(value) <= 193:
        pass
    elif unit == "in" and 59 <= int(value) <= 76:
        pass
    else:
        return 0

    # Hair Color
    match = re.match(r"^#[0-9a-f]{6}$", key_vals["hcl"])
    if not match:
        return 0

    # Eye color
    match = re.match(r"^amb|blu|brn|gry|grn|hzl|oth$", key_vals["ecl"])
    if not match:
        return 0

    if "pid" in key_vals:
        match = re.match(r"\d{9}$", key_vals["pid"])
        if not match:
            return 0

    return 1


valid = 0
entry = []
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()
        if line != "":
            entry.append(line)
        else:
            # Process entry
            valid += is_entry_valid(entry)
            entry = []

    # Final line
    valid += is_entry_valid(entry)
    entry = []

print(valid)