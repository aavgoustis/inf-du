#!/usr/bin/env python3

# ==============================================================================
# ÚLOHA:
# Nakreslite pomocou For cyklu šesť zmenšujúcich sa kružníc s totožnými stredmi.
# Dĺžka polomeru najväčšej kružnice sa rovná 60. Polomery ostatných kružníc,
# sa postupne zmenšujú o jednu šestinu, o dve šestiny, o tri šestiny,
# o štyri šestiny a o päť šestín dĺžky vzhľadom na polomer najväčšej kružnice.
# ==============================================================================

# RIEŠENIE:
# 1. Definovať funkciu s argumentmi pre polomer a počet cyklov
# 2. Definovať stred kruhov a polomer prvej kružnice (z toho aj jednu šestinu)
# 3. Vytvoriť 'for' cyklus pomocou funkcie range(), ktorá akceptuje existujúci
# argument pre počet cyklov,
#    1. kde sa pri každom cykle nakreslí kruh s daným polomerom a stredom,
#    2. pri každom cykle sa od polomeru odčíta jedna šestina.
# 4. Privloať funkciu so správnymi argumentmi
# ==============================================================================

# KÓD RIEŠENIA:

# importovať tkinter ako 'tk'. píše sa to rýchlejšie ;)
import tkinter as tk

canvas = tk.Canvas()     # vytvorenie plátna
canvas.pack()            # pripojenie plátna do GUI (Graphical User Interface = grafická aplikácia)

# definícia funkcie 'draw_circles' s argumentmi r (radius) a Range
def draw_circles(r, Range):
    x, y = 150, 150      # definícia stredu všetkých kruhov
    sestina = r // 6     # 'sestina' = 'r' vydelené na *celé číslo* 6-kou

    # for cyklus, ktorý využíva argument Range z 'draw_circles' na udanie počtu cyklov
    for i in range(Range):
        # kruh s polomerom 'r'
        canvas.create_oval(x-r, y-r, x+r, y+r)
        # pri každom cykle odpočítame 1 šestinu od 'r'
        r -= sestina     # to isté ako 'r = r - sestina'

# privolanie funkcie 'draw_circles' s argumentmi 60 a 6 (priemer 60px a zopakovať 6-krát)
draw_circles(60, 6)

tk.mainloop()