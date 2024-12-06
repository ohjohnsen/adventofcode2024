import re

print ("Advent of Code 2024 - Day 3 - Puzzle 2")

with open("day3/input.txt", "r") as input_file:
    program = input_file.read()

    segments = program.split("don't()")
    enabled_segments = []

    for segment in segments:
        do_segments = segment.split("do()", 1)
        if (len(do_segments) > 1):
            enabled_segments.append(do_segments[1])

    multiplications = []

    for segment in enabled_segments:
        multiplications.extend(re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', segment))

    results = []

    for multiplication in multiplications:
        arguments = multiplication.removeprefix("mul(").removesuffix(")").split(",")
        results.append(int(arguments[0]) * int(arguments[1]))

    total = sum(results)

    print("Sum of all multiplication expressions are: " + str(total))
