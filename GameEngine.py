ranksToRows = {"1":7, "2":6, "3":5, "4":4,
                    "5":3, "6":2, "7":1, "8":0}
rowsToRanks = {v: k for k, v in ranksToRows.items()}
filesToCols = {"a":0, "b":1, "c":2, "d":3,
                "e":4, "f":5, "g":6, "h":7}
colsToFiles = {v: k for k, v in filesToCols.items()}

def getChessNotation(start, end):
        return getRankFile(start[0], start[1]) + getRankFile(end[0], end[1])

def getChessNotationStart(start):
        return getRankFile(start[0], start[1])

def getChessNotationEnd(end):
        return getRankFile(end[0], end[1])

def getRankFile(r, c):
    return colsToFiles[c] + rowsToRanks[r]