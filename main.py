from UDPClient import UDPClient
from UDPServer import UDPServer
import sys
import pygame
import pygame_menu
import chess
import GraphicEngine
import GameEngine
from GraphicEngine import SQ_SIZE, WIDTH, HEIGHT
from tkinter import *
from tkinter import messagebox

# Initializes the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("white"))
GraphicEngine.loadImages()  # only once

# Initializes chess engine
board = chess.Board()
boardConverted = GraphicEngine.make_matrix(board)

def makeMyTheme():
    # Background image
    myimage = pygame_menu.baseimage.BaseImage(
        image_path="images/menubg.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
    )

    #Make the main menu
    mytheme = pygame_menu.themes.Theme(widget_font=pygame_menu.font.FONT_8BIT, 
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    title_offset=(130,108),
    title_font=pygame_menu.font.FONT_8BIT,
    background_color=myimage
    )  
    return mytheme

def mainMenu():
    menu = pygame_menu.Menu('PyChess', WIDTH, HEIGHT,theme=makeMyTheme())

    menu.add.button('Singleplayer', start_the_game)
    menu.add.button('Multiplayer', multiplayerMenu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

def multiplayerMenu():
    menu = pygame_menu.Menu('PyChess', WIDTH, HEIGHT,theme=makeMyTheme())

    menu.add.button('Create match', createAMultiplayerMatch)
    menu.add.button('Join a match', joinAMultiplayerMatch)
    menu.add.button('Back', main)
    menu.mainloop(screen)

def createAMultiplayerMatch():
    UDPServer()


def joinAMultiplayerMatch():
    cliente = UDPClient()
    cliente.sendAndReceive_msg("hola desde el cliente")


def start_the_game():
    # Variable of the game loop
    running = True

    # Variables for the moves
    sqSelected = ()  # square actually selected
    playerClick = []  # tracker of clicks

    # Generates the first time the game
    GraphicEngine.drawGameState(screen, board)
    pygame.display.flip()

    # Gaming loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()  # get tuple (x, y)
                col = location[0]//SQ_SIZE  # col of square
                row = location[1]//SQ_SIZE  # row of square
                if sqSelected == (row, col):  # click twice
                    GraphicEngine.drawGameState(screen, board)  # demark possible moves
                    pygame.display.flip()
                    sqSelected = ()  # deselect
                    playerClick = []
                else:
                    sqSelected = (row, col)
                    playerClick.append(sqSelected)
                if len(playerClick) == 2:  # second click
                    squareMove = GameEngine.getChessNotation(playerClick[0], playerClick[1])
                    move = chess.Move.from_uci(squareMove)

                    if move in board.legal_moves:
                        board.push(move)
                        print(board)
                    # promotion
                    elif chess.Move.from_uci(squareMove+"q") in board.legal_moves:
                        board.push(chess.Move.from_uci(squareMove+"q"))
                        print(board)

                    sqSelected = ()
                    playerClick = []
                    # update the board
                    GraphicEngine.drawGameState(screen, board)
                    pygame.display.flip()
                elif len(playerClick) == 1:  # mark possible moves
                    movesToPaint = []
                    legal_moves = list(board.legal_moves)
                    # for each legal_move, mark piece's ones
                    for moves in legal_moves:
                        if moves.uci()[:2] == GameEngine.getChessNotationStart(playerClick[0]):
                            possibleXY = GameEngine.getBoardNotation(moves.uci()[2:])
                            movesToPaint.append(possibleXY)
                    GraphicEngine.drawGameState(screen, board, movesToPaint, playerClick[0])
                    pygame.display.flip()

            # Checkmate, insuficent material, stalemate...
            if board.is_game_over():
                # Message
                submenu = pygame_menu.Menu('GameOver', WIDTH//4, HEIGHT//4,theme=pygame_menu.themes.THEME_BLUE)
                submenu.add.button('Return to Menu', main)
                submenu.mainloop(screen)
                submenu.close()
                # Tk().wm_withdraw() #to hide the main window
                # messagebox.showinfo('GameOver','Ok')
                running = False  # close the game automatically
    pass


def main():  
    mainMenu()

if __name__ == "__main__":
    main()
