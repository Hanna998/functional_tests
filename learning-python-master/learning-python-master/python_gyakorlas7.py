(8)Gyakorlatok :
 az előző «Vonalrajzoló» program módosításai.8.1.Hogyan kell módosítani a programot, hogy többé ne legyen cian, 
 maroon és green (cián, barna és zöld)vonal ?8.2.Hogyan kell módosítani a programot, hogy minden vonal 
 vízszintes és párhuzamos legyen ?8.3.Nagyítsa fel a vásznat. Legyen a szélessége 500, a hosszúsága 650 egység. 
 Változtassa meg a vonalakhosszát is úgy, hogy a vászon széléig érjenek.
 8.4.
 Adjon a programhoz egy «drawline2» függvényt, 
 ami egy vörös keresztet rajzol a vászon közepére.Adjon   egy   «Kereső»   nevű  gombot   is   a   programhoz.   
 A   gombra   való  kattintással   kell   kirajzolni   akeresztet !
 
 8.5.
 Az eredeti programban helyettesíts ük a «drawline» («rajzolj egyenest») metódust a «drawrectangle»
 («rajzolj téglalapot») metódussal. Mi történik ?Ugyanígy   próbálja   ki   a   «drawarc»   
 («rajzolj   körívet»)   «drawoval»   («rajzolj   ellipszist»)«drawpolygon»(«rajzolj sokszöget») metódust.
 Mindegyik módszernél adja meg, hogy mit jelölnek a zárójelben megadott paraméterek!
 (Megjegyzés: a sokszög esetében a programon módosítani kell !)
 
 8.6.­
Törölje a «global x1, y1, x2, y2» sort az eredeti program «drawline» függvény  ében. Mi történik? Miért?­ 
Ha a «drawline» függvényt definiáló sorban az «x1, y1, x2, y2»-­t zárójelbe teszi,
függvényparaméterként átadva ezeket a változókat, fog-­e még működni a program? 
(Ne felejtsük  elmódosítani a függvényhívó programsort sem!)­ Mi történik, ha «x1, y1, x2, y2 = 10, 390, 390, 10»  
értékadó  utasítás   van   a   «global   x1,y1, ...»utasítás helyén? Miért? Milyen következtetést tud ebből levonni?

8.7.
a) Írjon egy rövid programot, ami egy fehér hátterű (white) téglalapba rajzolja az 5 olimpiai karikát. 
Egy«Kilépés» gombnak kell bezárni az ablakot.
b)   Módosítsa   a   fenti   programot  úgy, hogy hozzátesz 5 gombot. Minden egyes gomb rajzoljon egykarikát.

8.8.
Készítsen a füzetében egy kétoszlopos táblázatot. A baloldali oszlopba írja be a már megismert osztályok definícióit 
(a paraméterlistájukkal együtt) és a jobboldali oszlopba az osztályok metódusait (aparaméterlistájukkal együtt). 
Hagyjon helyet a későbbi kiegészítésnek.

tKINTER, jENKINS telepítése
8.9.
Irjon egy scriptet az előző alapján, ami egy sakktábl  át (fehéralapon fekete négyzeteket) jelenít meg, amikor egy gombrakattintunk :
(page 92)

8.10.
Az   előző  gyakorlatba  építs ünk   be   még   egy   gombot,   amikorongokat jelenít meg véletlenszerűen a sakktábl  án 
(a gombminden megnyomására egy új korong jelenjen meg)

A program számos ismert elemet tartalmaz: létrehozunk egy  abl1  ablakot, ebben elhelyezünk egy vásznat,amin 
egy  színes  kör, és öt vezérlőgomb van. Vegyük észre, hogy a nyomógomb widget­eket nem rendeljük
változókhoz (ez felesleges lenne, mert nem fogunk rájuk hivatkozni a későbbiekben).
A pack() metódust rögt  önezeknek az objektumoknak a létrehozásakor kell alkalmaznunk.
Az igazi újdonság a script elején definiált mozog() f üggvényben van. A függvény minden egyes hívásakor 
átfogja definiálni a vászonra helyezett «színes kör» objektum koordinátáit   és ez idézi elő az objektum 
animációját. Ez az eljárás jellemző az «objektum orientált» programozásra: Létrehozunk egy objektumot, majd 
metódusok segíts égével módosítjuk a tulajdonságaikat. A «régimódi» procedurális (azaz az objektumok 
használatát nélkülöző) programozásban úgy animáljuk azábr  ákat.   hogy  törölj ük   őket egy  adott  helyen,  majd   
egy   kicsit távolabb  újra  rajzoljuk  őket.  Ezzel  szemben   az«objektum orientált» programozásban ezeket 
a feladatokat azok a classok végzik el automatikusan, melyekbőlaz objektumok származnak és ezért nem kell az 
időnket vesztegetni ezek újraprogramozására.Gyakorlatok :

8.12.

