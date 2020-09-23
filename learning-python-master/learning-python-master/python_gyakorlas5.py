# -*- coding:Utf-8 -*-
import math
'''
Gyakorlatok

#6.5.               x
Mit csinál az alábbi program abban a négy esetben, melyben előre meghatároztuk, hogy az a 
változó értéke: 1, 2, 3 vagy 15 ? 

if a !=2:
    print 'vesztett'
elif a ==3:
    print 'egy kis türelmet kérek'
else :
print 'nyert'

ha a=1, 3, vagy 15  kiírja, h 'vesztett'
ha a=2, kiírja, h 'nyert'
.................................
6.6.               x
Mit csinálnak ezek a programok ?
a)
a = 5
b = 2
if (a==5) & (b<2):
    print '"&" jelentése "  és"; az "and" szót is használhatjuk '
    
#Ha a=5 és b<2, akkor kiírja a program, hogy "&" jelentése "  és"; az "and" szót is használhatjuk.

b)
a, b = 2, 4
if (a==4) or (b!=4):
    print 'nyert'
elif (a==4) or (b==4):
    print 'majdnem nyert'

# Ha a=4 vagy b nem 4 akkor kiírja, hogy 'nyert'.
# Ha a nem 4, de b 4 akkor kiírja, hogy "majdnem nyert"

c)
a = 1
if not a:
    print ' nyert'
elif a:
    print 'vesztett'

..................................

6.7.               x
Vegyük a  c) programot  a = 0 ­val a = 1 helyett. Mi történik?  Következtessen!
#ha a hamis (a=0), kiírja, h nyert, ha a igaz (nem nulla), kiírja, h vesztett => a=0=hamis, a!=0 = igaz
..................................

6.8.                x/2
Írjon egy programot, ami adott a és b egész korlátok esetén összeadja a 3 és 5 korlátok 
közé  eső többszöröseit. Vegyük például az a=0, b=32 -t →  az eredménynek 0 +15 +30 = 45 ­nek kell lenni.
Módosítsa úgy a programot, hogy az adja össze a 3­-nak vagy az 5­-nek az a és b határok közé esőtöbbszöröseit. 
A 0 és 32 határokkal az eredménynek : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 +24 + 25 + 27 + 30 = 225 ­nek kell lenni.

a=int(input('alsó korlát:   '))     #also korlat
b=int(input('felső korlát:  '))     #felso korlat
c=0                                 #osszeg
for i in range (b-a):
    if (i%3==0) or (i%5==0):
        c=c+(b+i)
print c


6.9.               x
Határozzuk meg, hogy egy év szökőév vagy sem. (Az A év szökőév ha A osztható 4­gyel. 
Viszont nem az, ha A többszöröse 100­nak, kivéve, ha A 400 ­nak többszöröse). 


6.10.               x
Kérje a felhasználótól a nevét és a nemét (F vagy N). Ezektől az adatoktól függően írassa ki a felhasználó nevét 
és «Úr» ­at vagy «Asszony» ­t.

a=raw_input('Mi a becses neve?      ')
b=raw_input('És a neme? (Úr/Asszony)    ')
print a, b

6.11.               x
Kérjük meg a felhasználót, hogy írjon be három hosszúságadatot:   a,   b,   c   ­t.   
Ennek   a   háromhosszúságnak   a   segíts égével   határozza   meg,   hogy   lehet­e   egy   
háromszöget   szerkeszteni.     Majdhatározza   meg,   hogy   ez   a   háromszög:   derékszögű,   
egyenlősz  árú,   egyenlőoldalú  vagy  általánosháromszög. 
Figyelem: egy derékszögű háromszög lehet egyenlősz  árú.


6.12.
Kérjük   meg   a   felhasználót,   hogy  írjon   be   egy   egész   számot.   Ezután     
írassa   ki   ennek   asz  ámnak   vagy   a   négyzetgyökét,   vagy   egy  üzenetet,   
ami   jelzi,   hogy   ennek   a   számnak   a négyzetgyökét nem lehet kiszámolni.

print('6.12.')
a=int(input('Kérem, írjon be egy egész számot!     '))
if (a<0):
    print('Ennek a számnak imaginárius a négyzetgyöke!')
else:
    print sqrt(a)
print('\n')

6.13.               x
Konvertáljuk az iskolai N pontszámot, amit a felhasználó ad meg (péld ául 85­ből 27) egy standardizált 
jeggyé a következő feltételek szerint :

Pont                Értékelés
N >= 80 %               A
80 % > N >= 60 %        B
60 % > N >= 50 %        C
50 % > N >= 40 %        D
N < 40 %                E


6.14.               x
Legyen a következő felsorolás egy lista :['Jean­Michel', 'Marc', 'Vanessa', 'Anne', Maximilien', 'Alexandre­Benoît', 'Louise']
Írjon egy scriptet, ami kiírja ezen nevek mindegyikét  és a karaktereik számát.

t1=['Jean­Michel', 'Marc', 'Vanessa', 'Anne', Maximilien', 'Alexandre­Benoît', 'Louise']
for i in range(len(t1)):
    print t1[i], len(t1[i])

6.15.
Írjon egy programhurkot, ami a felhasználótól kéri a tanulók   érdemjegyeit. A hurok csakakkor   fejeződjön   be,   ha   a   felhasználó  egy   negatív     értéket  ír   be.   

Az  így   beírt   jegyekkel hozzon létre egy listát. Minden új jegy beírása után (tehát minden iterrációnál)    írassa ki a beírt 
jegyek számát, a legnagyobb és a legkisebb jegyet és a jegyek átlagát.

print('6.15')
t1=[]
while (a>=0):
    a=input('Kérem a következő tanuló eredményét!   ')
    t1.append(a)

NINCS KÉSZ


6.16.
Írjon egy scriptet, ami két 10000 kg tömegű test között ható gravitácó erőértékét  íratja ki.
A   testek   közötti   távolságok   5   cm   ­től   (0,05   m)   kezdődő  geometriai   sorozatot   
alkotnak, melynek kvóciense 2.
A gravitációs erőt a következő összefüggés alapján számoljuk: 
F=6,6710−11⋅m⋅m'd2
Példa :
d = .05 m :  ez erő nagysága  2.668 N
d = .1 m  :  ez erő nagysága  0.667 N
d = .2 m  :  ez erő nagysága  0.167 N
d = .4 m  :  ez erő nagysága  0.0417 N
stb.

..............................
«Háromszoros idézőjelek» :
Hogy egy karakterláncba könnyebben szúrjunk be speciális vagy «egzotikus» karaktereket anélk ül, hogy a
backslasht alkalmaznánk, vagy magát a backslasht tudjuk beszúrni, a karakterláncot  háromszoros aposztroffal
vagy háromszoros idézőjellel határolhatjuk:
>>> a1 = """
... Használat: izee[OPTIONS]
... { -h...   -H host
... }"""
>>> print a1
Használat: izee[OPTIONS]
{ -h
  -H host
  }
'''

