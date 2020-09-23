# -*- coding:Utf-8 -*-

#5.1            x
#Irjon egy programot, ami a kiindulásul fokokban, percekben és másodpercekben megadott sz ögeket radiánba számolja át.

#print ("5.1.")
#fok_egesz=int(input("Hany fok?"))
#perc=int(input("Hany perc?"))
#mp=int(input("Hany masodperc?"))        # Convert to an int immediately.
#fok_tizedes=fok_egesz + (perc + (mp / 60)) / 60
#radian= fok_tizedes*2*3.141592/360
#print ("Az on altal megadott adatok ", radian, "radiannal ekvivalensek.")
#print ('\n')

#5.2            x
#Írjon egy programot, ami a kiindulásul radiánokban megadott szögeket fokokba, percekbe és másodpercekbe számolja át.

#print ("5.2.")
#radian=int(input("Hany radian?"))
#fok_tizedes=radian*360/(2*3.141592)
#fok_egesz=int(fok_tizedes)
#fok_tort=fok_tizedes-fok_egesz          #print ("Fok: ", fok_egesz)         #print ("Fok tort: ", fok_tort)
#perc=int(fok_tort/(1/60))               # 1 perc = 1/60 fok (ahány egészszer megvan benne? a MARADÉK ALSÓ EGÉSZ RÉSZE??)
#maradek=fok_tort-(perc*(1/60))
#mp=int(maradek/((1/60)/60))             #1 mp= 1/60 perc
#print ("Ennyi radian egyenlo ", fok_egesz, " fokkal, ", perc," perccel es ", mp, " masodperccel.")
#print ('\n')

#5.3.           x
#Írjon egy programot, ami Celsius fokokba számolja át a kiindulásul Fahrenheit fokokban kifejezett hőmérsékletet
# és a fordított irányúátalakítást is elvégzi. .Az átalakítás képlete :TF=TC×1,832.


#print ("5.3.")
#b = float(input("Kerem a homersekletet Fahrenheit-ben kifejezve:   "))                    # átalakítás numerikus értékké
#print "         A homerseklet Celsiusban: ", b/1.832

#c=float(input('Most kerem adja meg a homersekletet Celsiusban!    '))
#print "         Koszonom! :) Ez bizony ", c*1.832, " Fahrenheit lesz..."
#print ('\n')

#5.4.           x
#Írjon   egy   programot,   ami   a   bankban   elhelyezett   4,3   %   ­os   kamatozású  tőke   20  év 
#alatt felhalmozódott évi kamatait számolja ki.


#print ("5.4.")
#print '\n'

#5.5            x
#Egy régi indiai legenda szerint a sakkjátékot egy öreg bölcs találta ki. A király meg akartaazt neki kösz  önni 
# és azt mondta, hogy jutalmul bármilyen ajándékot megad érte. Az öreg azt kérte, hogy adjon neki egy kevés rizset 
# öreg napjaira, pontosan annyi szem rizset, hogyaz általa   feltalált   játék   első  kockájára   1   szemet,   
# 2   második   kockára  kettőt,   a  harmadikra négyet, és   így tovább egészen a 64­ik kockáig.


#print ("5.5.")
#print '\n'


# 5.6.              x
# Írjon   egy   programot,   ami   meghatározza,   hogy   egy  karakterlánc   tartalmazza­e   az   «e»karaktert.
b=raw_input("Kerem, adjon meg egy szoveget!   ")

print ("5.6.")
a=0
c=0

while (a<len(b)):
    if (b[a]=='e'):
        c=1
    a=a+1
if (c==0):
    print('     A szoveg nem tartalmaz "e" betut.')
elif (c==1):
    print('     A szoveg tartalmaz "e" betut.')
else:
    print('Something went really-really wrong.')



# 5.7.          x
# Írjon   egy   programot,   ami   megszámolja  az   «e»   karakter   előfordulásainak   számát   egystringben.

print ("5.7.")
a=0                 #szamlalo
c=0                 #e karakterek szama az adott szovegben


while (a<len(b)):
    if (b[a]=='e'):
        c=c+1
    a=a+1

if (c==0):
    print('     A szoveg nem tartalmaz "e" betut.')
else:
    print  '     A szoveg ',c, ' db "e" betut tartalmaz.'


# 5.8.
# Írjon egy programot, ami egy új változóba másol át egy karakterláncot úgy, hogy csillagotsz  úr be a karakterek közé.
# Így péld ául, «gaston»­ból «g*a*s*t*o*n» lesz.

print ("5.8.")
a=0                 #szamlalo
print ("Csillagozva: ")
str2=''
for i in range(len(b)):
    str2=str2+b[i]
    if (i<len(b)-1):
        str2=str2+'*'

print(str2)


# 5.9.Írjon egy programot, ami egy új változóba fordított sorrendben másolja át egy karakterlánckaraktereit.
# Így például «zorglub» ­ból «bulgroz» lesz.

print ("5.9.")
a=0                 #szamlalo
print ("Visszafele: ")
str2=''
for i in reversed(xrange(len(b))):
    str2=str2+b[i]
print str2



# 5.10.
# Az   előző  gyakorlatból   kiindulva  írjon   egy   scriptet,   ami   meghatározza,   hogy   egykarakterlánc   
# palindrom   e   (vagyis   ami   mindkét   irányból   olvasva   ugyan   az),   mint   péld ául«radar» vagy «sós».

print ("5.10.")

# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 

def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 

    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

# Driver code 

ans = isPalindrome(b) 

if ans == 1: 
    print("     Palindrome!") 
else: 
    print("     Not palindrome!")
print '\n'