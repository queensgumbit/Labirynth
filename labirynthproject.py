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
    Text.pack() #cannot display message-just white screen


canvas.bind_all('<Key>', playerMove) #key without specifing a concrete key indicates any key on the key board





text= Text(window, width=400,height=408)
text.pack()

'''def display_Intro():
    label_frame = LabelFrame(window, text='Welcome, the game will start in...', font=('Arial', 20),fg='blue')
    label_frame.pack()

    intro_text1 = Label(label_frame, text='3', font=('Arial', 50),fg='blue')
    intro_text1.pack()
    window.update()
    time.sleep(1)
    intro_text1.destroy()

    intro_text2 = Label(label_frame, text='2', font=('Arial', 50),fg='blue')
    intro_text2.pack()
    window.update()
    time.sleep(1)
    intro_text2.destroy()

    intro_text3 = Label(label_frame, text='1', font=('Arial', 50),fg='blue')
    intro_text3.pack()
    window.update()
    time.sleep(1)
    intro_text3.destroy()

    messagebox.showinfo('Game Start', 'The game starts now!')
    window.destroy()


display_Intro()
'''