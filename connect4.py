
red = '\033[1;31;40m' #red
blue = '\033[1;34;40m' #blue
yellow = '\033[1;33;40m' #yellow
white = '\033[1;37;40m' #white
black = '\033[1;30;40m' #black
board = [[blue for i in range(7)] for j in range(6)]
#make player class with name color and last move
#switch player
#player1 is red, player2 is yellow


# Prints out the current game board to the terminal
def print_board(board):
   for row in range(6):
      print('{}-----------------------------'.format(blue))
      row_string = '{}| '.format(blue)
      for column in range(7):
         row_string += '{}O {}| '.format(board[row][column], blue)
      print(row_string[:-1])
   print('-----------------------------')
   print('{}  1   2   3   4   5   6   7'.format(white))

# Gets the next move from the player and adjusts the game board to reflect
# that players move
def get_move(board, color):
   print('Make your move: ')
   move = int(input()) - 1
   if board[5][move] == blue:
      board[5][move] = color
      return [5, move]
   elif board[4][move] == blue:
      board[4][move] = color
      return [4, move]
   elif board[3][move] == blue:
      board[3][move] = color
      return [3, move]
   elif board[2][move] == blue:
      board[2][move] = color
      return [2, move]
   elif board[1][move] == blue:
      board[1][move] = color
      return [1, move]
   elif board[0][move] == blue:
      board[0][move] = color
      return [0, move]
   else:
      print('ERROR TRY AGAIN')

# Checks if the last move made creates a connect 4
# and returns True if so and False if not so
def check_if_winner(board, color, last_move):
   #i and j are the last move row and column respectively
   i = last_move[0]
   j = last_move[1]
   #check for vertical win
   if i < 3:
      match_color = board[i][j] == color
      match1 = board[i][j] == board[i + 1][j]
      match2 = board[i][j] == board[i + 2][j]
      match3 = board[i][j] == board[i + 3][j]
      if (match1 and match2 and match3 and match_color):
         print('{}WINNER!!!{}'.format(color, white))
         return True
   #check for horizontal win
   for column in range(4):
      match_color = board[i][column] == color
      match1 = board[i][column] == board[i][column + 1]
      match2 = board[i][column] == board[i][column + 2]
      match3 = board[i][column] == board[i][column + 3]
      if (match1 and match2 and match3 and match_color):
         print('{}WINNER!!!{}'.format(color, white))
         return True
   #check forward slash
   for column in range(4):
      for row in range(3):
         match_color = board[row][column] == color
         match1 = board[row][column] == board[row + 1][column + 1]
         match2 = board[row][column] == board[row + 2][column + 2]
         match3 = board[row][column] == board[row + 3][column + 3]
         if (match1 and match2 and match3 and match_color):
            print('{}WINNER!!!{}'.format(color, white))
            return True
   #check back slash
   for column in range(3,7):
      for row in range(3):
         match_color = board[row][column] == color
         match1 = board[row][column] == board[row + 1][column - 1]
         match2 = board[row][column] == board[row + 2][column - 2]
         match3 = board[row][column] == board[row + 3][column - 3]
         if (match1 and match2 and match3 and match_color):
            print('{}WINNER!!!{}'.format(color, white))
            return True
   return False

# define our colors
red = '\033[1;31;40m' #red
blue = '\033[1;34;40m' #blue
yellow = '\033[1;33;40m' #yellow
white = '\033[1;37;40m' #white
#black = '\033[1;30;40m' #black

# build our game board 2d list
board = [[blue for i in range(7)] for j in range(6)]

# defines our main while loop condition
winner = False
print('Welcome to Terminal Connect 4')
print()
print_board(board)

# main loop
while(not winner or play_again):
   # red player's turn
   print('{}Red\'s{} turn'.format(red, white))
   last_move = get_move(board, red)
   winner = check_if_winner(board, red, last_move)
   print_board(board)
   if winner:
      print('Want to play again? Y/N')
      response = input()
      if response.upper() == 'Y':
         winner = False
         board = [[blue for i in range(7)] for j in range(6)]
         print_board(board)
      else:
         break
   # yellow player's turn
   print('{}Yellow\'s{} turn'.format(yellow, white))
   last_move = get_move(board, yellow)
   winner = check_if_winner(board, yellow, last_move)
   print_board(board)
   if winner:
      print('Want to play again? Y/N')
      response = input()
      if response.upper() == 'Y':
         winner = False
         board = [[blue for i in range(7)] for j in range(6)]
         print_board(board)
      else:
         break

# End of Program
