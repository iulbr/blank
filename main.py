
# text = input("text? ").lower()
# shift = int(input("shift? "))

#jrypur irefpuvrohat ragfpuyüffryg qvrfra grkg? rexyäera fvr na mjrv ohpufgnora!

text = "jrypurirefpuvrohatragfpuyffrygqvrfragrkg rexyerafvrnamjrvohpufgnora"
shift = 13

ausgabe = ""
for e in text:
  ausgabe += chr((ord(e) - 97 + shift) % 26 + 97)
print(ausgabe)

print("A5, A7, brute force")

for shift in range(26):
  ausgabe=""
  for e in text:
    ausgabe += chr((ord(e) - 97 + shift) % 26 + 97)
  print(shift, ausgabe, "\n\n")

print("\n A1")

print("\na)")
for _ in range(7): print(7)
print("\nb)")
for _ in range(7): print(7, end='')
print("\nc)")
for _ in range(7, 2): print(7, end='')
print("\nd)")
for _ in range(-7,0): print(7, end='')
print("\ne)")
for _ in range(-7,0,2): print(7, end='')

print("\nf)")
for i in range(7): print(i*'*', end=' ')
print("\ng)")
for i in range(7): print(i*'*')
print("\nh)")
for i in range(5): print(chr(97+i), end='')
   # Tipp: print(chr(97)) schreibt ein 'a'.
print("\ni)")
for _ in range(7,0,2): print(7, end='')
print("\nj)")
for i in range(7,0,-2): print(7*i, end='')


print("\n A2")
print("\n a)")
for i in range(3): print('+')

print("\n b)")
for i in range(5): print('+', end='')

print("\n c)")
for i in range(25,40,5): print(i, end=' ')

print("\n d)")
for i in range(11,16): print(i**2, end=' ')

print('\n e)')
for i in range(1,4): print('v'*i)

print('\n A4')

for j in range(7):
    for i in range(7):
        if i == 0 or i == 6 or i == j:
            print(' ', end="🦄")
        else:
            print(' ',end="🍕")
    print()
print()

'''
Zeile 0: 7 Zeilen. j nimmt die Werte 0..6 an.
Zeile 1: 7 Zeichen pro Zeile. i nimmt auch die Werte 0..6 an.
Zeile 2-3: Ein Pferd, falls i 0, 6 oder gleich j. Falls i 0 bedeutet immer
das erste Zeichen jeder Zeile. Also die erste Spalte, ein senkrechter Strich. 
Falls i 6 analog ein senkrechter Strich in der letzten Spalte.
i gleich j setzt Pferde auf Position (2,2), (3,3) usw. 
Also zweites Zeichen, zweite Zeile. Eine links oben beginnende Diagonale.
Die Diagonale in И startet links unten.
'''

print('\n A5')

'''
jrypur irefpuvrohat ragfpuyüffryg qvrfra grkg? 
rexyäera fvr na mjrv ohpufgnora!

welche verschiebung entschlüsselt diesen text? 
erklären sie an zwei buchstaben!

Das deutsche Alphabet hat 26 Buchstaben. 
Die Verschiebung -- oder Rotation, wenn man an eine Caesar-Scheibe denkt --
erzeugte ein symmetrische Zuordnung.

abcde fghij klm
nopgq stuvw xyz

Sie kann von oben nach unten und umgekehrt gelesen werden.

Aus dem Wort "an" wird "na."
'''

print('\n A6')
'''
a) Die While-Schleife wird ausgeführt, solange ihre Bedingung erfüllt ist. 
Hier: Das Wort "Ende" ist nicht in text enthalten. 
Groß- oder Kleinschreibung wird nicht beachtet.
b) Siehe a) und .lower() ist eine Python-Methode aller Zeichenketten, 
die alle Buchstaben der Kette kleinschreibt.
'''
print("AazZ".lower())
# schreibt: "aazz"  

print('\n A7')
text = "jrypurirefpuvrohatragfpuyffrygqvrfragrkg rexyerafvrnamjrvohpufgnora"
shift = 13

ausgabe = ""
for klar_buchstabe in text:
    ascii_klar = ord(klar_buchstabe) 
    ascii_geheim = ascii_klar + shift
    pos_in_alphabet_geheim  = (ascii_geheim - 97) % 26     # 97 = ord('a')
    geheim_buchstabe = chr(pos_in_alphabet_geheim + 97)  
    ausgabe += geheim_buchstabe
print(ausgabe)


ausgabe = ""
for e in text:
  ausgabe += chr((ord(e) - 97 + shift) % 26 + 97)
print(ausgabe)

print("A5, A7, brute force")

for shift in range(26):
  ausgabe=""
  for e in text:
    ausgabe += chr((ord(e) - 97 + shift) % 26 + 97)
  print(shift, ausgabe, "\n\n")


print('\n A8')


print('\n A8a)')
'''
blank: ' '
start state: q1
table:
  q1:
    ' ': {write: 1, L: q1}
'''


print('\n A8b)')
'''
blank: ' '
start state: q1
table:
  q1:
    ' ': {write: '.', R: q2}
  q2:
    ' ': {write: 'o', R: q3}
  q3:
    ' ': {write: 'O', R: q4}
  q4:
    ' ': {write: 'o', R: q1}
'''

'''
'''

print('\n A9)')


def papagei(text):
  return 2*text

text = ''
while text.lower().find('ende') < 0:
  text = input('Was ist? ')
  print('Rrrhhaa rrhhaaa ', end='')
  print(papagei(text))
print("Rrrhaa. Aufff Wiederrrrrssehn.")
