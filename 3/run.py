f = open("./3/input.txt")
raw_data = f.read().split("\n")


slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

tree_result = 1

for slope in slopes:

    line_pos = 0
    test_pos = 0
    tree_count = 0

    for current_line in range(0, len(raw_data), slope[1]):
        if line_pos > 0:
            test_pos = line_pos % len(raw_data[current_line])
        if raw_data[current_line][test_pos] == "#":
            tree_count = tree_count + 1

        line_pos = line_pos + slope[0]

    print(tree_count)
    tree_result = tree_result * tree_count

print (tree_result)