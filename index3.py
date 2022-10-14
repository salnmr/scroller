import time

def create_row(indent):
    row = []
    stars = ['x','*','x']
    for space in range(indent):
        row.insert(0,' ')
    for star in range(len(stars)):
        row.append(stars[star])
    return "".join(row)

for groups in range(2):
    reverse = False
    while reverse == False:
        for indent in range(3):
            print(create_row(indent))
            time.sleep(.3)
        reverse = True
        while reverse == True:
            for indent in range(2, 0, -1):
                print(create_row(indent))
                time.sleep(.3)
                reverse = False
