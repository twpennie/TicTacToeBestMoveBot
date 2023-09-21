import math


class Board:
    def __init__(self, turn, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):
        self.turn = turn
        self.move_list = []
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4
        self.pos5 = pos5
        self.pos6 = pos6
        self.pos7 = pos7
        self.pos8 = pos8
        self.pos9 = pos9

    def legal_moves(self):  # creates and returns a list of all open positions
        legals = []
        if self.pos1 == "1":
            legals.append(1)
        if self.pos2 == "2":
            legals.append(2)
        if self.pos3 == "3":
            legals.append(3)
        if self.pos4 == "4":
            legals.append(4)
        if self.pos5 == "5":
            legals.append(5)
        if self.pos6 == "6":
            legals.append(6)
        if self.pos7 == "7":
            legals.append(7)
        if self.pos8 == "8":
            legals.append(8)
        if self.pos9 == "9":
            legals.append(9)
        return legals

    def printboard(self):
        print(f"                {self.pos1} | {self.pos2} | {self.pos3}\n\
               ---|---|---\n\
                {self.pos4} | {self.pos5} | {self.pos6}\n\
               ---|---|---\n\
                {self.pos7} | {self.pos8} | {self.pos9}\n")

    def move(self, pos):
        current_turn = self.turn
        if pos == 1:
            if self.pos1 != "1":
                return "illegal move"
            else:
                self.pos1 = current_turn
                self.move_list.append(pos)
        elif pos == 2:
            if self.pos2 != "2":
                return "illegal move"
            else:
                self.pos2 = current_turn
                self.move_list.append(pos)
        elif pos == 3:
            if self.pos3 != "3":
                return "illegal move"
            else:
                self.pos3 = current_turn
                self.move_list.append(pos)
        elif pos == 4:
            if self.pos4 != "4":
                return "illegal move"
            else:
                self.pos4 = current_turn
                self.move_list.append(pos)
        elif pos == 5:
            if self.pos5 != "5":
                return "illegal move"
            else:
                self.pos5 = current_turn
                self.move_list.append(pos)
        elif pos == 6:
            if self.pos6 != "6":
                return "illegal move"
            else:
                self.pos6 = current_turn
                self.move_list.append(pos)
        elif pos == 7:
            if self.pos7 != "7":
                return "illegal move"
            else:
                self.pos7 = current_turn
                self.move_list.append(pos)
        elif pos == 8:
            if self.pos8 != "8":
                return "illegal move"
            else:
                self.pos8 = current_turn
                self.move_list.append(pos)
        elif pos == 9:
            if self.pos9 != "9":
                return "illegal move"
            else:
                self.pos9 = current_turn
                self.move_list.append(pos)
        else:
            return "illegal move"

        if current_turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def undo_move(self):
        if self.move_list:
            pos = self.move_list.pop()
            if pos == 1:
                self.pos1 = "1"
            elif pos == 2:
                self.pos2 = "2"
            elif pos == 3:
                self.pos3 = "3"
            elif pos == 4:
                self.pos4 = "4"
            elif pos == 5:
                self.pos5 = "5"
            elif pos == 6:
                self.pos6 = "6"
            elif pos == 7:
                self.pos7 = "7"
            elif pos == 8:
                self.pos8 = "8"
            elif pos == 9:
                self.pos9 = "9"
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def winningpos(self):
        # determines if there is a winning position on the board and returns 1 for X wins, -1 for O wins, 0 for tie
        # column win possibilities for X
        if self.pos1 == "X" and self.pos4 == "X" and self.pos7 == "X":
            return 1
        elif self.pos2 == "X" and self.pos5 == "X" and self.pos8 == "X":
            return 1
        elif self.pos3 == "X" and self.pos6 == "X" and self.pos9 == "X":
            return 1

        # row win possibilities for X
        elif self.pos1 == "X" and self.pos2 == "X" and self.pos3 == "X":
            return 1
        elif self.pos4 == "X" and self.pos5 == "X" and self.pos6 == "X":
            return 1
        elif self.pos7 == "X" and self.pos8 == "X" and self.pos9 == "X":
            return 1

        # diagonal win possibilities for X
        elif self.pos1 == "X" and self.pos5 == "X" and self.pos9 == "X":
            return 1
        elif self.pos3 == "X" and self.pos5 == "X" and self.pos7 == "X":
            return 1

        # column win possibilities for O
        if self.pos1 == "O" and self.pos4 == "O" and self.pos7 == "O":
            return -1
        elif self.pos2 == "O" and self.pos5 == "O" and self.pos8 == "O":
            return -1
        elif self.pos3 == "O" and self.pos6 == "O" and self.pos9 == "O":
            return -1

        # row win possibilities for O
        elif self.pos1 == "O" and self.pos2 == "O" and self.pos3 == "O":
            return -1
        elif self.pos4 == "O" and self.pos5 == "O" and self.pos6 == "O":
            return -1
        elif self.pos7 == "O" and self.pos8 == "O" and self.pos9 == "O":
            return -1

        # diagonal win possibilities for O
        elif self.pos1 == "O" and self.pos5 == "O" and self.pos9 == "O":
            return -1
        elif self.pos3 == "O" and self.pos5 == "O" and self.pos7 == "O":
            return -1

        # if draw, return 0
        elif self.pos1 != "1" and self.pos2 != "2" and self.pos3 != "3" and self.pos4 != "4" and self.pos5 != "5" and self.pos6 != "6" and self.pos7 != "7" and self.pos8 != "8" and self.pos9 != "9":
            return 0

        # otherwise, return None
        else:
            return None


