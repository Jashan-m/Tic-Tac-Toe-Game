board = [" " for _ in range(9)]
def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| {} | {} | {} |".format(*row))
    print()
def player_move(icon):
    print(f"Your turn player {1 if icon == 'X' else 2}")
    while True:
        choice = int(input("Enter your move (1-9): ").strip()) - 1
        if board[choice] == " ":
            board[choice] = icon
            break
        else:
            print("That space is taken!")
def is_victory(icon):
    win_conditions = [
        [board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]],
        [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]],
        [board[0], board[4], board[8]], [board[2], board[4], board[6]]
    ]
    return [icon, icon, icon] in win_conditions
def is_draw():
    return " " not in board
while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print_board()
        print("X wins! Congratulations!")
        break
    if is_draw():
        print_board()
        print("It's a draw!")
        break
    print_board()
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    if is_draw():
        print_board()
        print("It's a draw!")
        break