print('6.15')
t1=[]
a=5
c=0                     #számláló/beírt jegyek száma
min=0
max=5000
while (a>=0):
    a=input('Kérem a következő tanuló eredményét!   ')
    t1.append(a)
    c=c+1
    print c
    print len(t1)
print t1
print('\n')

print('6.8.')                                       #Nem jó!
a=int(input('alsó korlát:   '))     #also korlat
b=int(input('felső korlát:  '))     #felso korlat
c=0                                 #osszeg
for i in range (b-a):
    if (i%3==0) or (i%5==0):
        c=c+(b+i)
print c
print('\n')

print ('6.9.')
a=int(input('Adjon meg egy evszamot!   '))
if (a%4==0):
    print('Isten biza ez egy szokoev!!!')
else:
    print('Elcseszte!')
print('\n')

print ('6.10.')
a=raw_input('Mi a becses neve?      ')
b=raw_input('És a neme? (Úr/Asszony)    ')
print a, b
print('\n')

print('6.11')
a=int(input('Elso adat:   '))
b=int(input('Masodik adat:   '))
c=int(input('Harmadik adat:   '))
d=1
if (a+b<c):
    d=0
elif (a+c<b):
    d=0
elif (b+c<a):
    d=0
if d==0:
    print('A három adott hosszu oldal nem lehet haromszog.')
else:
    print('A harom adott hosszu oldal alkothat haromszoget.')
print('\n')

print('6.12.')
a=int(input('Kérem, írjon be egy egész számot!     '))
if (a<0):
    print('Ennek a számnak imaginárius a négyzetgyöke!')
else:
    print math.sqrt(a)
print('\n')

print('6.13.')
a=int(input('Kerem adja meg a pontszamat!  (Egy es 100 kozotti szam)        '))
if (100>=a>=80):
    print('Az on osztalyzata: A')
elif (a>=60):
    print('Az on osztalyzata: B')
elif (a>=50):
    print('Az on osztalyzata: C')
elif (a>=40):
    print('Az on osztalyzata: D')
elif (40>=a>=1):
    print('Az on osztalyzata: E')
else:
    print('Rossz szamot adott meg!')
print('\n')

print ('6.14')
t1=['Jean-­Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre­-Benoît', 'Louise']
for i in range(len(t1)):
    print t1[i], len(t1[i]),