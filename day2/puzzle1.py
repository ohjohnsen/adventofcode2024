print ("Advent of Code 2024 - Day 2 - Puzzle 1")

with open("day2\\input.txt", "r") as input_file:
    reports = input_file.read().splitlines()

safe_report_count = 0

for report in reports:
    levels = list(map(int, report.split(" ")))

    is_safe_report = True   # Assume report is true

    # Values are increasing
    if ((levels[0] < levels[1])):
        for index in range(len(levels)-1):
            diff = levels[index+1] - levels[index]
            if (diff < 1 or diff > 3):
                is_safe_report = False

    # Values are decreasing
    else:
        for index in range(len(levels)-1):
            diff = levels[index] - levels[index+1]
            if (diff < 1 or diff > 3):
                is_safe_report = False

    if (is_safe_report):
        safe_report_count += 1

print("Number of safe reports: " + str(safe_report_count))