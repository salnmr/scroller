import time

def create_top_row(indent):
    row = []
    for space in range(indent):
        row.append(" ")
    for char in range(3):
        row.append("x")
    return "".join(row)


def create_bottom_row(indent):
    row = []
    for space in range(indent - 1):
        row.append(" ")
    for char in range(3):
        row.append("x")
    return "".join(row)

for group in range(4):
    for indent in range(6):
        print(create_top_row(indent))
        time.sleep(.4)
    for indent in range(5, 0, -1):
        print(create_bottom_row(indent))
        time.sleep(.4)
