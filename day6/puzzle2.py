print ("Advent of Code 2024 - Day 6 - Puzzle 2")

# Note! This is not at all an elegant solution! But I spent WAAY too much time on this one... :-D

with open("day6/input.txt", "r") as input_file:
    input = input_file.read().splitlines()

obst_map = []
for row in input:
    obst_map.append(list(row))

height, width = (len(obst_map), len(obst_map[0]))
print("Map size: " + str(width) + " x " + str(height) + " positions")

loop_count = 0

for obst_pos_y in range(height):
    for obst_pos_x in range(width):
        if not obst_map[obst_pos_y][obst_pos_x] == ".":
            continue
        
        map = []
        for row in input:
            map.append(list(row))
        
        map[obst_pos_y][obst_pos_x] = "#"

        # Find the guard's current position
        for pos_y_index in range(height):
            for pos_x_index in range(width):
                if map[pos_y_index][pos_x_index] == "^":
                    pos_x = pos_x_index
                    pos_y = pos_y_index
                    break
            else:
                continue
            break

        dir = "up"
        for i in range(10000):
            next_pos_x = pos_x
            next_pos_y = pos_y

            # Find the next position
            if dir == "up": next_pos_y -= 1
            elif dir == "right": next_pos_x += 1
            elif dir == "down": next_pos_y += 1
            elif dir == "left": next_pos_x -= 1
            next_pos = map[next_pos_y][next_pos_x]

            # Go or rotate?
            if next_pos == "." or next_pos == "X":
                map[pos_y][pos_x] = "X"
                pos_x = next_pos_x
                pos_y = next_pos_y
            else:
                if dir == "up": dir = "right"
                elif dir == "right": dir = "down"
                elif dir == "down": dir = "left"
                elif dir == "left": dir = "up"
            
            if pos_x == 0 or pos_x == width - 1 or pos_y == 0 or pos_y == height - 1:
                map[pos_y][pos_x] = "X"
                break

        if i == 9999:
            loop_count += 1

        movements = 0
        for row in map:
            for pos in row:
                if pos == "X":
                    movements += 1

        # print("With obstacle @ (" + str(obst_pos_x) + "," + str(obst_pos_y) + "), number of movements: " + str(movements))

print("Loop count: " + str(loop_count))
