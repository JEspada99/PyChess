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
    print(boardConverted)

    # Variables for the moves
    sqSelected = () #square actually selected
    playerClick = [] #tracker of clicks

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() #get tuple (x, y)
                col = location[0]//SQ_SIZE #col of square
                row = location[1]//SQ_SIZE #row of square
                if sqSelected == (row, col): #click twice
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
            
            # Checkmate, insuficent material, stalemate...
            if board.is_game_over():
                # Message
                running = False #close the game automatically
        
        GraphicEngine.drawGameState(screen, board)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    
