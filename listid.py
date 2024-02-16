from random import *

# ----------------------------------------------------------------------
##2 Loetelu

# vanus_list = []
# vanus_summa = 0
# vanus_list1 = []
# nimi_list = []
##2v
##while True:
##    if len(nimi_list) < 5:
##        nimi = input("Sisatege nimi : ")
##        if len(nimi_list) != 0:
##            if nimi_list.count(nimi) != 0:
##                print("See nimi on juba olemas.")
##                pass
##            else:
##                nimi_list.append(nimi)
##                pass
##        else:
##            nimi_list.append(nimi)
##            pass
##    else:
##        break
##1v
# for i in range(5):
#    nimi = input("Sisatege nimi : ")
#    nimi_list.append(nimi)

# print(f"{sorted(nimi_list)}")
# print(f"Viimane nimi on {nimi_list[4]}")
# while True:
#    print("Vaata lehte(0)\nNime muuta(1)\nVanusenimede lisamine(2)\nKorduva nime kustutamine(3)\nLoo vanusenimekiri(4)\nBreak(5)")
#    v = int(input("Mida te tahate? "))
#    if v == 1:
#        v = input("Millist nime soovite muuta? ")
#        nimi_len = -1
#        for i in nimi_list:
#            nimi_len += 1
#            if v == str(i):
#                print(f"Mis nimele sa {v} muuta tahad? ", end="")
#                uus_nimi = input("")
#                nimi_list.remove(v)
#                nimi_list.insert(nimi_len, uus_nimi)
#                print(nimi_list)
#    elif v == 0:
#        nimi_len = len(nimi_list)
#        for i in range(nimi_len):
#            if vanus_list[i] in vanus_list:
#                print(f"{nimi_list[i]} - {vanus_list[i]}")
#            else:
#                print(nimi_list[i])
#    elif v == 2:
#        for i in range(5):
#            print(f"kui vana '{nimi_list[i]}' on? ", end="")
#            vanus = int(input(""))
#            vanus_list.append(vanus)
#        print(nimi_list)
#        print(vanus_list)
#    elif v == 3:
#        nimi_set = set(nimi_list)
#        nimi_list = list(nimi_set)
#        print(nimi_list)
#    elif v == 4:
#        v = int(input("Kui palju vanuseid? "))
#        for i in range(v):
#            vanus1 = input("Mitu ")
#            vanus_list1.append(vanus1)
#        vanus_list1_sorted = sorted(vanus_list1,reverse=True)
#        for i in vanus_list1:
#            vanus_summa += int(i)
#        print(f"{vanus_list1_sorted[0]} on suurim vanus, {vanus_list1_sorted[-1]} on väikseim vanus. {vanus_summa} on summa , " )
#    elif v == 5:
#        break

# 3 Tärnid
# from random import *

# arvud = []
# N = int(input("Mitu rida joonistame? "))
# S = input("Sisestage sümbolit: ")
# for p in range(N):
#    arvud.append(randint(1, 100))
# for p in range(N):
#    print(arvud[p] * S)


# ----------------------------------------------------------------------
##4 Postindeks

# linnad = ["Tallinn",
# ["Narva","Narva-Jõesuu"],
# "Kohtla-Järve",
# ["Ida-Virumaa","Lääne-Virumaa","Jõgevamaa"],
# "Tartu linn",
# ["Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa"],
# ["Viljanimaa","Järvamaa","Harjumaa","Raplamaa"],
# "Pärnymaa",
# ["Läänemaa","Hiiumaa","Sareaa"]
# ]
# indeksid = [1,2,3,4,5,6,7,8,9]
# v_indeksid = [1,2,3]

# vastus = ""
# while len(vastus) != 5:
#    vastus = input("Sisesta sulle indeksit: ")
#    if vastus[0] == "0":
#        print("Teie esimene number ei ole õige!")
#        print("Kõik olulised linnade indeksid - \n-------------------------\n")
#        for i in range(8):
#            print(f"{linnad[i]} - {indeksid[i]}")
#        print("\n-------------------------\n")
#    elif len(vastus) < 5 or len(vastus) > 5:
#        print("Indeks on vale")

# for i in range(8):
#    if vastus[0] == str(indeksid[i]):
#        print(f"Sinu linn on {linnad[i]}")
#    if i < 2:
#        if vastus[0] == str(v_indeksid[i]):
#            print("Püsige kodus!")
#            break
#        else:
#            print("Kandke maske!")
#            break

# ----------------------------------------------------------------------
##5 Vahetus

