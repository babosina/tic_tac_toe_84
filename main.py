def display_board(board) -> None:
    print("  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} {' | '.join(row)}")
        if i < 2:
            print("  ---------")
    print("\n")


def user_input(board) -> tuple[int, int] | None:
    while True:
        try:
            move_row = int(input("Enter row: "))
            move_col = int(input("Enter column: "))
            if move_row not in range(3) or move_col not in range(3):
                print("Invalid input. Try again.")
                continue
            if board[move_row][move_col] != " ":
                print("Already filled. Try again.")
                continue
            return move_row, move_col
        except ValueError:
            print("Invalid input. Values must be integers.")


def make_move(board, row, column, player="X") -> None:
    board[row][column] = player


def check_win(board) -> bool:
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False


def is_board_full(board) -> bool:
    for row in board:
        if " " in row:
            return False
    return True


def initialize_board() -> list:
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


def play_again() -> bool:
    while True:
        choice = input("Would you like to play again? (y/n) ").lower().strip()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        else:
            print("Invalid input. Try again.")


def play_game():
    board = initialize_board()
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player} your move")

        move_row, move_col = user_input(board)
        make_move(board, move_row, move_col, current_player)

        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    print("Welcome to the Tic Tac Toe game!")

    while True:
        play_game()
        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
