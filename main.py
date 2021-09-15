import sys
import pygame
import chess
import GraphicEngine
import GameEngine

# Global variables
WIDTH = HEIGHT = 512 #screen size
DIMENSION = 8 #8x8 board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def main():
    # Initializes the game
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pygame.Color("white"))
    GraphicEngine.loadImages() # only once
    running = True

    # Initializes chess engine
    board = chess.Board()
    boardConverted = GraphicEngine.make_matrix(board)

    # Variables for the moves
    sqSelected = () #square actually selected
    playerClick = [] #tracker of clicks

    # Generates the first time the game
    GraphicEngine.drawGameState(screen, board)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() #get tuple (x, y)
                col = location[0]//SQ_SIZE #col of square
                row = location[1]//SQ_SIZE #row of square
                if sqSelected == (row, col): #click twice
                    GraphicEngine.drawGameState(screen, board) #demark possible moves
                    pygame.display.flip()
                    sqSelected = () #deselect
                    playerClick = []
                else:
                    sqSelected = (row, col)
                    playerClick.append(sqSelected)
                if len(playerClick) == 2: #second click
                    squareMove = GameEngine.getChessNotation(playerClick[0], playerClick[1])
                    move = chess.Move.from_uci(squareMove)
                    if move in board.legal_moves:
                        board.push(move)
                        print(board)
                    sqSelected = ()
                    playerClick = []
                    #update the board
                    GraphicEngine.drawGameState(screen, board)
                    pygame.display.flip()
                elif len(playerClick) == 1: #mark possible moves
                    movesToPaint = []
                    legal_moves = list(board.legal_moves)
                    # for each legal_move, mark piece's ones
                    for moves in legal_moves:
                        if moves.uci()[:2] == GameEngine.getChessNotationStart(playerClick[0]):
                            possibleXY = GameEngine.getBoardNotation(moves.uci()[2:])
                            movesToPaint.append(possibleXY)
                    GraphicEngine.drawGameState(screen, board, movesToPaint)
                    pygame.display.flip()

            # Checkmate, insuficent material, stalemate...
            if board.is_game_over():
                # Message
                running = False #close the game automatically


if __name__ == "__main__":
    main()
    
