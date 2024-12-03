import re

print ("Advent of Code 2024 - Day 3 - Puzzle 1")

with open("day3\\input.txt", "r") as input_file:

    program = input_file.read()
    multiplications = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', program)
    results = []

    for multiplication in multiplications:
        arguments = multiplication.removeprefix("mul(").removesuffix(")").split(",")
        results.append(int(arguments[0]) * int(arguments[1]))

    total = sum(results)

    print("Sum of all multiplication expressions are: " + str(total))
