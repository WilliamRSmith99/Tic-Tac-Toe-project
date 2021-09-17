# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:40:11 2021

@author: WRSmi
"""

import pygame, sys;
pygame.init();

# Constants
X = "T"
WIDTH = 626;
HEIGHT = 442;
clicked_row = 99;
clicked_col = 99;
RED = (255,0,0);
LINE_COLOR = ('black')
bg = pygame.image.load('background1.jpg');
MENU = pygame.image.load('background2.jpg');
MENU = pygame.transform.scale(MENU, (626, 442))
COMPWIN = pygame.image.load('O_win.png')
IWIN = pygame.image.load('X_win.png')
TIE = pygame.image.load('Tie.png')
X= pygame.image.load('cross.png')
Y= pygame.image.load('circle.png')
playing = True


#making the GUI
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(RED);
screen.blit(bg, [0,0]);


#making the board
board = [' ' for x in range(10)]
def draw_lines():
    pygame.draw.line( screen, LINE_COLOR, (175,110), (175,340), 10);
    pygame.draw.line( screen, LINE_COLOR, (275,110), (275,340), 10);
    pygame.draw.line( screen, LINE_COLOR, (90,185), (360,185), 10);
    pygame.draw.line( screen, LINE_COLOR, (90,265), (360,265), 10);
 
#redraws the background
def drawScreen():
    screen.fill(RED);
    screen.blit(bg, [0,0]);
    pygame.display.update();


#inserts the png for X/O
def insertLetter(letter, pos):
    if pos == 1:
        if letter == 'X':
            screen.blit(X, (100, 115))
            board[pos] = letter
        else:
            screen.blit(Y, (100, 115))
            board[pos] = letter
    elif pos == 2:
        if letter == 'X':
            screen.blit(X, (193, 115))
            board[pos] = letter
        else:
            screen.blit(Y, (193, 115))
            board[pos] = letter
    elif pos == 3:
        if letter == 'X':
            screen.blit(X, (286, 115))
            board[pos] = letter
        else:
            screen.blit(Y, (286, 115))
            board[pos] = letter
    elif pos == 4:
        if letter == 'X':
            screen.blit(X, (100, 193))
            board[pos] = letter
        else:
            screen.blit(Y, (100, 193))
            board[pos] = letter
    elif pos == 5:
        if letter == 'X':
            screen.blit(X, (193, 193))
            board[pos] = letter
        else:
            screen.blit(Y, (193, 193))
            board[pos] = letter
    elif pos == 6:
        if letter == 'X':
            screen.blit(X, (286, 193))
            board[pos] = letter
        else:
            screen.blit(Y, (286, 193))
            board[pos] = letter
    elif pos == 7:
        if letter == 'X':
            screen.blit(X, (100, 272))
            board[pos] = letter
        else:
            screen.blit(Y, (100, 272))
            board[pos] = letter
    elif pos == 8:
        if letter == 'X':
            screen.blit(X, (193, 272))
            board[pos] = letter
        else:
            screen.blit(Y, (193, 272))
            board[pos] = letter
    elif pos == 9:
        if letter == 'X':
            screen.blit(X, (286, 272))
            board[pos] = letter
        else:
            screen.blit(Y, (286, 272))
            board[pos] = letter
            
def oWin():
  screen.blit(COMPWIN, (380,221));
  pygame.display.update()  
    
def xWin():
  screen.blit(IWIN, (380,221));
  pygame.display.update()
  
def tied():
    screen.blit(TIE, (380,221));
    pygame.display.update()
   
#checks if the space is occupied
def spaceIsFree(pos):
    return board[pos] == ' '

##DELETE LATER FOR DEBUGGING
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
#converting clicks to moves    
def convertRow(mouseY):
    if (mouseY >= 100 and mouseY<185):
        clicked_row = 0;
        return clicked_row;
    elif ( mouseY > 185 and mouseY < 265):
        clicked_row = 1;
        return clicked_row;
    elif ( mouseY > 265 and mouseY <= 350):
        clicked_row = 2;
        return clicked_row;
    
def convertCol(mouseX):
    if (mouseX >= 80 and mouseX < 175):
        clicked_col = 0;
        return clicked_row;
    elif ( mouseX > 175 and mouseX < 275):
        clicked_col = 1;
        return clicked_row;
    elif ( mouseX > 275 and mouseX <= 370):
        clicked_col = 2;
        return clicked_col;

def convert2Move(clicked_row, clicked_col):
    if clicked_row == 0 and clicked_col == 0:
        return 1;
    elif clicked_row == 0 and clicked_col == 1:
        return 2;
    elif clicked_row == 0 and clicked_col == 2:
        return 3;
    elif clicked_row == 1 and clicked_col == 0:
        return 4;
    elif clicked_row == 1 and clicked_col == 1:
        return 5;
    elif clicked_row == 1 and clicked_col == 2:
        return 6;
    elif clicked_row == 2 and clicked_col == 0:
        return 7;
    elif clicked_row == 2 and clicked_col == 1:
        return 8;
    elif clicked_row == 2 and clicked_col == 2:
        return 9;
      
    
#checks if theres a winner on each turn    
def isWinner(bo, le):
        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

#AI move
def compMove():
    pygame.display.update();
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    ## this checks to see if there is a winning move for either the player or the computer
    ## and plays it if so
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    ## if no winning moves are available, the cpu checks if the corners are
    ## open and assigns a random one
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    ## this checks if the center space is open
    if 5 in possibleMoves:
        move = 5
        return move
    #this checks if any of the edges are open
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    pygame.display.update();
    return move

#AI move uses to chose a spot
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
#checks if board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
#board fade@reset
        
def menuButtons(mouseX,mouseY):
    if mouseY >= 240 and mouseY <= 330:
        if mouseX > 80 and mouseX <=195 :
            return 'Y'
        if mouseX >= 240 and mouseX <=355 :
            return 'N'
        else:
            print("x is off")
    else:
            menuButtons(mouseX, mouseY)

#restart menu    
def menu():
    screen.fill((255,255,255));
    screen.blit(MENU, [0,0]);
    while True:
        pygame.display.update();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit();
            #detects where i click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX= event.pos[0]; #X
                mouseY= event.pos[1]; #Y
                answer= menuButtons(mouseX,mouseY)
                print(answer)
                return answer


#main game function
def main():
    while not isBoardFull(board):
        if not(isWinner(board, 'O') or isWinner(board, 'X')):
            pygame.display.update();
            for event in pygame.event.get():
                draw_lines();
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit();
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX= event.pos[0]; #X
                    mouseY= event.pos[1]; #Y
                    clicked_row = convertRow(mouseY)
                    clicked_col = convertRow(mouseX)
                    if not(isWinner(board, 'O')):
                        try:
                            move = int(convert2Move(clicked_row, clicked_col))
                            if spaceIsFree(move):
                                run = False
                                insertLetter('X', move)
                                pygame.display.update();
                            else:
                                pygame.display.update();
                                print('Sorry, this space is occupied!')
                    
                        except:
                            pygame.display.update();
                            
                            break;
                        printBoard(board)
                    else:
                        print('Sorry, O\'s won this time!')
                        pygame.display.update();
                        oWin();
                        pygame.time.wait(2000) 
                        return 'O'
            
                    if not(isWinner(board, 'X')):
                        move = compMove()
                        if move != 0:
                            insertLetter('O', move)
                            print('Computer placed an \'O\' in position', move , ':')
                            printBoard(board)
                            pygame.display.update();
                        else:
                            print('Tie Game')
                            pygame.display.update();
                            tied();
                            pygame.time.wait(2000)
                            return 'T'
                    else:
                        print('X\'s won this time! Good Job!')
                        xWin();
                        pygame.time.wait(2000)
                        return 'X'
                
                if (isWinner(board, 'O')):
                    print('Sorry, O\'s won this time!')
                    pygame.display.update();
                    oWin();
                    pygame.time.wait(2000)
                    return 'O'
                
                if isBoardFull(board):
                    print('Tie Game!')
                    tied();
                    pygame.time.wait(2000)
                    return 'T'
                
games = 0
while True:
    screen.fill((255,255,255));
    screen.blit(MENU, [0,0]);
    answer= menu()
    games += 1
    if answer.lower() == 'y':
        board = [' ' for x in range(10)]
        drawScreen();
        print('-----------------------------------')
        main()
    else:
        pygame.quit()
        sys.exit();
        pygame.display.update();


