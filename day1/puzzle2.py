print ("Advent of Code 2024 - Day 1 - Puzzle 2")

with open("day1/input.txt", "r") as input_file:
    rows = input_file.read().splitlines()
    column1 = []
    column2 = []
    similarities = []

    for row in rows:
        columns = row.split("   ")
        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

    for index in range(len(column1)):
        similarity = 0
        for row in column2:
            if (column1[index] == row):
                similarity += column1[index]
        similarities.append(similarity)

    total_similarity = sum(similarities)

    print("Total similarity: " + str(total_similarity))