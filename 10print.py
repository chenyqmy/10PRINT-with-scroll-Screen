import tkinter as tk
import random, time

root = tk.Tk()
root.title("10Print")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

def draw_line(x, y, size):
    if random.random() > 0.5:
        canvas.create_line(x, y, x+size, y+size)
    else:
        canvas.create_line(x, y+size, x+size, y)
    time.sleep(0.005)
    
size = 20
y_offset = 0
x, y = 0, 0

for y in range(0, 600, size):
    for x in range(0, 600, size):
        draw_line(x, y, size)
        canvas.update()        

if x == 580 and y == 580:
    canvas.move("all",0,-size)
    while True:
        for x in range(0, 600, size):
            draw_line(x, 580, size)
            canvas.update()
        canvas.move("all",0,-size)

root.mainloop()
