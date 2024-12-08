print ("Advent of Code 2024 - Day 8 - Puzzle 1")

with open("day8/input.txt", "r") as input_file:
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
                antinode1 = [
                    occurrence1[0]-y_distance,
                    occurrence1[1]-x_distance
                ]
                antinode2 = [
                    occurrence2[0]+y_distance,
                    occurrence2[1]+x_distance
                ]
                if ((0 <= antinode1[0] < height) and (0 <= antinode1[1] < width)):
                    total_antinodes.append(antinode1)

                if ((0 <= antinode2[0] < height) and (0 <= antinode2[1] < width)):
                    total_antinodes.append(antinode2)

print(total_occurrences)
print(total_antinodes)

unique_antinodes = []
for antinode in total_antinodes:
    if not antinode in unique_antinodes:
        unique_antinodes.append(antinode)

print("Number of unique antinode locations: " + str(len(unique_antinodes)))