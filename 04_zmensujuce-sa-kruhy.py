#!/usr/bin/env python3

### ULOHA 4

from tkinter import *

gui=Tk()
gui.title("INF Domáca Úloha z 2021-12-17")
gui.geometry("600x500")  # šírka a výška okna

canvas = Canvas(gui, width=500, height=500)  # vytvorenie plátna
canvas.pack()            # pripojenie plátna do GUI (Graphical User Interface = grafická aplikácia)

# definícia funkcie 'draw_circles' s argumentmi r (radius) a Range
def draw_circles(r, Range):
    x, y = 250, 250      # stred
    sestnastina = r / 16
    farba1, farba2, farba3, farba4 = 'green', 'blue', 'yellow', 'turquoise'

    for i in range(Range):
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba1)
        r -= sestnastina
        farba1, farba2, farba3, farba4 = farba4, farba1, farba2, farba3

# privolanie funkcie 'draw_circles' s argumentmi 60 a 6 (priemer 60px a zopakovať 6-krát)
draw_circles(160, 12)

gui.mainloop()
