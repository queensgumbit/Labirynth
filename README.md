 Labirynthproject.py :

from tkinter import *
import time
import random
from tkinter import messagebox
from levels import levels_list
from playground import window,canvas,walls,keys,doors,exits,players,create_level

currentLevel = 0
create_level(levels_list[currentLevel])


def playerMove(event):
    global currentLevel
    player = players[0]
    key = event.keysym
    x = 0
    y = 0
    if key == 'Up':
        y = -5
    if key == 'Down':
        y = 5
    if key == 'Left':
        x = -5
    if key == 'Right':
        x = 5
    canvas.move(player,x,y)
    for wall in walls:
        x1,y1,x2,y2 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.move(player, -x, -y)
    for key in keys:
        x1,y1,x2,y2 = canvas.coords(key)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete(key)
            keys.remove(key)
            if len(keys) == 0:
                for door in doors:
                    canvas.itemconfig(door, fill='green', outline='green')
    for door in doors:
        x1,y1,x2,y2 = canvas.coords(door)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            if canvas.itemcget(door,'fill') == 'red':
                canvas.move(player, -x, -y)
    for exit in exits:
        x1,y1,x2,y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete('all')
            currentLevel +=1
            if currentLevel < len(levels_list):
                create_level(levels_list[currentLevel])
            elif currentLevel >= len(levels_list):
                canvas.delete('all')
                canvas.after(100, display_victory_message)  # Delay to ensure canvas deletion doesn't interfere

def display_victory_message():
    Text = LabelFrame(window, text='You won the game', font=('Arial', 50), fg='green')
    Text.pack() 

canvas.bind_all('<Key>', playerMove) #key without specifing a concrete key indicates any key on the key board


playground.py :

from tkinter import *

# Import the levels module (assuming levels.py exists and defines level1)
import levels

window = Tk()
window.title("playground")

canvas = Canvas(window, height=350, width=350, relief=SOLID, bg="white")
canvas.pack()

walls = []
doors = []
keys = []
exits = []  # Changed 'exit' to 'exits'
players = []

def create_level(level):
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    x = 0
    y = 0
    for line in level:
        for block in line:
            if block == "W":
                wall = canvas.create_rectangle(x, y, x + 20, y + 20, fill='black', outline='black')
                walls.append(wall)
            elif block == "K":
                key = canvas.create_rectangle(x, y, x + 20, y + 20, fill='yellow', outline='yellow')
                keys.append(key)
            elif block == 'D':
                door = canvas.create_rectangle(x, y, x + 20, y + 20, fill='red', outline='red')
                doors.append(door)
            elif block == 'E':
                exit = canvas.create_rectangle(x, y, x + 20, y + 20, fill='orange', outline='orange')
                exits.append(exit)
            elif block == 'P':
                player = canvas.create_rectangle(x + 1,y + 1,x + 20 -1,y + 20 -1,fill='blue',outline='blue')
                players.append(player)
            x += 20
        y += 20
        x = 0

if __name__ == '__main__':
    level1 = levels.level1  # Assuming levels.py defines level1
    create_level(level1)
    window.mainloop()

levels.py :

level1 = [
    "WWWWWWWWWWWWWWWWWW",
    "WP         WWW   W",
    "WWWWWW WWW WWW W W",
    "WWW    WWW     W W",
    "W    WWWWWWWWW W W",
    "W WWWW     WWWWW W",
    "W WWWW WWW WWWWW W",
    "W  WWW W         W",
    "W  WWW W WWWW WW W",
    "WW WWW W WWWW WWWW",
    "WW     W WK      W",
    "WWWWWWWW WWWWWWWWW",
    "W                W",
    "WWWWW WWWWWW WWWWW",
    "WWWWW   WW   WWWWW",
    "WWWWWDWWWWWWDWWWWW",
    "WWWWW        WWWWW",
    "WWWWWWWWEEWWWWWWWW",
]

level2 = [
       "WWWWWWWWWWWWWW",
    "WP         WWW   W",
    "WWW WWW WWW  ",
    "WWW    WWW     W W",
    "W    WWWWW W W",
    "W WWKW     WWWKW ",
    "W WWWW WWW WWWWW",
    "W  WWW          ",
    "W  WWW  WWWW  ",
    "WW WKW WWWW WWWW",
    "WW     WWK      W",
    "WWWWW WWWWWWWWW",
    "WWW              W",
    "WWWWW WWWWWW WWWWW",
    "WWWWW   WW   WWWWW",
    "WWWWWDWWWWWWDWWWWW",
    "WWEWWW        WWEWW",
]

'''
level3= [  "WWWWWWWWWWWW",
    "W         WWW   W",
    "WWWWWW   K WWW WW W W",
    "WWW    WWW     W W",
    "W       WWWWWW W W",
    "W WWKW     WWWKW W",
    "W W  WWWWW W",
    "W  WWW W      P   W",
    "W  WWW W WWWW WW W",
    "WkW WKW W WWWW WWWW",
    "WW     W WK      W",
    "WWWkWWWW WWWWWWWWW",
    "W                W",
    "WWWWW WWWWWW WWWWW",
    "WWWWW   WW   WWWWW",
    "WWWWWDWWWWWWDWWWWW",
    "WWWWW        WWWWW",
    "WWWWWWWWEEWWWWWWWW",
]

level4=["WWWWWWWWWWWWWWWWWW",
    "W       WWW   W",
    "WWWWWW WWW WWW W W",
    "WWW    WWW     W W",
    "W    WWWWkWWWWW W W",
    "W WWKW     WWWKW W",
    "W WWWW WWW WWWWW W",
    "W  W W         W",
    "W  WWW W WWWW WW W",
    "WW WKW W WWWW WWWW",
    "WWE E     W WK      W",
    "WWWWWWWW WWWWWWWWW",
    "W                W",
    "WWWWW WWWWWW WWWWW",
    "WWWWW   WW   WWWWW",
    "WWWWWDWWWWWWDWWWWW",
    "WWWWW        WWWWW",
    "WWWWWWWWWWPWW",
]'''

levels_list = [level1, level2]

#w-walls,d-doors,k-keys,e-exist,p-player






text= Text(window, width=400,height=408)
text.pack()
