# I need to do this
# ***
#  ***
#   ***
#  ***
# ***

def fill_stars():
    return "*"
def create_row(indent):
    row = []
    for item in range(indent):
        row.append(" ")

        if indent > 5 // 2:
            new_count = 5 - indent
            for x in range(new_count):
                

    for x in range(3):
        row.append(fill_stars())

    return "".join(row)

for indent in range(5):
    print(create_row(indent))