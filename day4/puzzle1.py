print ("Advent of Code 2024 - Day 4 - Puzzle 1")

with open("day4\\input.txt", "r") as input_file:
    puzzle = input_file.read().splitlines()

    height = len(puzzle)
    width = len(puzzle[0])

    print("Height:" + str(height) + "  Width:" + str(width))

    xmas_count = 0

    # Step 1 - check horizontally
    for v_index in range(height):
        for h_index in range(width-3):
            sub = puzzle[v_index][h_index:h_index+4]
            if sub == "XMAS" or sub == "SAMX":
                xmas_count += 1

    # Step 2 - check vertically
    for v_index in range(height-3):
        for h_index in range(width):
            sub = ""
            for i in range(4):
                sub += puzzle[v_index+i][h_index:h_index+1]
            if sub == "XMAS" or sub == "SAMX":
                xmas_count += 1

    # Step 3 - check diagonally upwards (slash)
    for v_index in range(height-3):
        for h_index in range(width-3):
            sub = ""
            for i in range(4):
                sub += puzzle[v_index+3-i][h_index+i:h_index+i+1]
            if sub == "XMAS" or sub == "SAMX":
                xmas_count += 1

    # Step 4 - check diagonally downwards (backslash)
    for v_index in range(height-3):
        for h_index in range(width-3):
            sub = ""
            for i in range(4):
                sub += puzzle[v_index+i][h_index+i:h_index+i+1]
            if sub == "XMAS" or sub == "SAMX":
                xmas_count += 1

    print("XMAS is written " + str(xmas_count) + " times")
