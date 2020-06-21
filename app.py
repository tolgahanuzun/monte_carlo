from random import random
import math
import tkinter as tk

loop = 50000
square = 250
root = tk.Tk()
canvas = tk.Canvas(root, width=square,
                   height=square, bg='yellow')


def circle(x, y, r):
    canvas.create_arc(x-r, y-r, x+r, y+r, start=0,
                      extent=90, outline='blue')


def dot(x, y):
    canvas.create_line(x, y, x+1, y, fill='black')


def monte_carlo(loop):
    inside = 0
    for index in range(0,loop):
        x2 = random()**2
        y2 = random()**2
        
        dot(x2*square, y2*square)
        if math.sqrt(x2 + y2) < 1:
            inside += 1

    pi = (float(inside) / loop) * 4
    print(pi)


if __name__ == '__main__':
    circle(5, 250, 245)
    monte_carlo(loop)
    canvas.pack(fill='both', expand=True)
    root.mainloop()
