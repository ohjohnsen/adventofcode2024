print ("Advent of Code 2024 - Day 4 - Puzzle 2")

with open("day4/input.txt", "r") as input_file:
    puzzle = input_file.read().splitlines()

    height = len(puzzle)
    width = len(puzzle[0])

    print("Height:" + str(height) + "  Width:" + str(width))

    xmas_count = 0

    for v_index in range(height-2):
        for h_index in range(width-2):
            sub = ""
            dw_sub = ""
            uw_sub = ""
            for i in range(3):
                dw_sub += puzzle[v_index+i][h_index+i:h_index+i+1]
                uw_sub += puzzle[v_index+2-i][h_index+i:h_index+i+1]

            if (dw_sub == "MAS" or dw_sub == "SAM") and (uw_sub == "MAS" or uw_sub == "SAM"):
                xmas_count += 1

    print("MAS is written as an X " + str(xmas_count) + " times")
