class Ai:
    def move(self, matrix):
        m = matrix

        for row in range(3):  # Rows
            for column in range(3):  # Columns
                if m[row][column] == "X":  # Found the first X
                    # Expressions for the y axis, rows
                    up = row - 1 if row > 0 else 0
                    up_far = row - 2 if row == 2 else up

                    down = row + 1 if row < 2 else 2
                    down_far = row + 2 if row == 0 else down

                    # Expressions for x axis, columns
                    left = column - 1 if column > 0 else 0
                    left_far = column - 2 if column == 2 else left

                    right = column + 1 if column < 2 else 2
                    right_far = column + 2 if column == 0 else right

                    # X - -
                    # - - -
                    # - - -
                    if row == 0 and column == 0:
                        # X x -
                        # - - -
                        # - - -
                        if m[row][right] == "X" and m[row][right_far] == " ":
                            # X x O
                            # - - -
                            # - - -
                            m[row][right_far] = "O"
                            return
                        # X - -
                        # x - -
                        # - - -
                        if m[down][column] == "X" and m[down_far][column] == " ":
                            # X - -
                            # x - -
                            # O - -
                            m[down_far][column] = "O"
                            return
                        # X - -
                        # - x -
                        # - - -
                        if m[down][right] == "X" and m[down_far][right_far] == " ":
                            # X - -
                            # - X -
                            # - - O
                            m[down_far][right_far] = "O"
                            return
                        # X - x
                        # - - -
                        # - - -
                        if m[row][right] == " " and m[row][right_far] == "X":
                            # X O x
                            # - - -
                            # - - -
                            m[row][right] = "O"
                            return
                        # X - -
                        # - - -
                        # - - x
                        if m[down][right] == " " and m[down_far][right_far] == "X":
                            # X - -
                            # - O -
                            # - - x
                            m[down][right] = "O"
                            return
                        # X - -
                        # - - -
                        # x - -
                        if m[down][column] == " " and m[down_far][column] == "X":
                            # X - -
                            # O - -
                            # x - -
                            m[down][column] = "O"
                            return
                        # X - -
                        # - - -
                        # - - -
                        if m[down][right] == " ":
                            # X - -
                            # - O -
                            # - - -
                            m[down][right] = "O"
                            return

                    # - X -
                    # - - -
                    # - - -
                    if row == 0 and column == 1:
                        # x X -
                        # - - -
                        # - - -
                        if m[row][left] == "X" and m[row][right] == " ":
                            # x X O
                            # - - -
                            # - - -
                            m[row][right] = "O"
                            return
                        # - X x
                        # - - -
                        # - - -
                        if m[row][right] == "X" and m[row][left] == " ":
                            # O X x
                            # - - -
                            # - - -
                            m[row][left] = "O"
                            return
                        # - X -
                        # - x -
                        # - - -
                        if m[down][column] == "X" and m[down_far][column] == " ":
                            # - X -
                            # - x -
                            # - O -
                            m[down_far][column] = "O"
                            return
                        # - X -
                        # - - -
                        # - x -
                        if m[down_far][column] == "X" and m[down][column] == " ":
                            # - X -
                            # - O -
                            # - x -
                            m[down][column] = "O"
                            return
                        # - X -
                        # - - -
                        # - - -
                        if m[down][column] == " ":
                            # - X -
                            # - O -
                            # - - -
                            m[down][column] = "O"
                            return
                        elif m[row][left] == " ":
                            # O X -
                            # - - -
                            # - - -
                            m[row][left] = "O"
                            return

                    # - - X
                    # - - -
                    # - - -
                    if row == 0 and column == 2:
                        # - x X
                        # - - -
                        # - - -
                        if m[row][left] == "X" and m[row][left_far] == " ":
                            # O x X
                            # - - -
                            # - - -
                            m[row][left_far] = "O"
                            return
                        # - - X
                        # - - x
                        # - - -
                        if m[down][column] == "X" and m[down_far][column] == " ":
                            # - - X
                            # - - x
                            # - - O
                            m[down_far][column] = "O"
                            return
                        # - - X
                        # - x -
                        # - - -
                        if m[down][left] == "X" and m[down_far][left_far] == " ":
                            # - - X
                            # - x -
                            # O - -
                            m[down_far][left_far] = "O"
                            return
                        # - - X
                        # - - -
                        # - - -
                        if m[down][left] == " ":
                            # - - X
                            # - O -
                            # - - -
                            m[down][left] = "O"
                            return
                        elif m[row][left] == " ":
                            # - O X
                            # - - -
                            # - - -
                            m[row][left] = "O"
                            return

                    # - - -
                    # X - -
                    # - - -
                    if row == 1 and column == 0:
                        # x - -
                        # X - -
                        # - - -
                        if m[up][column] == "X" and m[down][column] == " ":
                            # x - -
                            # X - -
                            # O - -
                            m[down][column] = "O"
                            return
                        # - - -
                        # X x -
                        # - - -
                        if m[row][right] == "X" and m[row][right_far] == " ":
                            # - - -
                            # X x O
                            # - - -
                            m[row][right_far] = "O"
                            return
                        # - - -
                        # X - -
                        # x - -
                        if m[down][column] == "X" and m[up][column] == " ":
                            # O - -
                            # X - -
                            # x - -
                            m[up][column] = "O"
                            return
                        # - - -
                        # X - -
                        # - - -
                        if m[row][right] == " ":
                            # - - -
                            # X O -
                            # - - -
                            m[row][right] = "O"
                            return

                    # - - -
                    # - X -
                    # - - -
                    if row == 1 and column == 1:
                        # x - -
                        # - X -
                        # - - -
                        if m[up][left] == "X" and m[down][right] == " ":
                            # x - -
                            # - X -
                            # - - O
                            m[down][right] = "O"
                            return
                        # - x -
                        # - X -
                        # - - -
                        if m[up][column] == "X" and m[down][column] == " ":
                            # - x -
                            # - X -
                            # - O -
                            m[down][column] = "O"
                            return
                        # - - x
                        # - X -
                        # - - -
                        if m[up][right] == "X" and m[down][left] == " ":
                            # - - x
                            # - X -
                            # O - -
                            m[down][left] = "O"
                            return
                        # - - -
                        # x X -
                        # - - -
                        if m[row][left] == "X" and m[row][right] == " ":
                            # - - -
                            # x X O
                            # - - -
                            m[row][right] = "O"
                            return
                        # - - -
                        # - X x
                        # - - -
                        if m[row][right] == "X" and m[row][left] == " ":
                            # - - -
                            # O X x
                            # - - -
                            m[row][left] = "O"
                            return
                        # - - -
                        # - X -
                        # x - -
                        if m[down][left] == "X" and m[up][right] == " ":
                            # - - O
                            # - X -
                            # x - -
                            m[up][right] = "O"
                            return
                        # - - -
                        # - X -
                        # - x -
                        if m[down][column] == "X" and m[up][column] == " ":
                            # - O -
                            # - X -
                            # - x -
                            m[up][column] = "O"
                            return
                        # - - -
                        # - X -
                        # - - x
                        if m[down][right] == "X" and m[up][left] == " ":
                            # O - -
                            # - X -
                            # - - x
                            m[up][left] = "O"
                            return
                        # - - -
                        # - X -
                        # - - -
                        if m[up][left] == " ":
                            # O - -
                            # - X -
                            # - - -
                            m[up][left] = "O"
                            return
                        elif m[down][right] == " ":
                            # - - -
                            # - X -
                            # - - O
                            m[down][right]
                            return

                    # - - -
                    # - - X
                    # - - -
                    if row == 1 and column == 2:
                        # - - x
                        # - - X
                        # - - -
                        if m[up][column] == "X" and m[down][column] == " ":
                            # - - x
                            # - - X
                            # - - O
                            m[down][column] = "O"
                            return
                        # - - -
                        # - x X
                        # - - -
                        if m[row][left] == "X" and m[row][left_far] == " ":
                            # - - -
                            # O x X
                            # - - -
                            m[row][left_far] = "O"
                            return
                        # - - -
                        # - - X
                        # - - x
                        if m[down][column] == "X" and m[up][column] == " ":
                            # - - O
                            # - - X
                            # - - x
                            m[up][column] = "O"
                            return
                        # - - -
                        # - - X
                        # - - -
                        if m[row][left] == " ":
                            # - - -
                            # - O X
                            # - - -
                            m[row][left] = "O"
                            return

                    # - - -
                    # - - -
                    # X - -
                    if row == 2 and column == 0:
                        # - - -
                        # x - -
                        # X - -
                        if m[up][column] == "X" and m[up_far][column] == " ":
                            # O - -
                            # x - -
                            # X - -
                            m[up_far][column] = "O"
                            return
                        # - - -
                        # - x -
                        # X - -
                        if m[up][right] == "X" and m[up_far][right_far] == " ":
                            # - - O
                            # - x -
                            # X - -
                            m[up_far][right_far] = "O"
                            return
                        # - - -
                        # - - -
                        # X x -
                        if m[row][right] == "X" and m[row][right_far] == " ":
                            # - - -
                            # - - -
                            # X x O
                            m[row][right_far] = "O"
                            return
                        # - - -
                        # - - -
                        # X - -
                        if m[up][right] == " ":
                            # - - -
                            # - O -
                            # X - -
                            m[up][right] = "O"
                            return
                        elif m[up_far][column] == " ":
                            # O - -
                            # - - -
                            # X - -
                            m[up_far][column] = "O"
                            return

                    # - - -
                    # - - -
                    # - X -
                    if row == 2 and column == 1:
                        # - - -
                        # - - -
                        # x X -
                        if m[row][left] == "X" and m[row][right] == " ":
                            # - - -
                            # - - -
                            # x X O
                            m[row][right] = "O"
                            return
                        # - - -
                        # - x -
                        # - X -
                        if m[up][column] == "X" and m[up_far][column] == " ":
                            # - O -
                            # - x -
                            # - X -
                            m[up_far][column] = "O"
                            return
                        # - - -
                        # - - -
                        # - X x
                        if m[row][right] == "X" and m[row][left] == " ":
                            # - - -
                            # - - -
                            # O X x
                            m[row][left] = "O"
                            return
                        # - - -
                        # - - -
                        # - X -
                        if m[up][column] == " ":
                            # - - -
                            # - O -
                            # - X -
                            m[up][column] = "O"
                            return
                        elif m[row][right] == " ":
                            # - - -
                            # - - -
                            # - X O
                            m[row][right] = "O"
                            return

                    # - - -
                    # - - -
                    # - - X
                    if row == 2 and column == 2:
                        # - - -
                        # - - -
                        # - x X
                        if m[row][left] == "X" and m[row][left_far] == " ":
                            # - - -
                            # - - -
                            # O x X
                            m[row][left_far] = "O"
                            return
                        # - - -
                        # - x -
                        # - - X
                        if m[up][left] == "X" and m[up_far][left_far] == " ":
                            # O - -
                            # - x -
                            # - - X
                            m[up_far][left_far] = "O"
                            return
                        # - - -
                        # - - x
                        # - - X
                        if m[up][column] == "X" and m[up_far][column] == " ":
                            # - - O
                            # - - x
                            # - - X
                            m[up_far][column] = "O"
                            return
                        # - - -
                        # - - -
                        # - - X
                        if m[up][left] == " ":
                            # - - -
                            # - O -
                            # - - X
                            m[up][left] = "O"
                            return
                        elif m[up_far][column] == " ":
                            # - - O
                            # - - -
                            # - - X
                            m[up_far][column] = "O"
                            return

        # If everything else fails, seek out a free spot to put an O to
        for row in range(3):
            for column in range(3):
                if m[row][column] == " ":
                    m[row][column] = "O"
                    return
