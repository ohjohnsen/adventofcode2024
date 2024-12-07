import numpy as np

print ("Advent of Code 2024 - Day 7 - Puzzle 2")

with open("day7/input.txt", "r") as input_file:
    equations = input_file.read().splitlines()

valid_results = []

for line in equations:
    parts = line.split(": ")
    result = int(parts[0])
    numbers = []
    for number in parts[1].split(" "):
        numbers.append(int(number))

    print(numbers)

    for i in range(pow(3, len(numbers)-1)):
        operator_pattern = np.base_repr(i, 3, 20)
        operators = list(operator_pattern)[::-1]

        _result = numbers[0]
        for j in range(len(numbers)-1):
            if operators[j] == "0":
                _result += numbers[j+1]
            elif operators[j] == "1":
                _result *= numbers[j+1]
            else:
                _result = int(f"{_result}{numbers[j+1]}")

        if _result == result:
            valid_results.append(result)
            break

print("Sum of all valid results: " + str(sum(valid_results)))
