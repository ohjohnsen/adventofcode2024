print ("Advent of Code 2024 - Day 2 - Puzzle 2")

with open("day2/input.txt", "r") as input_file:
    reports = input_file.read().splitlines()

def check_report(levels):
    is_safe_report = True   # Assume report is true
    # Values are increasing
    if ((levels[0] < levels[1])):
        for index in range(len(levels)-1):
            diff = levels[index+1] - levels[index]
            if (diff < 1 or diff > 3):
                is_safe_report = False
                break
    # Values are decreasing
    else:
        for index in range(len(levels)-1):
            diff = levels[index] - levels[index+1]
            if (diff < 1 or diff > 3):
                is_safe_report = False
                break
    return is_safe_report

safe_report_count = 0
report_safety_states = []

for report in reports:
    levels = list(map(int, report.split(" ")))

    if (check_report(levels)):
        safe_report_count += 1
    else:
        # Try removing each level one by one and re-check if the report is safe
        for index in range(len(levels)):
            levels_copy = levels.copy()
            del levels_copy[index]
            if (check_report(levels_copy)):
                safe_report_count += 1
                break

print("Number of safe reports: " + str(safe_report_count))