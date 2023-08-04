import Mini_Game as G

def print_board(board):

    print("\n")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print("\n")
 
def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return True, board[i][0]
 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return True, board[0][i]
 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True, board[0][2]
 
    return False, "-"
 
def main():

    board = [["-" for j in range(3)] for i in range(3)]
    player = "X"
 
    while True:
        print_board(board)
 
        move = input(f"Player {player}, enter your move (row column): ")
        row, col = move.split()
        row, col = int(row), int(col)
 
        if board[row][col] != "-":
            print("Invalid move, try again.")
            continue
 
        board[row][col] = player
 
        winner, symbol = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {symbol} wins!")
            break
 
        if all(board[i][j] != "-" for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
 
        player = "O" if player == "X" else "X"


def reset():
    print("-----------------------------------------------------------------")
    print("                            Reset:                               ")
    print("-----------------------------------------------------------------")
    print("                     Choose from the option:")
    print("                       1. Play Again")
    print("                       2. Start Menu")
    print("-----------------------------------------------------------------\n")
    Choose_reset = int(input("Your choice : "))
    if Choose_reset == 1:
        main()
    elif Choose_reset == 2:
        G.main()

if __name__ == "__main__":
    main()
