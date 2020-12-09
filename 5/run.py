
f = open("./5/input.txt")
raw_data = f.read().split("\n")

max_seat_id = 0

seat_ids = []

for entry in raw_data:
    rows = list(range(0, 128))
    cols = list(range(0, 8))

    for row_loc in range(0, 7):
        if entry[row_loc] == "F":
            rows = rows[0:int(len(rows)/2)]
        elif entry[row_loc] == "B":
            rows = rows[int(len(rows)/2):len(rows)]

    row = rows[0]

    for col_loc in range(7, 10):
        if entry[col_loc] == "L":
            cols = cols[0:int(len(cols)/2)]
        elif entry[col_loc] == "R":
            cols = cols[int(len(cols)/2):len(cols)]

    col = cols[0]

    seat_id = (row * 8) + col
    seat_ids.append(seat_id)

    if seat_id > max_seat_id:
        max_seat_id = seat_id

seat_ids.sort()
last_seat_id = 0

for seat_id in seat_ids:
    if last_seat_id == 0:
        last_seat_id = seat_id - 1

    if last_seat_id == seat_id - 2:
        print(last_seat_id + 1)

    last_seat_id = seat_id

