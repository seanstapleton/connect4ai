import sys
from board import GameBoard

def playVerbose():
    board = GameBoard()
    print("A Connect4 Game has begun!\n")
    winner = 0
    while (winner <= 0):
        print("Player "+str(board.getPlayerTurn())+" - your move!")
        colnum = input("Which column do you want to play?")
        if (colnum == "q"):
            winner = 0
        else:
            colnum = int(colnum)
            boardMove = board.play(colnum)
            if boardMove < 0:
                print("INVALID MOVE: try again.")
            elif boardMove == 1:
                winner = board.getPlayerTurn()
                if winner == -1:
                    print("It's a tie!")
                else:
                    print("Player " + str(winner) + " wins!")
            else:
                board.printBoard()

def main():
    playVerbose()
    return

if __name__ == "__main__":
    main()
