#!/usr/bin/env python3

from tkinter import *
from math import sin, cos, radians

gui=Tk()
gui.title("Domáca Úloha z INF 2021-01-12")
gui.geometry("600x500")

canvas = Canvas(gui, width=600, height=500)
canvas.pack()

def buda():
    ## Psia búda
    canvas.create_rectangle(100, 100, 200, 200)

    ## Dvere

    ## Strecha búdy
    canvas.create_line(150, 50, 100, 100)  # strecha 1
    canvas.create_line(150, 50, 200, 100)  # strecha 2

class snehuliak():
    def kruh0():
        ## Nakresli spodný kruh snehuliaka
        k0 = [300, 185, 30]  # x, y, r
        canvas.create_oval(k0[0]-k0[2], k0[1]-k0[2], k0[0]+k0[2], k0[1]+k0[2], fill='lightblue')

    def kruh1():
        ## Nakresli stredný kruh snehuliaka
        k1 = [300, 130, 25]
        canvas.create_oval(k1[0]-k1[2], k1[1]-k1[2], k1[0]+k1[2], k1[1]+k1[2], fill='lightblue')

    def kruh2():
        ## Nakresli vrchný kruh snehuliaka
        k2 = [300, 85, 20]
        canvas.create_oval(k2[0]-k2[2], k2[1]-k2[2], k2[0]+k2[2], k2[1]+k2[2], fill='lightblue')

    def oci():
        ## Nakresli oko0 (ľavé)
        o0 = [292, 83, 2]
        canvas.create_oval(o0[0]-o0[2], o0[1]-o0[2], o0[0]+o0[2], o0[1]+o0[2], fill='black')

        ## Nakresli oko1 (pravé)
        o1 = [308, 83, 2]
        canvas.create_oval(o1[0]-o1[2], o1[1]-o1[2], o1[0]+o1[2], o1[1]+o1[2], fill='black')


## Spusti program
buda()
snehuliak.kruh0()
snehuliak.kruh1()
snehuliak.kruh2()
snehuliak.oci()
gui.mainloop()

## Exit msg
print('EXITED')
