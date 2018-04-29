class GameBoard(object):
    def __init__(self):
        self.data = [[0 for i in range(7)] for j in range(6)]
        self.playerTurn = 1
        self.moves = [0 for i in range(7)]

    # modularized for bounds checking and future optimizations
    def pieceAt(self, row, col):
        #return 0 for empty, 1 for P1, 2 for P2, -1 for error
        if row < 0 or row > 5 or col < 0 or col > 6:
            return -1
        return self.data[row][col]

    def rowAt(self, col):
        if col < 0 or col > 6:
            return -1
        if (self.moves[col] > 5):
            return -1
        else:
            return self.moves[col]

    def inBounds(self, row, col):
        if col < 0 or col > 6:
            return False
        if row < 0 or row > 5:
            return False
        return True

    def play(self, col):
        freeRow = self.rowAt(col)
        if freeRow > -1:
            self.data[freeRow][col] = self.playerTurn
            self.moves[col] += 1
            if self.isWin(col):
                return 1
            self.playerTurn = 2 if self.playerTurn == 1 else 1
            return 0
        else:
            for i in range(7):
                if (self.moves[i] <= 5):
                    return -1
            self.playerTurn = -1
            return 1

    def getBoard(self):
        return [col for row in self.data for col in row]

    def getPlayerTurn(self):
        return self.playerTurn

    def printBoard(self):
        for i in range(5,-1,-1):
            print("+---"*7 + "+");
            for j in range(7):
                pieceNum = self.pieceAt(i,j)
                piece = " " if pieceNum == 0 else "x" if pieceNum == 1 else "o"
                print("| " + piece + " ", end='');
            print("|")
        print("+---"*7 + "+");

    def numInDirection(self, col, colDir, rowDir, player):
        playedRow = self.moves[col]-1
        count = 0
        while(self.inBounds(col+colDir, playedRow+rowDir)):
            if (self.pieceAt(playedRow+rowDir,col+colDir) == player):
                count += 1
            else:
                break
            col += colDir
            playedRow += rowDir
        return count

    def isWin(self, col):
        playedRow = self.moves[col]-1
        if playedRow >= 3:
            isWinner = True
            for i in range(playedRow-3, playedRow):
                #make sure turn has not been changed
                if (self.data[i][col] != self.playerTurn):
                    isWinner = False
                    break
            if (isWinner):
                return True
        if self.numInDirection(col,1,0,self.playerTurn) + self.numInDirection(col,-1,0,self.playerTurn) >= 3:
            return True
        if self.numInDirection(col,1,1,self.playerTurn) + self.numInDirection(col,-1,-1,self.playerTurn) >= 3:
            return True
        if self.numInDirection(col,1,-1,self.playerTurn) + self.numInDirection(col,-1,1,self.playerTurn) >= 3:
            return True
        return False
