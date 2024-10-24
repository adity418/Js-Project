def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("----------")

def check_winner(board, player):

    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for j in range(3)):
            return False
    
def is_board_full(board):
     return all(cell != " " for row in board for cell in row)

def play_game():
     board = [[" " for _ in range(3)] for _ in range(3)]
     current_player = "X"

     while True:
          print_board(board)
          row = int(input(f"Player {current_player}, enter row(0-2): "))
          col = int(input(f"Player {current_player}, enterr column (0-2): "))
   
          if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie")
                break
            current_player = "O" if current_player == "X" else "X"
          else:
              print("That cell is ready occupied. Try again.")

if __name__ =="__main__":
    play_game()