# lst = []
# while True:
#    print("Lisa elementi (0)\nLõpetada (1)\n")
#    v = int(input("Mida te tahate? "))
#    if v:
#        if len(lst) <= 1:
#            print("Pead lisama vähemalt 2 elementi!")
#        else:
#            break
#    else:
#        v = input("Mida soovite lisada? ")
#        lst.append(v)
#        print(lst)

# while True:
#    v = int(input("Mitu elementi soovite vahetada?"))
#    if type(len(lst) / v) == float:
#        print("vale arv")
#    else:
#        for i in range(v):
#            ov = (i + 1) * -1
#            el_elem = lst[i]
#            vi_elem = lst[ov]

#            lst.insert(i, vi_elem)
#            lst.pop(i + 1)

#            lst.insert(ov, el_elem)
#            lst.pop(ov)

#            print(lst)
#            print(f"muutunud {el_elem} ja {vi_elem} kohta")
#        break

# ----------------------------------------------------------------------
##6: Бесполезные числа

# 1v for
# lst = []
# v = int(input("Kui palju numbreid te nimekirjas soovite?"))
# for i in range(v):
#    v = int(input("Arv: "))
#    lst.append(v)
# suur = 0
# for el in lst:
#    if el > suur:
#        suur = el
# print(f"suur {suur}, indeks on {lst.index(suur) + 1}\n{lst}")
# lst[lst.index(suur)] = suur / len(lst)

##2v sort
# lst = []
# v = int(input("Kui palju numbreid te nimekirjas soovite?"))
# for i in range(v):
#    v = int(input("Arv: "))
#    lst.append(v)
# lst.sort()
# print(f"suur {lst[-1]}, indeks on {lst.index(lst[-1]) + 1}\n{lst}")
# lst[lst.index(lst[-1])] = lst[-1] / ( len(lst) + 1 )

# ----------------------------------------------------------------------
##7 Sorteerimine

# v = int(input("Sisestage arv: "))
# lst = []
# for i in range(v):
#    lst.append(i)

# while True:
#    v = int(input("Kuidas sa nimekirja näha tahad? Kas kahanevas järjekorras(0) või taassünnikorras(1)?"))
#    if v:
#        break

# ----------------------------------------------------------------------
##8 Võrdsepikkusega elemendid

