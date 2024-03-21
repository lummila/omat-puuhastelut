import random


class Player:
    def __init__(self):
        pass


class Ai:
    def __init__(self):
        self.column1 = []
        self.column2 = []
        self.column3 = []

        self.row1 = []
        self.row2 = []
        self.row3 = []

        self.cross1 = []
        self.cross2 = []

        self.possibilities = [
            self.column1,
            self.column2,
            self.column3,
            self.row1,
            self.row2,
            self.row3,
            self.cross1,
            self.cross2,
        ]
        # Random priority in attempts
        random.shuffle(self.possibilities)

    def decision(self, board: tuple):
        self.column1 = [board[0][0], board[1][0], board[2][0]]
        self.column2 = [board[0][1], board[1][1], board[2][1]]
        self.column3 = [board[0][2], board[1][2], board[2][2]]

        self.row1 = [board[0][0], board[0][1], board[0][2]]
        self.row2 = [board[1][0], board[1][1], board[1][2]]
        self.row3 = [board[2][0], board[2][1], board[2][2]]

        self.cross1 = [board[0][0], board[1][1], board[2][2]]
        self.cross2 = [board[0][2], board[1][1], board[2][0]]

        # Going through columns, rows and crosses to find one where there isn't an X
        for dec in self.possibilities:
            if "X" in dec:
                continue

            option = dec
            # Now going through the selected straight to not put an O over one
            for spot in dec:
                if "O" not in spot:
                    return int()


class Board:
    def __init__(self):
        self.matrix = (
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        )

    def draw(self):
        m = self.matrix

        print(" -----------")
        print(f"| {m[0][0]} | {m[0][1]} | {m[0][2]} |")
        print("|-----------|")
        print(f"| {m[1][0]} | {m[1][1]} | {m[1][2]} |")
        print("|-----------|")
        print(f"| {m[2][0]} | {m[2][1]} | {m[2][2]} |")
        print(" -----------")

    def update(self, mover, move_x, move_y):
        self.matrix[move_x][move_y] = "X" if mover == "Player" else "O"


class Interface(Board):
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


player = Player()
ai = Ai()
board = Board()
ui = Interface()

while True:
    print("\nTic tac toe!")
    board.draw()
    player_input = ui.input()

    board.update("Player", player_input[0], player_input[1])
    ai.decision(board.matrix)
