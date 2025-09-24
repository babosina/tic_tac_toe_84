class TicTacToe:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.current_player = "X"

    def display_board(self):
        """Display the board in the console"""
        print("  0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i} {' | '.join(row)}")
            if i < 2:
                print("  ---------")
        print("\n")

    def user_input(self) -> tuple[int, int] | None:
        """Get valid input from the current user"""
        while True:
            try:
                move_row = int(input("Enter row: "))
                move_col = int(input("Enter column: "))
                if move_row not in range(3) or move_col not in range(3):
                    print("Invalid input. Try again.")
                    continue
                if self.board[move_row][move_col] != " ":
                    print("Already filled. Try again.")
                    continue
                return move_row, move_col
            except ValueError:
                print("Invalid input. Values must be integers.")

    def make_move(self, row, column) -> None:
        """Make a move"""
        self.board[row][column] = self.current_player

    def check_win(self) -> bool:
        """Check if one of the players has won"""
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_board_full(self) -> bool:
        """Check the tie condition"""
        for row in self.board:
            if " " in row:
                return False
        return True

    def switch_player(self):
        """Switching between players"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.current_player = "X"

    def play_game(self):
        """Play the game"""
        while True:
            self.display_board()
            print(f"Player {self.current_player} your move")

            move_row, move_col = self.user_input()
            self.make_move(move_row, move_col)

            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_board_full():
                self.display_board()
                print("It's a tie!")
                break

            self.switch_player()

    @staticmethod
    def play_again() -> bool:
        while True:
            choice = input("Would you like to play again? (y/n) ").lower().strip()
            if choice in ["y", "yes"]:
                return True
            elif choice in ["n", "no"]:
                return False
            else:
                print("Invalid input. Try again.")

    def start_game(self):
        print("Welcome to the Tic Tac Toe game!")

        while True:
            self.play_game()
            if not self.play_again():
                print("Thanks for playing!")
                break
            self.reset_game()
