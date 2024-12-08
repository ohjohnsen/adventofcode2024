print ("Advent of Code 2024 - Day 8 - Puzzle 2")

with open("day8/input_example.txt", "r") as input_file:
    input = input_file.read().splitlines()

height = len(input)
width = len(input[0])

print(height)
print(width)

total_antinodes = []  # Represented by [Y,X] from top left
total_occurrences = []

for frequency in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    occurrences = []  # Represented by [Y,X] from top left
    for row in input:
        for location in row:
            if location == frequency:
                # print(frequency + " @ (" + str(row.index(location)) + "," + str(input.index(row)) + ")")
                occurrences.append([input.index(row), row.index(location)])
                total_occurrences.append([input.index(row), row.index(location)])

    if len(occurrences) > 1: # Antinodes are only formed with two or more occurrences of a frequency
        # print(occurrences)
        # print(occurrences[1:])

        for index in range(len(occurrences)-1):
            occurrence1 = occurrences[index]
            for occurrence2 in occurrences[index+1:]:
                x_distance = occurrence2[1]-occurrence1[1]
                y_distance = occurrence2[0]-occurrence1[0]

                antinode1_ref = occurrence1
                antinode2_ref = occurrence2

                while True:
                    antinode1 = [
                        antinode1_ref[0]-y_distance,
                        antinode1_ref[1]-x_distance
                    ]
                    antinode2 = [
                        antinode2_ref[0]+y_distance,
                        antinode2_ref[1]+x_distance
                    ]
                    print(antinode1)
                    print(antinode2)
                    if ((0 <= antinode1[0] < height) and (0 <= antinode1[1] < width)):
                        total_antinodes.append(antinode1)
                        antinode1_ref = antinode1
                        # print(antinode1)

                    if ((0 <= antinode2[0] < height) and (0 <= antinode2[1] < width)):
                        total_antinodes.append(antinode2)
                        antinode2_ref = antinode2
                        # print(antinode2)

                    if (((antinode1[0] < 0 or antinode1[0] >= height) or (antinode1[1] < 0 or antinode1[1] >= width)) and
                        ((antinode2[0] < 0 or antinode2[0] >= height) or (antinode2[1] < 0 or antinode2[1] >= width))):
                        break


print(total_occurrences)
print(total_antinodes)
print(len(total_antinodes))

unique_antinodes = []
for antinode in total_antinodes:
    if not antinode in unique_antinodes:
        unique_antinodes.append(antinode)

print("Number of unique antinode locations: " + str(len(unique_antinodes)))