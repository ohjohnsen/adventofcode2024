print ("Advent of Code 2024 - Day 5 - Puzzle 1")

with open("day5/input.txt", "r") as input_file:
    input = input_file.read()

split_input = input.split("\n\n")
rules = split_input[0].split("\n")
updates = split_input[1].split("\n")

middle_pages = []

for update in updates:
    update_pages = update.split(",")
    is_update_correct_order = True  # Assume update has correct page order

    for rule in rules:
        first, second = rule.split("|")

        if first in update_pages:
            first_index = update_pages.index(first)
        else: continue

        if second in update_pages:
            second_index = update_pages.index(second)
        else: continue

        if first_index > second_index:
            is_update_correct_order = False
            break

    if is_update_correct_order:
        page_count = len(update_pages)
        middle_page = update_pages[page_count//2]
        middle_pages.append(int(middle_page))
    
print("Sum of middle page numbers are: " + str(sum(middle_pages)))
