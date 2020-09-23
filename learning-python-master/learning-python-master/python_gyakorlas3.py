# -*- coding:Utf-8 -*-
'''
Gyakorlatok :
5.11.                   x
Legyenek adottak a következő listák:
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'J úlius', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
Írjon egy kis programot, ami egy új t3 listáthoz létre. Ennek felváltva kell tartalmazni a két lista minden elemét úgy, hogy minden hónap nevét követnie kell a   
megfelelő napok számának: ['Január',31,'Február',28,'Március',31, stb...].

5.12.                   x
Írjon egy programot, ami kiíratja egy lista összes elemét. Ha például a fenti gyakorlat 
t2 listájára alkalmaznánk, akkor a következőt kellene kapnunk: 
Január Február Március Április Május Június Július Augusztus Szeptember Október November December

5.13.                   x
Írjon egy programot, ami megkeresi egy adott lista legnagyobb elemét. Például, ha a 
[32,5, 12, 8, 3, 75, 2, 15], listára alkalmaznánk, akkor a következőt kellene kiírnia :
a lista legnagyobb elemének az értéke 75.

5.14.                   x
Írjon   egy   programot,   ami   megvizsgálja   egy   számlista   minden   elemét   
(például   az   előzőpélda   listáját)   azért,   hogy   két    új  listát   hozzon   
létre.   Az  egyik   csak   az   eredeti   lista   páros számait tartalmazza, a másik 
a páratlanokat. Például, ha a kiindulási lista az előző gyakorlatlistája,  akkor a 
programnak  egy  páros listát  kell létrehoznia,  ami a [32, 12, 8, 2]-­t tartalmazza 
és egy páratlan listát ami [5, 3, 75, 15]-­t tartalmazza. 
Trükk: Gondoljon az előzőekben említett modulo (%) operátor használatára!

5.15.                   x
Írjon egy programot, ami egy szavakból álló lista elemeit egyenként megvizsgálja azért,
hogy két  új listát hozzon létre. (például: ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean­Pierre','Sandra'] 
Az egyikben 6 karakternél rövidebb szavakat legyenek, a másikban 6, vagy annáltöbb karaktert tartalmazzonó szavak legyenek.
'''



print ("5.11.")
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Januar', 'Februar', 'Marcius', 'Aprilis', 'Majus', 'Junius', 'Julius', 'Augusztus', 'Szeptember', 'Oktober', 'November', 'December']
t3=[]
for i in range(len(t1)):        #ilyet lehet!!
    t3.append(t1[i])            #hozzáadok egy elemet a listához
    t3.append(t2[i])
print t3
print '\n'



print ("5.12.")
for i in range(len(t2)):
    print t2[i],
print '\n'



print ("5.13.")
max=t1[0]
for i in range(len(t1)):
    if (t1[i]>max):
        max=t1[i]
print max
print '\n'



print ("5.14.")
t1=[1,2,3,4,4,5,6,7,7,8,9]
t2=[]
t3=[]
for i in range(len(t1)):        #ilyet lehet!!
    if (t1[i]%2==0):                #ha ps
        t2.append(t1[i])            #hozzáadom az elemet a ps listához
    else:
        t3.append(t1[i])            #hozzáadom az elemet a pt listához
print t2
print t3
print '\n'



print ("5.15.")
t1=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean­Pierre','Sandra']      #lista
t2=[]       #6 karakternel rovidebb szavak listaja
t3=[]       #6 karakternel hoszabb szavak listaja
for i in range(len(t1)):        #vegigmegyek a lista elemein
    
    if (len(t1[i])<6):       #ha az i. elem hossza ps
        t2.append(t1[i])
    else:
        t3.append(t1[i])

print t2
print t3