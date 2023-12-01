numbers = set([f"{i}" for i in range(1, 10)])

calibration_nums = []
with open("input.txt") as handle:
    for line in handle:
        # Filter out all numbers
        nums = [char for char in line if char in numbers]
        calibration_nums.append(int(f"{nums[0]}{nums[-1]}"))

print(sum(calibration_nums))
