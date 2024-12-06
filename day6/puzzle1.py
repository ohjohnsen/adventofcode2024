print ("Advent of Code 2024 - Day 6 - Puzzle 1")

with open("day6/input.txt", "r") as input_file:
    input = input_file.read().splitlines()

map = []
for row in input:
    map.append(list(row))

height, width = (len(map), len(map[0]))

print("Map size: " + str(width) + " x " + str(height) + " positions")

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

for i in range(1000000):
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

movements = 0
for row in map:
    for pos in row:
        if pos == "X":
            movements += 1

print("Number of movements: " + str(movements))
