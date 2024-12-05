print ("Advent of Code 2024 - Day 5 - Puzzle 1")

with open("day5/input.txt", "r") as input_file:
    input = input_file.read()

split_input = input.split("\n\n")
rules = split_input[0].split("\n")
updates = split_input[1].split("\n")

incorrect_updates = []
middle_pages = []

# First find the incorrect updates
for update in updates:
    update_pages = update.split(",")

    for rule in rules:
        first, second = rule.split("|")

        if first in update_pages:
            first_index = update_pages.index(first)
        else: continue

        if second in update_pages:
            second_index = update_pages.index(second)
        else: continue

        if first_index > second_index:
            incorrect_updates.append(update_pages)
            break

# Correct each update according to the rules
for update_pages in incorrect_updates:

    is_correct_order = False

    while is_correct_order == False:
        is_correct_order = True  # Assume correct order to begin with

        for rule in rules:
            first, second = rule.split("|")

            if first in update_pages:
                first_index = update_pages.index(first)
            else: continue

            if second in update_pages:
                second_index = update_pages.index(second)
            else: continue

            if first_index > second_index:
                update_pages[first_index] = second
                update_pages[second_index] = first
                is_correct_order = False
                break

    page_count = len(update_pages)
    middle_page = update_pages[page_count//2]
    middle_pages.append(int(middle_page))
    
print("Sum of middle page numbers are: " + str(sum(middle_pages)))
