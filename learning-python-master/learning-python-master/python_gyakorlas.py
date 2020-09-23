# -*- coding:Utf-8 -*-
#4.2        x
a=0
print (1)
while (a<6):
    a=a+1
    print (a*7)

#4.3        x
a=1
while (a<16385):
    print a, "euro = ", 1.65*a, "dollar"
    a=a*2

#4.4        x
a=4
b=0
while (b<12):
    b=b+1
    if a<20:
        a=a*3
        print (a)
    else:
        print (a)


#4.5        x
#A derékszögű parallelepipedon maga a téglatest... Retardált!

a=input("Kerem a derekszogu parallelepipedon szelesseget!")
b=input("Kérem a derekszogu parallelepipedon magasságat!") 
c=input("Kerem a derekszogu parallelepipedon hosszusagát!")

print "A derekszogu parallelepipedon terfogata: ", a*b*c
print '\n'

#4.6        x
mp=input("Hany masodperccel szeretne szamolni?")
print "Ez ", mp/60, " perc, ", mp/3600, " ora, ", mp/(3600*24), " nap es ", mp/(3600*24*365), " ev."
print '\n'

#4.7        x
a=0
print (1),
while (a<29):
    a=a+1
    print (a*7),
    if ((a*7)%3==0):
        print "*",
print '\n'

#4.8        x
a=0
print (1),
while (a<49):
    a=a+1
    if ((a*13)%7==0):
        print (a*13),

print '\n'

#4.9        x
a=0
while (a<9):
    a=a+1
    print (a*"*")

print '\n'