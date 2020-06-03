# write your code here
cells = []
letter = ""
for _ in range(9):
    cells.append(" ")


def check(cell, letter):
    if(
            ((cell[0] == letter) & (cell[1] == letter) & (cell[2] == letter)) or
            ((cell[3] == letter) & (cell[4] == letter) & (cell[5] == letter)) or
            ((cell[6] == letter) & (cell[7] == letter) & (cell[8] == letter)) or
            ((cell[0] == letter) & (cell[3] == letter) & (cell[6] == letter)) or
            ((cell[1] == letter) & (cell[4] == letter) & (cell[7] == letter)) or
            ((cell[2] == letter) & (cell[5] == letter) & (cell[8] == letter)) or
            ((cell[0] == letter) & (cell[4] == letter) & (cell[8] == letter)) or
            ((cell[2] == letter) & (cell[4] == letter) & (cell[6] == letter))
    ):
        return True
    else:
        return False


def print_():  # function to print the cells in order
    print('''
    ----------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ----------
    '''.format(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7], cells[8]))


def is_empty(x, y, add_element):
    global cells, letter
    if x == "1" and y == "1" and (cells[6] != "X" and cells[6] != "O"):
        if add_element:
            cells[6] = letter
        return True
    elif x == '1' and y == '2' and (cells[3] != "X" and cells[3] != "O"):
        if add_element:
            cells[3] = letter
        return True
    elif x == '1' and y == '3' and (cells[0] != "X" and cells[0] != "O"):
        if add_element:
            cells[0] = letter
        return True
    elif x == '2' and y == '1' and cells[7] != "X" and cells[7] != "O":
        if add_element:
            cells[7] = letter
        return True
    elif x == '2' and y == '2' and cells[4] != "X" and cells[4] != "O":
        if add_element:
            cells[4] = letter
        return True
    elif x == '2' and y == '3' and cells[1] != "X" and cells[1] != "O":
        if add_element:
            cells[1] = letter
        return True
    elif x == '3' and y == '1' and (cells[8] != "X" and cells[8] != "O"):
        if add_element:
            cells[8] = letter
        return True
    elif x == '3' and y == '2' and cells[5] != "X" and cells[5] != "O":
        if add_element:
            cells[5] = letter
        return True
    elif x == '3' and y == '3' and cells[2] != "X" and cells[2] != "O":
        if add_element:
            cells[2] = letter
        return True
    else:
        return False


def main_():
    global letter
    x, y = input("Enter the coordinates: ").split()
    if x > '3' or y > '3':
        print("Coordinates should be from 1 to 3!")
        main_()
    elif not is_empty(x, y, False):                             # if the cells are empty, then is_empty() function
        print("This cell is occupied! Choose another one! ")    # will return True and this statement gets false
        main_()
    elif is_empty(x, y, True):
        print_()
    else:
        print("You should enter numbers!")
        main_()


# main function started ***********************
n = 0
print_()
while n != 9:
    if n % 2 == 0:
        letter = "X"
    else:
        letter = "O"
    main_()
    n += 1
    if check(cells, "X"):
        print("X wins")
        break
    elif check(cells, "O"):
        print("O wins")
        break
    elif (
        (cells.count("X") == 5 and cells.count("O") == 4) or
        (cells.count("X") == 4 and cells.count("O") == 5)
    ):
        print("Draw")
        break