# minimax algorithm
searches = 0


def minimax(ismaximizing, board):
    if board.winningpos() is not None:
        return board.winningpos()

    scores = []
    for move in board.legal_moves():
        global searches
        searches += 1
        board.move(move)
        scores.append(minimax(not ismaximizing, board))
        board.undo_move()

    if ismaximizing:
        return max(scores)
    else:
        return min(scores)


# initialize gamerunning variable and make initial empty game board and determine who is playing as X or O

gamerunning = True
gameboard = Board("X", "1", "2", "3", "4", "5", "6", "7", "8", "9")
playerteam = str(input("Would you like to be X or O?\n"))
computer_turn = None
computer_team = None

if playerteam == "X":
    computer_turn = False
    computer_team = "O"
elif playerteam == 'x':
    computer_turn = False
    computer_team = "O"
else:
    computer_team = "X"
    computer_turn = True


# uses minimax to make the best move
def computer_move(computer_team):
    if computer_team == "X":
        best_score = -math.inf
        best_move = None
        for move in gameboard.legal_moves():
            gameboard.move(move)
            score = minimax(False, gameboard)
            gameboard.undo_move()
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for move in gameboard.legal_moves():
            gameboard.move(move)
            score = minimax(True, gameboard)
            gameboard.undo_move()
            if score < best_score:
                best_score = score
                best_move = move
        return best_move


# game running loop
while gamerunning:
    gameboard.printboard()
    if computer_turn:
        print("computer is moving\n")
        gameboard.move(computer_move(computer_team))
        print("computer searched {} gamestates\n".format(searches))
        searches = 0
        computer_turn = False
        if gameboard.winningpos() == 1:
            gameboard.printboard()
            print("X wins! Game over")
            gamerunning = False
        elif gameboard.winningpos() == 0:
            gameboard.printboard()
            print("The game is a draw!")
            gamerunning = False
        elif gameboard.winningpos() == -1:
            gameboard.printboard()
            print("O wins! Game over")
            gamerunning = False
    else:
        playermove = int(input("Please enter your move\n"))
        if gameboard.move(playermove) == "illegal move":
            print("illegal move")
        else:
            gameboard.move(playermove)
            if gameboard.winningpos() == 1:
                gameboard.printboard()
                print("X wins! Game over")
                gamerunning = False
            elif gameboard.winningpos() == 0:
                gameboard.printboard()
                print("The game is a draw!")
                gamerunning = False
            elif gameboard.winningpos() == -1:
                gameboard.printboard()
                print("O wins! Game over")
                gamerunning = False
            else:
                computer_turn = True

gameover = True
while gameover:
    quitkey = input("\nEnter any key to exit\n")
    gameover = False
