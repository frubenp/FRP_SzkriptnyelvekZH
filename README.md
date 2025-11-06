# FRP Typing WPM

## NÉV: Feltóti Ruben Péter, EEO220

## Feladat leírása
A program egy magyar mondatot ad, amelyet le kell gépelni.  
A START gomb megnyomása után 3 másodperces visszaszámlálás következik, ha ez lejárt, elindul az időmérés és helyesen be kell írni a fenti szöveget.  
A FINISH gomb megnyomása után a program kiszámolja a gépelési sebességet WPM (words per minute) formában.  
Minden mérés rögzítésre kerül a `frp_eredmenyek.txt` fájlba.  
Az alkalmazás mutatja az utolsó mért WPM értéket és az összes eddigi mérésből számított átlag WPM-et.

## Modulok, függvények

### Saját modul
- `frp_utils.py`

### Saját függvény
- `frp_calc_wpm(chars, seconds)`  
  WPM értéket számol a bevitt karakterszám és az eltelt idő alapján.

### Saját osztály
- `FRPStats`  
  A mért WPM értékek tárolását és az utolsó eredmény visszaadását biztosítja.

### További modulok:
- `random` – mondat kiválasztása
- `time` – időmérés
- `datetime` – ISO timestamp generálás mentéshez
- `tkinter` – grafikus felület és eseménykezelés

## Futtatás
A programot a `main.py` futtatásával lehet indítani.

