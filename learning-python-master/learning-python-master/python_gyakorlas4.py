# -*- coding:Utf-8 -*-
'''
(6)Gyakorlatok:
(Megjegyzés : Mindegyik gyakorlatban használja adatbevitelre a raw_input() f üggvényt !)

6.1.
Írjon egy programot, ami m/sec és km/h ­ba számolja át a felhasználóáltal mérföld/h ­ban megadottsebességet. .  
( 1 mérf  öld = 1609 méter)

6.2.
Írjon egy programot, ami kiszámolja a kerületét  és a területét annak a háromszögnek, melynek 3 oldaláta felhasználó adja meg. 
(Ismétlés : egy háromszög területét a következő formula segíts égével számoljuk ki :
S=sqrt(d⋅(d−a)⋅(d−b)⋅(d−c))
ahol d a kerület felét, a, b, c az oldalak hosszát jelöli).

6.3.
Írjon egy programot, ami kiszámolja egy adott hosszúságú matematikai inga periódusidejét
A periódusidő számolására szolgáló formula a következő: T=2*pi(l/g), 
ahol : l az inga hossza és g a szabadesés gyorsulása a kísérlet helyén.

6.4.
Írjon egy programot, ami értékeket tesz egy listába. Ennek a programnak ciklusban kell 
működni úgy,hogy mindaddig kéri az értékeket, amíg a felhasználótól úgy nem dönt, hogy befejezésként <Entert>
üt. A program a lista kiírásával fejeződik be. Működési példa :

Írjon be egy értéket : 25
Írjon be egy értéket : 18
Írjon be egy értéket : 6284
Írjon be egy értéket : [25, 18, 6284]
'''

a = input('Írjon be egy tetsz leges számot')
if a:
    print("igaz")        #ha a nem 0
else:
    print("hamis")       #ha a=0

# Összetett utasítások <while> - <if> - <elif> - <else>                 #  1

a = input('Válasszon egy számot 1-t l 3-ig (vagy nullát befejezésként) ')                                                             #  4
while (a != 0):           # a != operátor jelentése "nem egyenl  "        #  5
    if (a==1):                                                          #  6
        print ("Ön az egyet választotta ")                                #  7
        print ("els , egyedi, egység ...")                                #  8
    elif (a == 2):                                                        #  9
        print ("Ön a kett t szereti   :")                                 # 10
        print ("pár, páros, duo ...")                                     # 11
    elif (a == 3):                                                        # 12
        print ("Ön a három közül a legnagyobb mellett dönt:")             # 13
        print ("trio, hármas, triplet ...")                               # 14
    else:                                                              # 15
        print ("1 és 3 közötti számot legyen szíves")                     # 16
    a = input('Válasszon egy számot 1-t l 3-ig (vagy 0 befejezésként)     ')                                                         # 18
print ("Ön nullát írt be :")                                              # 19
print ("A gyakorlatnak vége van.")                                        # 20