import numpy as np
import constant_values
import random

def get_board(board):

    chessboard = np.array(list(board), dtype=str)
    chessboard = chessboard.reshape(16,16)

    print(chessboard)

    return(chessboard)

def empty_space(chessboard,row,col):
    if chessboard[row][col] == ' ':
        return True
    return False

def white_piece(chessboard,row,col):
    if chessboard[row][col].isupper() and not chessboard[row][col].islower() and not chessboard[row][col] == ' ':
        return True
    return False

def black_piece(chessboard,row,col):
    if chessboard[row][col].islower() and not chessboard[row][col].isupper() and not chessboard[row][col] == ' ':
        return True
    return False

def best_move_white(move_white):
    best_move = []
    score = 0
    for a in move_white:
        if a[4] > score:
            score = a[4]
            best_move.insert(0,[a[0],a[1],a[2],a[3]])
    return best_move
            
def best_move_black(move_black):
    best_move = []
    score = 0
    for a in move_black:
        if a[4] > score:
            score = a[4]
            best_move.insert(0,[a[0],a[1],a[2],a[3]])
    return best_move

def valid_white_move(chessboard):
    move_white = []
    for row in range(16):
        for col in range(16):
            #Peon come en diagonal izq
            if chessboard[row][col] == 'P' and col >= 1 and row >= 1 and black_piece(chessboard,row-1,col-1):
                move_white.append([row,col,row-1,col-1,10])
            #Peon come en diagonal der
            if chessboard[row][col] == 'P' and row >= 1 and col <= 14 and black_piece(chessboard,row-1,col+1):
                move_white.append([row,col,row-1,col+1,10])
            #Peon hace salto de 2 casillas desde fila inicial
            if chessboard[row][col] == 'P' and row == 12 and chessboard[row-1][col] == ' ' and chessboard[row-2][col] == ' ':
                move_white.append([row,col,row-2,col,3])
            if chessboard[row][col] == 'P' and row == 13 and chessboard[row-1][col] == ' ' and chessboard[row-2][col] == ' ':
                move_white.append([row,col,row-2,col,3])
            #Peon mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'P' and row <= 11 and chessboard[row-1][col] == ' ':
                move_white.append([row,col,row-1,col,4])
            if chessboard[row][col] == 'P' and chessboard[row-1][col] == ' ':
                move_white.append([row,col,row-1,col,1])

            #Reina come 1 casilla hacia adelante
            if chessboard[row][col] == 'Q' and row >= 1 and black_piece(chessboard,row-1,col):
                move_white.append([row,col,row-1,col,5])
            #Reina come 1 casilla hacia la derecha
            if chessboard[row][col] == 'Q' and col <= 14 and black_piece(chessboard,row,col+1):
                move_white.append([row,col,row,col+1,5])
            #Reina come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'Q' and col >= 1 and black_piece(chessboard,row,col-1):
                move_white.append([row,col,row,col-1,5])
            #Reina come 1 casilla hacia atras
            if chessboard[row][col] == 'Q' and row <= 14 and black_piece(chessboard,row+1,col):
                move_white.append([row,col,row+1,col,5])
            #Reina come en diagonal izquierda, adelante
            if chessboard[row][col] == 'Q' and col >= 1 and row >=1 and black_piece(chessboard,row-1,col-1):
                move_white.append([row,col,row-1,col-1,5])
            #Reina come en diagonal izquierda, atras
            if chessboard[row][col] == 'Q' and col >= 1 and row <= 14 and black_piece(chessboard,row+1,col-1):
                move_white.append([row,col,row+1,col-1,5])
            #Reina come en diagonal derecha, adelante
            if chessboard[row][col] == 'Q' and col <= 14 and row >= 1 and black_piece(chessboard,row-1,col+1):
                move_white.append([row,col,row-1,col+1,5])
            #Reina come en diagonal derecha, atras
            if chessboard[row][col] == 'Q' and col <= 14 and row <= 14 and black_piece(chessboard,row+1,col+1):
                move_white.append([row,col,row+1,col+1,5])

            #Torre come 1 casilla hacia adelante
            if chessboard[row][col] == 'R' and row >= 1 and black_piece(chessboard,row-1,col):
                move_white.append([row,col,row-1,col,10])
            #Torre come 1 casilla hacia la derecha
            if chessboard[row][col] == 'R' and col <= 14 and black_piece(chessboard,row,col+1):
                move_white.append([row,col,row,col+1,10])
            #Torre come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'R' and col >= 1 and black_piece(chessboard,row,col-1):
                move_white.append([row,col,row,col-1,10])
            #Torre come 1 casilla hacia atras
            if chessboard[row][col] == 'R' and row <= 14 and black_piece(chessboard,row+1,col):
                move_white.append([row,col,row+1,col,10])

            #Torre mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'R' and row >= 1 and chessboard[row-1][col] == ' ':
                move_white.append([row,col,row-1,col,1])
            #Torre mueve 1 casilla hacia la derecha
            if chessboard[row][col] == 'R' and col <= 14 and chessboard[row][col+1] == ' ':
                move_white.append([row,col,row,col+1,1])
            #Torre mueve 1 casilla hacia la izquierda
            if chessboard[row][col] == 'R' and col >= 1 and chessboard[row][col-1] == ' ':
                move_white.append([row,col,row,col-1,1])
            #Torre mueve 1 casilla hacia atras
            if chessboard[row][col] == 'R' and row <= 14 and chessboard[row+1][col] == ' ':
                move_white.append([row,col,row+1,col,2])

            #Alfil come en diagonal izquierda, adelante
            if chessboard[row][col] == 'B' and col >= 1 and row >=1 and black_piece(chessboard,row-1,col-1):
                move_white.append([row,col,row-1,col-1,10])
            #Alfil come en diagonal izquierda, atras
            if chessboard[row][col] == 'B' and col >= 1 and row <= 14 and black_piece(chessboard,row+1,col-1):
                move_white.append([row,col,row+1,col-1,10])
            #Alfil come en diagonal derecha, adelante
            if chessboard[row][col] == 'B' and col <= 14 and row >= 1 and black_piece(chessboard,row-1,col+1):
                move_white.append([row,col,row-1,col+1,10])
            #Alfil come en diagonal derecha, atras
            if chessboard[row][col] == 'B' and col <= 14 and row <= 14 and black_piece(chessboard,row+1,col+1):
                move_white.append([row,col,row+1,col+1,10])

            #Rey come 1 casilla hacia adelante
            if chessboard[row][col] == 'K' and row >= 1 and black_piece(chessboard,row-1,col):
                move_white.append([row,col,row-1,col,10])
            #Rey come 1 casilla hacia la derecha
            if chessboard[row][col] == 'K' and col <= 14 and black_piece(chessboard,row,col+1):
                move_white.append([row,col,row,col+1,10])
            #Rey come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'K' and col >= 1 and black_piece(chessboard,row,col-1):
                move_white.append([row,col,row,col-1,10])
            #Rey come 1 casilla hacia atras
            if chessboard[row][col] == 'K' and row <= 14 and black_piece(chessboard,row+1,col):
                move_white.append([row,col,row+1,col,10])
            #Rey come en diagonal izquierda, adelante
            if chessboard[row][col] == 'K' and col >= 1 and row >=1 and black_piece(chessboard,row-1,col-1):
                move_white.append([row,col,row-1,col-1,10])
            #Rey come en diagonal izquierda, atras
            if chessboard[row][col] == 'K' and col >= 1 and row <= 14 and black_piece(chessboard,row+1,col-1):
                move_white.append([row,col,row+1,col-1,10])
            #Rey come en diagonal derecha, adelante
            if chessboard[row][col] == 'K' and col <= 14 and row >= 1 and black_piece(chessboard,row-1,col+1):
                move_white.append([row,col,row-1,col+1,10])
            #Rey come en diagonal derecha, atras
            if chessboard[row][col] == 'K' and col <= 14 and row <= 14 and black_piece(chessboard,row+1,col+1):
                move_white.append([row,col,row+1,col+1,10])
            
            #Rey mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'K' and row >= 1 and chessboard[row-1][col] == ' ':
                move_white.append([row,col,row-1,col,1])
            #Rey mueve 1 casilla hacia la derecha
            if chessboard[row][col] == 'K' and col <= 14 and chessboard[row][col+1] == ' ':
                move_white.append([row,col,row,col+1,1])
            #Rey mueve 1 casilla hacia la izquierda
            if chessboard[row][col] == 'K' and col >= 1 and chessboard[row][col-1] == ' ':
                move_white.append([row,col,row,col-1,1])
            #Rey mueve 1 casilla hacia atras
            if chessboard[row][col] == 'K' and row <= 14 and chessboard[row+1][col] == ' ':
                move_white.append([row,col,row+1,col,2])
            #Rey mueve en diagonal izquierda, adelante
            if chessboard[row][col] == 'K' and col >= 1 and row >=1 and chessboard[row-1][col-1] == ' ':
                move_white.append([row,col,row-1,col-1,1])
            #Rey mueve en diagonal izquierda, atras
            if chessboard[row][col] == 'K' and col >= 1 and row <= 14 and chessboard[row+1][col-1] == ' ':
                move_white.append([row,col,row+1,col-1,1])
            #Rey mueve en diagonal derecha, adelante
            if chessboard[row][col] == 'K' and col <= 14 and row >= 1 and chessboard[row-1][col+1] == ' ':
                move_white.append([row,col,row-1,col+1,1])
            #Rey mueve en diagonal derecha, atras
            if chessboard[row][col] == 'K' and col <= 14 and row <= 14 and chessboard[row+1][col+1] == ' ':
                move_white.append([row,col,row+1,col+1,1])

    return move_white

