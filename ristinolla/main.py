import random


class Board:
    def __init__(self):
        self.matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.pattern = 0
        self.turn = 1

    def draw(self):
        m = self.matrix

        print(" -----------")
        print(f"| {m[0][0]} | {m[0][1]} | {m[0][2]} |")
        print("|-----------|")
        print(f"| {m[1][0]} | {m[1][1]} | {m[1][2]} |")
        print("|-----------|")
        print(f"| {m[2][0]} | {m[2][1]} | {m[2][2]} |")
        print(" -----------")

    def alt_ai(self):
        m = self.matrix

        for y in range(3):
            for x in range(3):
                if m[y][x] == "X":
                    # Expressions for x axis, columns
                    left = x - 1 if x > 0 else 0
                    right = x + 1 if x < 2 else 2

                    # Expressions for the y axis, rows
                    up = y - 1 if y > 0 else 0
                    down = y + 1 if y < 2 else 2

                    ## ROWS, e.g. X AXEL!!! On the same list in list of lists
                    # If there's an additional X on the left side of the X being checked and not on right
                    if x == 1 and m[y][left] == "X" and m[y][right] == " ":
                        if m[up][left] == "X" and m[down][left] == " ":
                            m[down][left] = "O"
                            return
                        if m[down][left] == "X" and m[up][left] == "X":
                            m[up][left] = "O"
                            return

                        m[y][right] = "O"
                        return
                    # If there's an additional X on the right side of the X being checked and not left
                    if x == 1 and m[y][left] == " " and m[y][right] == "X":
                        if m[up][right] == "X" and m[down][right] == " ":
                            m[down][right] = "O"
                            return
                        if m[down][right] == "X" and m[up][right] == " ":
                            m[up][right] = "O"
                            return

                        m[y][left] = "O"
                        return
                    # If the X is on the left side and there isn't any X on the right
                    if x == 0 and m[y][right] == " ":
                        if y > 0 and m[up][x] == "X" and m[down][x] == " ":
                            m[down][x] = "O"
                            return
                        if y > 0 and m[down][x] == "X" and m[up][x] == " ":
                            m[up][x] = "O"
                            return

                        m[y][right] = "O"
                        return
                    # If X is on the right side and there isn't an X on the left
                    if x == 2 and m[y][left] == " ":
                        if y < 2 and m[up][x] == "X" and m[down][x] == " ":
                            m[down][x] = "O"
                            return
                        if y < 2 and m[down][x] == "X" and m[up][x] == " ":
                            m[up][x] = "O"
                            return

                        m[y][left] = "O"
                        return

                    ## COLUMNS, e.g. Y AXEL!! On different lists in list of lists
                    # If there's an additional X above of the X being checked and not below
                    if y == 1 and m[up][x] == "X" and m[down][x] == " ":
                        if m[up][left] == "X" and m[up][right] == " ":
                            m[up][right] = "O"
                            return
                        if m[up][right] == "X" and m[up][left] == " ":
                            m[up][left] = "O"
                            return

                        m[down][x] = "O"
                        return
                    # If there's an additional X below of the X being checked
                    if y == 1 and m[up][x] == " " and m[down][x] == "X":
                        m[up][x] = "O"
                        return
                    # If the X is on the top row and there isn't an X below
                    if y == 0 and m[down][x] == " ":
                        if m[y][right] == "X" and m[y][left] == " ":
                            m[y][left] = "O"
                            return
                        if m[y][left] == "X" and m[y][right] == " ":
                            m[y][right] = "O"
                            return

                        m[down][x] = "O"
                        return
                    # If X is on the bottom row and there isn't an X above
                    if y == 2 and m[up][x] == " ":
                        m[up][x] = "O"
                        return

                    # If player starts in the middle, fuckery:
                    if y == 1 and x == 1:
                        rand_y = random.randint(0, 2)
                        rand_x = random.randint(0, 2)
                        while m[rand_y][rand_x] != " ":
                            rand_y = random.randint(0, 2)
                            rand_x = random.randint(0, 2)

                        m[rand_y][rand_x] = "O"
                        return

    def update(self, mover, move_x, move_y):
        self.matrix[move_x][move_y] = "X" if mover == "Player" else "O"

    def check_for_winner(self):
        m = self.matrix

        # Rows
        for x in range(3):
            win_check = self.who_won(m[x][0], m[x][1], m[x][2])
            if win_check != 0:
                self.end_game(win_check)

        # Columns
        for x in range(3):
            win_check = self.who_won(m[0][x], m[1][x], m[2][x])
            if win_check != 0:
                self.end_game(win_check)

        # Crosses
        win_check = self.who_won(m[0][0], m[1][1], m[2][2])
        if win_check != 0:
            self.end_game(win_check)

        win_check = self.who_won(m[0][2], m[1][1], m[2][0])
        if win_check != 0:
            self.end_game(win_check)

    def who_won(self, one, two, three):
        if one == "X" and two == "X" and three == "X":
            return 1
        if one == "O" and two == "O" and three == "O":
            return 2

        return 0

    def end_game(self, winner):
        print(f"\n{'AI' if winner == 2 else "You"} won the game!\n")
        self.draw()
        exit()


class Interface:
    def input(self):
        player_input_x = input("Enter row (1-3): ")
        while player_input_x not in ["1", "2", "3"]:
            player_input_x = input("Incorrect input. Enter row (1-3): ")

        print(f"You chose row {player_input_x}!")

        player_input_y = input("Enter column (1-3): ")
        while player_input_y not in ["1", "2", "3"]:
            player_input_y = input("Incorrect input. Enter column (1-3): ")

        print(f"You chose column {player_input_y}!")

        return (int(player_input_x) - 1, int(player_input_y) - 1)


board = Board()
ui = Interface()

while True:
    print("\nTic tac toe!")
    board.draw()
    # Tuple of player coords
    player_input = ui.input()

    spot_check = board.matrix[player_input[0]][player_input[1]]
    # If there's an X or O in the player's chosen spot
    while spot_check == "X" or spot_check == "O":
        print("\nSpot already taken!")
        player_input = ui.input()
        spot_check = board.matrix[player_input[0]][player_input[1]]

    board.update("Player", player_input[0], player_input[1])

    board.check_for_winner()

    board.alt_ai()
