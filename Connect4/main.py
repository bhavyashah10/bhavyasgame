import sys
import numpy as np
import pygame
import math

RED=(180,0,0)
BLUE= (0,0,180)
GREEN= (0,180,0)
BLACK = (0,0,0)
pygame.font.init()
myfont = pygame.font.SysFont("SFNSRounded",75)

ROWS = 6
COLUMNS = 7
game_over=False
turn=0

def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

def drop_piece(board, row, column,piece):
    board[row][column] = piece

def is_valid_location(board,col):
    if board[ROWS - 1][col]==0:
        return True
    else:
        return False

def get_next_open_row(board,col):
    for r in range(ROWS):
        if board[r][col]==0:
            return r

def winning_move(board,piece):
    #horizontal win conditions
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    #vertical win conditions
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    #positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    #negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3,ROWS):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

def print_board():
    print(np.flip(board, 0))

def draw_board(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE + SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2),height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(screen, GREEN, (int(c * SQUARESIZE + SQUARESIZE / 2),height- int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

board = create_board()
pygame.init()

SQUARESIZE=100
RADIUS=45

width = COLUMNS*SQUARESIZE
height = (ROWS+1) * SQUARESIZE
size = (width,height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            posx= event.pos[0]
            if turn % 2 == 0:
                pygame.draw.circle(screen, RED,(posx,int(SQUARESIZE/2)),RADIUS )
            else:
                pygame.draw.circle(screen, GREEN,(posx,int(SQUARESIZE/2)),RADIUS )

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn % 2 == 0:
                posx= event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("player 1 wins",1,RED)
                        screen.blit(label,(40,10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("player 2 wins", 1, GREEN)
                        screen.blit(label, (40, 10))
                        game_over = True
            print_board()
            draw_board(board)
            turn += 1

            if game_over:
                pygame.time.wait(4500)