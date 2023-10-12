# Herbstklausur | Informatik Leistungskurs 12 | Merian-Schule | Berlin
## Papierteil
### Aufgabe 1) {___ BE von 5 BE} Notieren Sie die Ausgabe folgender Programmfragmente *zeichengenau*.
```python
# Tipp: range(anzahl) range(start, stop) range(start, stop, step)
a) for _ in range(7): print(7)
b) for _ in range(7): print(7, end='')
c) for _ in range(7, 2): print(7, end='')
d) for _ in range(-7,0): print(7, end='')
e) for _ in range(-7,0,2): print(7, end='')

f) for i in range(7): print(i*'*', end=' ')
g) for i in range(7): print(i*'*')
h) for i in range(5): print(chr(97+i), end='')
   # Tipp: print(chr(97)) schreibt ein 'a'.
i*) for _ in range(7,0,2): print(7, end='')
j*) for i in range(7,0,-2): print(7*i, end='')
```
### Aufgabe 2) {___ BE von 5 BE} Notieren Sie möglichen Quellcode folgenden Ausgaben. Verwenden Sie unbedingt eine Schleifen.
```python
a) +
   +
   +

b) +++++
c) 25 30 35
d) 121 144 169 196 225
e) vv
   vvvv
   vvvvvv
```

### Aufgabe 3) {___ BE von 5 BE} Betrachten Sie die unten dargestellte Turingmaschine.  
![grafik](https://github.com/iulbr/blank/assets/70510036/fc38ec3f-02bb-437c-aeee-7a615e8d1642)  
```python
blank: ' '
start state: q1
table:
  q1:
    ' ': {write: 1, R: q1}
```
a) Beschreiben Sie die Funktion der Maschine in zwei Sätzen.  
b) Wie sieht das Band nach fünf Übergängen aus? Notieren Sie.  
c) Welche Eigenschaft eines Algorithmus ist hier **nicht** erfüllt? Erklären Sie in einem Satz.  

### Aufgabe 4) {___ BE von 5 BE} Betrachten Sie den unten dargestellten Quelltext.  
```python
0   for j in range(7):
1      for i in range(7):
2         if i == 0 or i == 6 or i == j:
3            print(' ', end="")🦄
4         else:
5            print(' ',end="")🍕
6      print()
7   print()
```
a) Erläutern Sie die Wirkung der Zeilen 0, 1, 2 und 3, 4 und 5.  
b) Welcher Buchstabe entsteht und warum ist es kein kyrillisches И?   

### Aufgabe 5) {___ BE von 3 BE} ROT13 
jrypur irefpuvrohat ragfpuyüffryg qvrfra grkg? rexyäera fvr na mjrv ohpufgnora!  

## Am Rechner ohne Netz
### Aufgabe N) {___ BE von N BE} turingmachine.io

### Nützliche Python-Fragmente
```
x = int(input('Zahl bitte: '))
print(x**2)

> python3 main.py
Zahl bitte: 5
25


text = 'seitanwurst'
print(text.find('wurst'))
# Ausgabe> 6


print(ord('a'))    # Ausgabe> 97
print(chr(97))     # Ausgabe> a

plz = 12555
print(f"Wir sind in {plz} Berlin.")
# Ausgabe> Wir sind in 12555 Berlin.

```

## Am Rechner mit Netz
### Aufgabe N) {___ BE von N BE} turingmachine.io
a) Entwerfen Sie eine Turingmaschine (TM), die ein leeres Band mit Einses beschreibt und dabei nach links wandert.  
Kopieren Sie den Quelltext der TM in ihrem Klausurordner.   
b) Entwerfen Sie eine Turingmaschine (TM), die fortlaufend folgendes Muster auf ein leeres Band schreibt .oOo.oOo.oOo. usw.

