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
