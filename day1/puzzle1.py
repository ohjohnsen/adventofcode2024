print ("Advent of Code 2024 - Day 1 - Puzzle 1")

with open("day1\\input.txt", "r") as input_file:
    rows = input_file.read().splitlines()
    column1 = []
    column2 = []

    for row in rows:
        columns = row.split("   ")
        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

    column1.sort()
    column2.sort()
    distance = []

    for i in range(len(column1)):
        distance.append(abs(column1[i]-column2[i]))

    total_distance = sum(distance)

    print("Total distance: " + str(total_distance))