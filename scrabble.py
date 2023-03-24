#scrabble game variation
#   one player: high score per game/set(?)
#   7 letters at a time
#   particular gae can be replicated by making output of letters the same order to keep it fair
#   high score per game/set

import curses
from curses import wrapper
from curses import ascii
from turtle import color
import random

def main(w):
    w.clear()
    
    #create scrabble board: 11x11 for now
    for row in range(12):
        for s in range(11):
            w.addstr("[ ]")
        w.move(row,0)

    min_y = 0
    max_y = 10
    min_x = 1
    max_x = 31    

    #add center STAR  
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    w.addstr(5,16,"*", curses.color_pair(1))

    #TODO:create bonus boxes

    #TODO:randomly generate starting word?
    
    letters = {}
    letterBag = []
    lettersPlayable = []
    lettersPlayed = []
    InitializeLetters(w, letters, letterBag, lettersPlayable)

    # w.refresh(100) #TODO: is this refresh needed?
    #start at middle block?
    w.move(5, 16)


    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key
        
        curs_y, curs_x = curses.getsyx()

        #DIRECTIONAL KEYS
        if key == curses.KEY_DOWN:
            if curs_y < max_y:
                w.move(curs_y + 1, curs_x)
        elif key == curses.KEY_RIGHT:
            if curs_x < max_x:
                w.move(curs_y, curs_x + 3)
        elif key == curses.KEY_LEFT:
            if curs_x > min_x:
                w.move(curs_y, curs_x - 3)
        elif key == curses.KEY_UP:
            if curs_y > min_y:
                w.move(curs_y - 1, curs_x)
        
        #PLAYABLE KEYS
        # elif key == 10: #this is ENTER key
        elif key == 27: #ESC key
            curses.endwin()
            quit()
        elif key == 330: #DEL
            toDelete = curses.ascii.unctrl(w.inch(curs_y,curs_x))
            if toDelete in lettersPlayed:
                lettersPlayed.remove(toDelete)
                lettersPlayable.append(toDelete)
                                
                w.addch(curs_y,curs_x,32)
                w.move(curs_y,curs_x) 
        elif curses.ascii.isalpha(key):            
            key = chr(key).upper()
            
            if key in lettersPlayable:
                lettersPlayed.append(key)
                lettersPlayable.remove(key)
                  
                #move cursor to new block
                if curs_x < max_x:
                    w.addch(key)
                    w.move(curs_y, curs_x + 3)
                elif curs_x == max_x:
                    w.addch(key)
                    w.move(curs_y, curs_x)
        # else:
        #     pass

def InitializeLetters(w, letters, letterBag, lettersPlayable):
    #dictionary of letters {Letter:[distribution,point value]}
    #TODO: should blanks [2, 0] be added?
    letters = {'A':[9,1], 'B':[2,3], 'C':[2,3], 'D':[4,2], 'E':[12,1], 'F':[2,4], 'G':[3,2],
    'H':[2,4], 'I':[9,1], 'J':[1,8], 'K':[1,5], 'L':[4,1], 'M':[2,3], 'N':[6,1], 'O':[8,1],
    'P':[2,3], 'Q':[1,10], 'R':[6,1], 'S':[4,1], 'T':[6,1], 'U':[4,1], 'V':[2,4], 'W':[2,4],
    'X':[1,8], 'Y':[2,4], 'Z':[1,10]}

    for letter in letters.items():
        for num in range(letter[1][0]):
            letterBag.append(letter[0])
    random.shuffle(letterBag)

    for l in range(7):
        lettersPlayable.append(letterBag.pop(0))

    #create available letters
    w.move(12,0)
    for l in range(7):
        w.addstr("[" + lettersPlayable[l] +  "]")

        
        
#execute main
wrapper(main)
        

