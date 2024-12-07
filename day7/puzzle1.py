print ("Advent of Code 2024 - Day 7 - Puzzle 1")

with open("day7/input.txt", "r") as input_file:
    equations = input_file.read().splitlines()

valid_results = []

for line in equations:
    parts = line.split(": ")
    result = int(parts[0])
    numbers = []
    for number in parts[1].split(" "):
        numbers.append(int(number))

    for i in range(pow(2, len(numbers)-1)):
        operator_pattern = "{0:020b}".format(i)
        operators = list(operator_pattern)[::-1]

        _result = numbers[0]
        for j in range(len(numbers)-1):
            if operators[j] == "0":
                _result += numbers[j+1]
            else:
                _result *= numbers[j+1]

        if _result == result:
            valid_results.append(result)
            break

print("Sum of all valid results: " + str(sum(valid_results)))