def valid_black_move(chessboard):
    move_black = []
    for row in reversed(range(16)):
        for col in reversed(range(16)):
            #Peon come en diagonal izq
            if chessboard[row][col] == 'p' and col <= 14 and row <= 14 and white_piece(chessboard,row+1,col+1):
                move_black.append([row,col,row+1,col+1,10])
            #Peon come en diagonal der
            if chessboard[row][col] == 'p' and col >= 1 and row <= 14 and white_piece(chessboard,row+1,col-1):
                move_black.append([row,col,row+1,col-1,10])
            #Peon hace salto de 2 casillas desde fila inicial
            if chessboard[row][col] == 'p' and row == 3 and chessboard[row+1][col] == ' ' and chessboard[row+2][col] == ' ':
                move_black.append([row,col,row+2,col,3])
            if chessboard[row][col] == 'p' and row == 2 and chessboard[row+1][col] == ' ' and chessboard[row+2][col] == ' ':
                move_black.append([row,col,row+2,col,3])
            #Peon mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'p' and row >= 4 and chessboard[row+1][col] == ' ':
                move_black.append([row,col,row+1,col,4])
            if chessboard[row][col] == 'p' and chessboard[row+1][col] == ' ':
                move_black.append([row,col,row+1,col,1])

            #Reina come 1 casilla hacia adelante
            if chessboard[row][col] == 'q' and row <= 14 and white_piece(chessboard,row+1,col):
                move_black.append([row,col,row+1,col,5])
            #Reina come 1 casilla hacia la derecha
            if chessboard[row][col] == 'q' and col >= 1 and white_piece(chessboard,row,col-1):
                move_black.append([row,col,row,col-1,5])
            #Reina come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'q' and col <= 14 and white_piece(chessboard,row,col+1):
                move_black.append([row,col,row,col+1,5])
            #Reina come 1 casilla hacia atras
            if chessboard[row][col] == 'q' and row >= 1 and white_piece(chessboard,row-1,col):
                move_black.append([row,col,row-1,col,5])
            #Reina come en diagonal izquierda, adelante
            if chessboard[row][col] == 'q' and col <= 14 and row <= 14 and white_piece(chessboard,row+1,col+1):
                move_black.append([row,col,row+1,col+1,5])
            #Reina come en diagonal izquierda, atras
            if chessboard[row][col] == 'q' and col <= 14 and row >= 1 and white_piece(chessboard,row-1,col+1):
                move_black.append([row,col,row-1,col+1,5])
            #Reina come en diagonal derecha, adelante
            if chessboard[row][col] == 'q' and col >= 1 and row <= 14 and white_piece(chessboard,row+1,col-1):
                move_black.append([row,col,row+1,col-1,5])
            #Reina come en diagonal derecha, atras
            if chessboard[row][col] == 'q' and col >= 1 and row >= 1 and white_piece(chessboard,row-1,col-1):
                move_black.append([row,col,row-1,col-1,5])

            #Torre come 1 casilla hacia adelante
            if chessboard[row][col] == 'r' and row <= 14 and white_piece(chessboard,row+1,col):
                move_black.append([row,col,row+1,col,10])
            #Torre come 1 casilla hacia la derecha
            if chessboard[row][col] == 'r' and col >= 1 and white_piece(chessboard,row,col-1):
                move_black.append([row,col,row,col-1,10])
            #Torre come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'r' and col <= 14 and white_piece(chessboard,row,col+1):
                move_black.append([row,col,row,col+1,10])
            #Torre come 1 casilla hacia atras
            if chessboard[row][col] == 'r' and row >=1 and white_piece(chessboard,row-1,col):
                move_black.append([row,col,row-1,col,10])

            #Torre mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'r' and row <= 14 and chessboard[row+1][col] == ' ':
                move_black.append([row,col,row+1,col,1])
            #Torre mueve 1 casilla hacia la derecha
            if chessboard[row][col] == 'r' and col >= 1 and chessboard[row][col-1] == ' ':
                move_black.append([row,col,row,col-1,1])
            #Torre mueve 1 casilla hacia la izquierda
            if chessboard[row][col] == 'r' and col <= 14 and chessboard[row][col+1] == ' ':
                move_black.append([row,col,row,col+1,1])
            #Torre mueve 1 casilla hacia atras
            if chessboard[row][col] == 'r' and row >=1 and chessboard[row-1][col] == ' ':
                move_black.append([row,col,row-1,col,2])

            #Alfil come en diagonal izquierda, adelante
            if chessboard[row][col] == 'b' and col <= 14 and row <= 14 and white_piece(chessboard,row+1,col+1):
                move_black.append([row,col,row+1,col+1,10])
            #Alfil come en diagonal izquierda, atras
            if chessboard[row][col] == 'b' and col <= 14 and row >= 1 and white_piece(chessboard,row-1,col+1):
                move_black.append([row,col,row-1,col+1,10])
            #Alfil come en diagonal derecha, adelante
            if chessboard[row][col] == 'b' and col >= 1 and row <= 14 and white_piece(chessboard,row+1,col-1):
                move_black.append([row,col,row+1,col-1,10])
            #Alfil come en diagonal derecha, atras
            if chessboard[row][col] == 'b' and col >= 1 and row >= 1 and white_piece(chessboard,row-1,col-1):
                move_black.append([row,col,row-1,col-1,10])

            #Rey come 1 casilla hacia adelante
            if chessboard[row][col] == 'k' and row <= 14 and white_piece(chessboard,row+1,col):
                move_black.append([row,col,row+1,col,10])
            #Rey come 1 casilla hacia la derecha
            if chessboard[row][col] == 'k' and col >= 1 and white_piece(chessboard,row,col-1):
                move_black.append([row,col,row,col-1,10])
            #Rey come 1 casilla hacia la izquierda
            if chessboard[row][col] == 'k' and col <= 14 and white_piece(chessboard,row,col+1):
                move_black.append([row,col,row,col+1,10])
            #Rey come 1 casilla hacia atras
            if chessboard[row][col] == 'k' and row >= 1 and white_piece(chessboard,row-1,col):
                move_black.append([row,col,row-1,col,10])
            #Rey come en diagonal izquierda, adelante
            if chessboard[row][col] == 'k' and col <= 14 and row <= 14 and white_piece(chessboard,row+1,col+1):
                move_black.append([row,col,row+1,col+1,10])
            #Rey come en diagonal izquierda, atras
            if chessboard[row][col] == 'k' and col <= 14 and row >= 1 and white_piece(chessboard,row-1,col+1):
                move_black.append([row,col,row-1,col+1,10])
            #Rey come en diagonal derecha, adelante
            if chessboard[row][col] == 'k' and col >= 1 and row <= 14 and white_piece(chessboard,row+1,col-1):
                move_black.append([row,col,row+1,col-1,10])
            #Rey come en diagonal derecha, atras
            if chessboard[row][col] == 'k' and col >= 1 and row >= 1 and white_piece(chessboard,row-1,col-1):
                move_black.append([row,col,row-1,col-1,10])

            #Rey mueve 1 casilla hacia adelante
            if chessboard[row][col] == 'k' and row <= 14 and  chessboard[row+1][col] == ' ':
                move_black.append([row,col,row+1,col,1])
            #Rey mueve 1 casilla hacia la derecha
            if chessboard[row][col] == 'k' and col >= 1 and  chessboard[row][col-1] == ' ':
                move_black.append([row,col,row,col-1,1])
            #Rey mueve 1 casilla hacia la izquierda
            if chessboard[row][col] == 'k' and col <= 14 and  chessboard[row][col+1] == ' ':
                move_black.append([row,col,row,col+1,1])
            #Rey mueve 1 casilla hacia atras
            if chessboard[row][col] == 'k' and row >= 1 and  chessboard[row-1][col] == ' ':
                move_black.append([row,col,row-1,col,2])
            #Rey mueve en diagonal izquierda, adelante
            if chessboard[row][col] == 'k' and col <= 14 and row <= 14 and chessboard[row+1][col+1] == ' ':
                move_black.append([row,col,row+1,col+1,1])
            #Rey mueve en diagonal izquierda, atras
            if chessboard[row][col] == 'k' and col <= 14 and row >= 1 and chessboard[row-1][col+1] == ' ':
                move_black.append([row,col,row-1,col+1,1])
            #Rey mueve en diagonal derecha, adelante
            if chessboard[row][col] == 'k' and col >= 1 and row <= 14 and chessboard[row+1][col-1] == ' ':
                move_black.append([row,col,row+1,col-1,1])
            #Rey mueve en diagonal derecha, atras
            if chessboard[row][col] == 'k' and col >= 1 and row >= 1 and chessboard[row-1][col-1] == ' ':
                move_black.append([row,col,row-1,col-1,1])

    return move_black