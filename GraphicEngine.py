import pygame
import chess

# Global variables
WIDTH = HEIGHT = 512  # screen size
DIMENSION = 8  # 8x8 board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['P', 'R', 'N', 'B', 'K', 'Q', 'p', 'r', 'n', 'b', 'k', 'q']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def drawGameState(screen, board, coordToPaint=None, coordOfMove=None):
    drawBoard(screen)
    drawPieces(screen, board)
    if coordOfMove is not None:
        markWhatToMove(screen, coordOfMove)
    if coordToPaint is not None:
        markPossibleMoves(screen, coordToPaint)

def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row+col)%2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    convertedBoard = make_matrix(board)
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = convertedBoard[row][col]
            if piece != ".": #not empty
                screen.blit(IMAGES[piece], pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def markPossibleMoves(screen, coord):
    for moves in coord:
        color = pygame.Color("red")
        pygame.draw.rect(screen, color, pygame.Rect(moves[1]*SQ_SIZE, moves[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE), width=3)

def markWhatToMove(screen, coord):
    color = pygame.Color("green")
    pygame.draw.rect(screen, color, pygame.Rect(coord[1]*SQ_SIZE, coord[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE), width=3)

# Conversion of the chess board into a matrix
def make_matrix(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo
