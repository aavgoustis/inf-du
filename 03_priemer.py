#!/usr/bin/env python3
### 3. ÚLOHA

zoznam = [10, -700, 230, -500, 1370, -270, 1230, 120, -7040, 2330]

## Najmenšie cislo
najmensie = min(zoznam)
print("najmenšia hodnota je:", najmensie)

## Najväčšie číslo
najvacsie = max(zoznam)
print("najväčšie číslo je:", najvacsie)

## Priemer
def Priemer(zoznam):
    return sum(zoznam) / len(zoznam)

priemer = Priemer(zoznam)
print("Priemer je:", round(priemer, 2))