Írjon   egy   programot,   ami   megjelenít   
egy   ablakot   egy   vászonnal.   Legyen   a   vásznon   két   (különbözőméretűés   színű)   kör,   amik   
két    égitestet   reprezentálnak.   Egy­egy   gombbal   lehessen  őket   mozgatniminden   irányba.   A   
vászon   alatt   a   programnak   ki   kell  írni:   
a)   a   két    égitest   közötti   távolságot;   
b)   aközött ük   fellépő  gravitáci  ós   erőt   (Írassuk   ki   az   ablak   felső  részére 
az  égitestek   tömegét   valamint   atávolságskálát). Ebben a gyakorlatban Newton gravitációs 
törvényét kell alkalmazni (lásd a 62. oldalona 42. gyakorlatot és a fizika tankönyvet).

8.13.
A vásznon az egérkattintást detektáló program ötletét felhasználva módosítsa a fenti 
programot úgy,hogy csökkentse a gombok számát: egy égitest elmozdításához legyen elég 
az égitestet kiválasztani egygombbal, majd a vászonra kattintani, hogy a kiválasztott 
égitest arra a helyre kerülj ön, ahová kattintott.8.14.Az előző program bővítése. Jelenítsen 
meg egy harmadik égitestet és mindig írassa ki   minden egyeségitestre   a   ható  eredők   
erőjét   (mindegyik  égitest   mindig   a   másik   kettőáltal   kifejtett   gravitációs 
erőhatása alatt áll !).8.15.Ugyanaz a gyakorlat, mint az előző, két elektromos tölt éssel 
(Coulomb törvény). Adjon lehetőséget atölt és előjel   ének megválasztására !

8.16.
rjon egy programot, ami megjelenít egy ablakot két mezővel: az egyik írja ki a hőmérsékletet 
Celsiusfokban, a másik ugyanazt a hőfokot Fahrenheit fokban. A két hőmérséklet bármelyikét 
megváltoztatvaa másik megfelelően módosuljon. Az átv ált áshoz aTF=TC×1,8032képletet használja. 
Nézzemeg az egyszerű kalkulátoros programot is!


8.23.
Törölje   a   start_it()   függvényben   az  if   flag   ==   0:  utasítást   (és   az   azt   
követő  k ét   sort).   Mi   történik?(Kattintson többször az «Indítás» gombra.) Pr  óbálja meg elmagyarázni, 
hogy mi történik.

8.24.
Módosítsa úgy a programot, hogy a labda minden fordulónál váltsa a színét..

8.25.
Módosítsa úgy a programot, hogy a labda ferde mozgást végezzen, mint amilyet a biliárdasztal szélérőlvisszapattanó biliárdgolyó («cikk­cakk»).

8.26.
Módosítsa úgy a programot, hogy más mozgásokat kapjon. Próbáljon meg pl. körmozgást kapni. (Minta   105.oldal 
gyakorlatában.)Módosítsa  úgy   a   programot,   vagy  írjon   egy   másik   hasonlót,   hogy   anehézs  égi erő 
hatására eső labda mozgását szimulálja, ami visszapattan a földről. Figyelem: ez esetbengyorsuló mozgásokról van szó 

8.27.
Az   előző  scriptekből   mostmár   tud  írni   egy   játékprogramot,   ami   a   következő  k éppen   
működik   :   Kissebességgel   véletlenszerűen   mozog   egy   labda   a   vásznon.   A   játékosnak   meg   kell   
próbálni   az   egérrelrákattintani a labdára. Ha sikerült, akkor kap egy pontot de a labda ettől kezdve egy kicsit 
gyorsabbanmozog és   így tovább. Bizonyos számú kattintás után   áll ítsa le a játékot és   írassa ki az elért pontszámot.

8.28.
Az előző j áték változata : minden alkalommal, amikor a játékosnak sikerült «elkapni», a labda méretekisebb lesz (a színét is megváltoztathatja).

8.29.
Írjon egy programot, amiben több, különb  öző színű labda mozog, amik egymásr  ól   és az oldalfalakrólvisszapattannak.8.30.Tökéletesítse az előző 
gyakorlatok játékait az előbbi algoritmus beépítésével. Most a játékosnak csak apiros labdára kell kattintani. Egy hibás kattintásra (más színű labda 
eltalálására) pontot veszít.8.31.Írjon egy programot, ami a Nap körül különböző k örpály án keringőégitestek (vagy az atommag körülkeringő k ét elektron) 
mozgását szimulálja.8.32.Írjon egy programot, a «kígyójátékra»: egy kígy  ó (egy négyzetekből  áll ó r övid vonal) a négy irány:föl,   le,   balra,   
jobbra   valamelyikében   mozog   a   vásznon.   A   játékos   a   kígy  ó  haladási   irányát   anyílbillentyűkkel   bármikor   megváltoztathatja.   
A   vásznon   «zs  ákmányok»   is   találhatók   (kisvéletlenszerűen   elhelyezett,   mozdulatlan   körök).  Úgy   kell   a   kígy  ót   irányítani,   
hogy   «megegye»   azs  ákmányokat, de ne érjen a vászon széleihez. Amikor a kígyó megeszik egy zsákmányt, egy négyzettelhosszabb   lesz  és   egy  új  
zsákmány   jelenik   meg   valahol.   A   játék   akkor   fejeződik  be,  amikor  a   kígyómegérinti az egyik falat vagy elér egy bizonyos méretet.

8.33.
Az előbbi játék tökéletesítése: a játék akkor is megszakad, ha a kígyóátmetszi önmagát.