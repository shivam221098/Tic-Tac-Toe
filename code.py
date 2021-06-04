import random
from abc import ABC, abstractmethod


cells = []
letter = ""
for _ in range(9):
    cells.append(" ")


def check(cell, check_letter):
    if (
            ((cell[0] == check_letter) & (cell[1] == check_letter) & (cell[2] == check_letter)) or
            ((cell[3] == check_letter) & (cell[4] == check_letter) & (cell[5] == check_letter)) or
            ((cell[6] == check_letter) & (cell[7] == check_letter) & (cell[8] == check_letter)) or
            ((cell[0] == check_letter) & (cell[3] == check_letter) & (cell[6] == check_letter)) or
            ((cell[1] == check_letter) & (cell[4] == check_letter) & (cell[7] == check_letter)) or
            ((cell[2] == check_letter) & (cell[5] == check_letter) & (cell[8] == check_letter)) or
            ((cell[0] == check_letter) & (cell[4] == check_letter) & (cell[8] == check_letter)) or
            ((cell[2] == check_letter) & (cell[4] == check_letter) & (cell[6] == check_letter))
    ):
        return True
    else:
        return False


def print_():  # function to print the cells in order
    print('''
    ---------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ---------
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
    num_coordinate = {
        "1": "1 1",
        "2": "2 1",
        "3": "3 1",
        "4": "1 2",
        "5": "2 2",
        "6": "3 2",
        "7": "1 3",
        "8": "2 3",
        "9": "3 3"
    }
    global letter
    num = input("Enter the coordinates: ")
    x, y = num_coordinate.get(num).split()
    if x > '3' or y > '3':
        print("Coordinates should be from 1 to 3!")
        main_()
    elif not is_empty(x, y, False):  # if the cells are empty, then is_empty() function
        print("This cell is occupied! Choose another one! ")  # will return True and this statement gets false
        main_()
    elif is_empty(x, y, True):
        print_()
    else:
        print("You should enter numbers!")
        main_()


# ******************** main function started ***********************
def main():
    global letter
    n = 0
    print_()
    while n != 9:
        if n % 2 == 0:
            print("X's turn")
            letter = "X"
        else:
            print("O's turn")
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


# ************************* Player vs Computer ************************
class Player:
    # 3.
    def __init__(self, mark, player_type):
        self.mark = mark
        self.opp_mark = "O" if mark == "X" else "X"
        self.player_type = player_type


class User(Player):
    def move(self, fields):
        coord = self.coordinates(fields)
        fields[coord] = self.mark

    def coordinates(self, fields):
        try:
            prompt = input("Enter the coordinates: ")
            if prompt.isalpha():
                coord = prompt

            else:
                coord = int(prompt) - 1

            if 8 < coord < 0:
                print("Coordinates should be from 1 to 9!")
                return self.coordinates(fields)
            if fields[coord] in Game.mark:
                print("This cell is occupied! Choose another one!")
                return self.coordinates(fields)

            return coord
        except TypeError:
            if coord == "quit":
                Game().start()
            else:
                print("You should enter numbers!")
                return self.coordinates(fields)


# abstract sublass of Player
class Robot(ABC, Player):
    # 4b
    def move(self, fields):
        print(f'Making move level "{self.player_type.lower()}"')
        coord = self.coordinates(fields)
        fields[coord] = self.mark

    @abstractmethod
    def coordinates(self, fields):
        pass


# Playing with computer in medium level
class Medium(Robot):
    def coordinates(self, fields):
        coord = self.two_row_check(fields)
        if coord is None:
            coord = self.random_coord(fields)
        return coord

    def random_coord(self, fields):
        coord = random.randint(0, 8)
        if fields[coord] != " ":
            return self.coordinates(fields)
        return coord

    def two_row_check(self, fields):
        if Game.mark[0] == self.mark:
            mark_list = Game.mark
        else:
            mark_list = Game.mark.copy()
            mark_list.reverse()

        cols = [fields[i::3] for i in range(3)]

        rows = [fields[i * 3:(i + 1) * 3] for i in range(3)]

        main_diagonal = [fields[0], fields[4], fields[8]]
        side_diagonal = [fields[2], fields[4], fields[6]]
        """Below checks various cases below where the player is one mark away from a win
        Then Returns a coordinate based on that."""
        for mark in mark_list:
            for index, col in enumerate(cols):
                if col.count(mark) == 2 and col.count(' '):
                    return 3 * col.index(" ") + index
            for index, row in enumerate(rows):
                if row.count(mark) == 2 and row.count(' '):
                    return 3 * index + row.index(" ")

            if main_diagonal.count(mark) == 2 and main_diagonal.count(' '):
                index = main_diagonal.index(' ')
                return (3 * index) + index

            if side_diagonal.count(mark) == 2 and side_diagonal.count(' '):
                index = side_diagonal.index(' ')
                return (index + 1) * 2
        return None


# Class for starting game
class Game:
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    command = {'user': User, 'medium': Medium}
    mark = ['X', 'O']  # Our two marks

    def __init__(self):
        self.fields = Game.board.copy()
        self.player = ""
        self.play = True
        self.start()
        print(self)
        self.process()

    def __str__(self):
        # displays the board/field
        result = f"---------\n" \
                 f"| {' '.join(self.fields[6:9])} |\n" \
                 f"| {' '.join(self.fields[3:6])} |\n" \
                 f"| {' '.join(self.fields[0:3])} |\n" \
                 f"---------"
        return result

    # 2. This method calls different other methods based on the command
    def start(self):
        if not self.play:
            print("Thanks for playing!")
            exit(0)
        params = "start user medium".split()
        self.play = False
        if params[0] == 'exit' and len(params) == 1:
            exit()
        elif params[0] == 'start' and len(params) == 3:
            # this block starts the game
            if params[1] in Game.command and params[2] in Game.command:
                self.players = [
                    # a list whose elements calls the 3. constructor(s) from different subclasses 3a, 3b
                    Game.command[params[1]]('X', params[1]),
                    Game.command[params[2]]('O', params[2])
                ]
            else:
                print("Bad parameters!")
                self.start()
        else:
            print("Bad parameters!")
            self.start()

    def process(self):
        # 4. This loop controls the movement by calling 4a/4b method depending on the current player
        # And it calls 4c after each move
        while True:
            for player in self.players:
                player.move(self.fields)
                print(self)
                if self.checker():
                    return None

    def checker(self):
        # This method checks if player wins or not, at every run of the program
        fields = self.fields
        result = ''
        for check in Game.mark:
            # this loop checks the winning conditions for each marks
            # It works by centreing 1 game mark at a time
            if fields[4] == check:
                if (fields[7] == fields[1] == check or
                        fields[3] == fields[5] == check or
                        fields[2] == fields[6] == check or
                        fields[0] == fields[8] == check):
                    result += check
            if fields[6] == check:
                if (fields[7] == fields[8] == check or
                        fields[0] == fields[3] == check):
                    result += check
            if fields[2] == check:
                if (fields[1] == fields[0] == check or
                        fields[5] == fields[8] == check):
                    result += check

        # If there is no win / draw '' is returned and the loop at 4 continues
        if not result and not fields.count(" "):
            print("Draw\n")
            result = "Draw"
        elif result:
            print(result, 'wins\n')
        return result


if __name__ == '__main__':
    # Main driver function for implementation of player vs player and player vs computer
    name = input("Enter your name: ")
    print("Hi, {}".format(name))
    while True:
        print("What you like to play: \n1. Play with computer\n2. Play with player\n3. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            session = Game()

        elif option == "2":
            main()

        elif option == "3":
            print("Thanks for playing!")
            break

        else:
            print("You have entered a wrong choice. ")
