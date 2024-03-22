"""
Tic tac toe by Aleksi Lummila!
Initial 1.0 finished 22.3.2024.
"""

from ai import Ai


class Board:
    def __init__(self):
        self.matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.pattern = 0
        self.turn = 1

        self.ai = Ai()

    def draw(self):
        m = self.matrix

        print(" -----------")
        print(f"| {m[0][0]} | {m[0][1]} | {m[0][2]} |")
        print("|-----------|")
        print(f"| {m[1][0]} | {m[1][1]} | {m[1][2]} |")
        print("|-----------|")
        print(f"| {m[2][0]} | {m[2][1]} | {m[2][2]} |")
        print(" -----------")

    def go_first(self):
        self.matrix[1][1] = "O"
        return

    # Using the Ai class imported from ai.py
    def move(self):
        self.ai.move(self.matrix)

    # Update the board with player's input
    def update(self, move_x, move_y):
        self.matrix[move_x][move_y] = "X"

    # Checks for possible win conditions
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

        # Rare case, no one wins:
        for row in range(3):
            for column in range(3):
                if m[row][column] == " ":
                    return

        print("\nIt's a draw!\n")
        self.draw()
        exit()

    # Returns one if three parameters are all "X" and 2 if it's "O", 0 else
    def who_won(self, one, two, three):
        if one == "X" and two == "X" and three == "X":
            return 1
        if one == "O" and two == "O" and three == "O":
            return 2

        return 0

    # Uses who_won() return value set in check_for_winner() to print out the winner and the end board
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

difficulty = input("Enter 'HARD' to let the computer go first! ")
if difficulty == "HARD":
    board.go_first()

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

    board.update(player_input[0], player_input[1])
    board.check_for_winner()

    board.move()
    board.check_for_winner()
