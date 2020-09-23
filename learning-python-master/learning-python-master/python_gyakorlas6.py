Gyakorlatok :
7.14.
Módosítsa   az   egyik   előző  p éld ában   definiált  dobozTerfogat(x1,x2,x3)  f  üggvényt  úgy,   hogy   3,   2,   1 
argumentummal,  vagy akár argumentum nélk ül is lehessen hívni. Alapértelmezésben  az argumentumértéke legyen 10. 
Például:print dobozTerfogat() az eredmény:  1000 print dobozTerfogat(5.2) az eredmény:  250 print dobozTerfogat(5.2, 3)
az eredmény:  156.0

7.15.
Módosítsa  a  fenti  dobozTerfogat(x1,x2,x3)  f  üggvényt  olymódon, hogy  3, 2  vagy  1  argumentummal
lehessen hívni. Ha egy argumentumot használunk, akkor a dobozt kockának tekintjük (az argumentum akocka  oldala).  
Ha két argumentumot használunk, akkor  a dobozt négyzet alapú prizmának tekintjük.(Ebben az esetben az első argumentum a 
négyzet oldala és a második a prizma magassága). Ha háromargumentumot használunk, akkor a dobozt parallelepipedonnak  tekintjük. 
Például:print dobozTerfogat()az eredmény: ­1 (→ hibajelzés) print dobozTerfogat(5.2)az eredmény: 140.608 p
rint dobozTerfogat(5.2, 3)az eredmény: 81.12 print dobozTerfogat(5.2, 3, 7.4)az eredmény: 115.44

7.16.
Definiálja a karakterCsere(ch,ca1,ca2,kezdo,vegso) 
függvényt, ami a ch karakterláncban valamennyica1  karaktert   a  kezdoindextől   kezdve   a  vegso  indexig   a  ca2  karakterrel   helyettesíti,   
az   utolsó  k étargumentum   elhagyható  (ebben   az   esetben   a   karakterlánc   elejétől   a   végéig   helyettesítendő  a   ca1karakter.) 
Példák a végrehajtásra: 
>>> mondat = 'Ceci est une toute petite phrase.' 
>>> print karakterCsere(mondat, ' ', '*') Ceci*est*une*toute*petite*phrase.
>>> print karakterCsere(mondat, ' ', '*', 8, 12) Ceci est*une*toute petite phrase. 
>>> print karakterCsere(mondat, ' ', '*', 12) Ceci est une*toute*petite*phrase. 
>>> print karakterCsere(mondat, ' ', '*', vegso = 12) Ceci*est*une*toute petite phrase.


7.17.
Definiálja   az   maxElem(lista,kezdo,vegso)   f   üggvényt,   ami   a   paraméterként  átadott   lista   listábólmegadja   
legnagyobb  értékű  elemet.   A  kezdoés  vegso  argumentumok   adják   meg   azt   a   két   indexet,melyek   között   végre   
kell   hajtani   a   keresést.   Közülük   bármelyik   elhagyható  (az   előző  gyakorlathozhasonlóan). 
élda a várt függvényvégrehajtásra:
>>> serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
>>> print maxElem(serie)9
>>> print maxElem(serie, 2, 5)7
>>> print maxElem(serie, 2)8 
>>> print maxElem(serie, vegso =3, kezdo =1)6