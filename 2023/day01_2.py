numbers = {
    "1": 1,
    "one": 1,
    "2": 2,
    "two": 2,
    "3": 3,
    "three": 3,
    "4": 4,
    "four": 4,
    "5": 5,
    "five": 5,
    "6": 6,
    "six": 6,
    "7": 7,
    "seven": 7,
    "8": 8,
    "eight": 8,
    "9": 9,
    "nine": 9,
}

calibration_nums = []
with open("input.txt") as handle:
    for line in handle:
        line = line.strip()
        nums = []
        while line:
            for key, value in numbers.items():
                if line.startswith(key):
                    nums.append(value)
                    break

            line = line[1:]

        calibration_nums.append(10 * nums[0] + nums[-1])

print(sum(calibration_nums))