lst = [['крот', 'белка', 'выхухоль'], ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']]
suur = 0
indks = 0

for i in range(len(lst)):
   suur = 0
   for j in lst[i]:
       suur = len(j)
       for x in lst[i]:
           if len(x) < suur:
               indks = lst[i].index(x)
               len_el = suur - len(x)
               lst[i][indks] += "_" * len_el

print(lst)

# ----------------------------------------------------------------------
# 9: Nimi kontroll
konsonantid = ["Q","R","T","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","W"]
vokaalid = ["A","U","E","O","I","Ü","Õ","Ä","Ö","Y","Ä"]


tyhik = 0
vokaali = 0
konsonanti = 0
sumbolid = 0

breek = False
arv = 0
indeks = 0
nimi = ""

while breek == False:
   nimi = input("Mis sinu nimi on? ")
   indeks = 0
   arv = 0
   for i in nimi:
       indeks += 1
       if int(i.isnumeric()):
           arv += 1
   if len(nimi) == indeks:
       if arv == 0:
           breek = True
print(f"Tere {nimi.capitalize()}!")

sona_len = len(nimi)
sona_list = list(nimi)
for i in sona_list:
   if i == " ":
       tyhik += 1
   else:
       for vokaal_sona in vokaalid:
           if str(i).upper() == str(vokaal_sona):
               vokaali += 1
       for konsonanti_sona in konsonantid:
           if str(i).upper() == str(konsonanti_sona):
               konsonanti += 1

sumbolid = sona_len - konsonanti - vokaali - tyhik

print(f"[{nimi}] : tühikud on {tyhik}, vokaalid on {vokaali}, konsonantid on {konsonanti}; sumbolid on {sumbolid}")


# 10

lst = [["Aadu Suur",56,2500],["Malle Kapsas",42,1500],["Uudo Koba",32,700],["Tiit Kopikas",22,550],["Vahur Vana",67,870]]
maks = 0
suur = 0
keskm = 0


while True:
   print("Teada saada kõrgeima palgaga töötaja nimi ja summa (0)\nSaada teada keskmine palk (1)\nTeada keskmisest palgast rohkem teenijate arvu (2)\nTeada keskmised vanused eraldi neile, kes teenivad keskmisest palgast vähem (3)\nLõpetama (4) ")
   v = int(input("\nMida sa näha tahad?"))
   if v == 0:
       for x in range(len(lst)):
           indeks = -1
           for i in lst:
               for j in lst[x]:
                   indeks += 1
                   if indeks == 2:
                       if j > maks:
                           maks = i
       print(f"nimi: {maks[0]}, palga suuruse: {maks[2]}\n-------------------")
   elif v == 1:
       zar_plat = 0
       for x in range(len(lst)):
           indeks = -1
           for i in lst:
               for j in lst[x]:
                   indeks += 1
                   if indeks == 2:
                       zar_plat += 1
                       suur += j
       keskm = suur / zar_plat
       print(f"-------------------\nKeskmise palg on: {keskm}\n-------------------")
   elif v == 2:
       if keskm == 0:
           print("-------------------\nAlustuseks arvutage keskmine palk, kirjutage (1)\n-------------------")
           continue
       else:
           suur = 0
           for x in range(len(lst)):
               indeks = -1
               for i in lst:
                   for j in lst[x]:
                       indeks += 1
                       if indeks == 2:
                           if j > keskm:
                               suur += 1
       print(f"-------------------\nkeskmisest palgast rohkem teenijate arvu on {suur}\n-------------------")

   elif v == 3:
       suur = 0
       maks = 0
       if keskm == 0:
           print("-------------------\nAlustuseks arvutage keskmine palk, kirjutage (1)\n-------------------")
           continue
       else:
           for x in range(len(lst)):
               indeks = -1
               for i in lst:
                   for j in lst[x]:
                       indeks += 1
                       if indeks == 2:
                           if j <= keskm:
                               suur += i[1]
                               maks += 1
       x = suur / maks
       print(f"keskmised vanused eraldi neile, kes teenivad keskmisest palgast vähem (või samapalju) : {x}")
   elif v == 4:
       break

# 11

sona_list = ["a","b","c","d", "e", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
indeks = -1
for j in sona_list:
   indeks += 1
   sona_list[indeks] = j * (indeks + 1)

# 12

lst = []

for i in range(10):
   lst.append(randint(1,100))
maks = 0
mini = 0

for el in lst:
   if mini != 0:
       if el > maks:
           maks = el
       elif el < mini:
           mini = el
   else:
       mini = el
print(f"max {maks}, min {mini}")
print(lst)

maks_indeks = lst.index(maks)
min_indeks = lst.index(mini)

lst.insert(maks_indeks, mini)
lst.pop(maks_indeks + 1)

lst.insert(min_indeks, maks)
lst.pop(min_indeks + 1)

print(lst, "uue")

# 13

kas_sona_on = False
permission = True
while True:
    if kas_sona_on == False:
        katsed = 0
        sonad_list = ["Juhatus", "Ema", "Puu", "Tiiger"]
        rand_sona = [sonad_list[randint(0, len(sonad_list) - 1)], ""]
        condition = [0, 0]
        lst = []

        for i in rand_sona[0]:
            if i != " ":
                rand_sona[1] += "_"
                condition[0] += 1
            else:
                rand_sona[1] += " "

        kas_sona_on = True

        print(
            f"-------------------------\nSõna on valitud! See koosneb {condition[0]} tähest.\n-------------------------")
        tyaht = input("Kirjuta täht, mis on võimalik sõna! ")
        if len(tyaht) > 1 or tyaht.isnumeric():
            print("Sa pead kirjutama ühe tähe!")
            continue
        katsed += 1
    print("=---------SÕNE---------=\n", rand_sona[1], "\n=----------------------=")

    if condition[0] != condition[1]:
        if permission == False:
            tyaht = input("Kirjuta täht, mis on võimalik sõna! ")
            katsed += 1
        permission = False

        indeks = -1
        if rand_sona[0].upper().count(tyaht.upper()) != 0:
            for i in rand_sona[0]:
                if i == " ":
                    pass
                    indeks += 1
                elif tyaht.upper() == i.upper():
                    indeks += 1
                    lst.append(indeks)
                else:
                    indeks += 1
            if len(lst) != 0:
                for i in lst:
                    rand_sona[1] = list(rand_sona[1])
                    rand_sona[1][i] = rand_sona[0][i]
                    rand_sona[1] = ''.join(rand_sona[1])
                    condition[1] += 1
            lst = []
        else:
            print(f"{tyaht}-tähti pole, proovi uuesti.")
    else:
        print(f'valmis, katsed on {katsed}')
        kas_sona_on = False
        permission = True
