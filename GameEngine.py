# (x, y) to chess notation
ranksToRows = {"1":7, "2":6, "3":5, "4":4,
                    "5":3, "6":2, "7":1, "8":0}
rowsToRanks = {v: k for k, v in ranksToRows.items()}
filesToCols = {"a":0, "b":1, "c":2, "d":3,
                "e":4, "f":5, "g":6, "h":7}
colsToFiles = {v: k for k, v in filesToCols.items()}

# Chess notation to (x, y)
ranksToRowsInverted = {7:"1", 6:"2", 5:"3", 4:"4",
                        3:"5", 2:"6", 1:"7", 0:"8"}
rowsToRanksInverted = {v: k for k, v in ranksToRowsInverted.items()}
filesToColsInverted = {0:"a", 1:"b", 2:"c", 3:"d",
                        4:"e", 5:"f", 6:"g", 7:"h"}
colsToFilesInverted = {v: k for k, v in filesToColsInverted.items()}

def getChessNotation(start, end):
        return getRankFile(start[0], start[1]) + getRankFile(end[0], end[1])

def getChessNotationStart(start):
        return getRankFile(start[0], start[1])

def getChessNotationEnd(end):
        return getRankFile(end[0], end[1])

def getRankFile(r, c):
    return colsToFiles[c] + rowsToRanks[r]

def getBoardNotation(square):
        return getRankFileInverted(square[0], square[1])

def getRankFileInverted(r, c):
        return (rowsToRanksInverted[c], colsToFilesInverted[r])