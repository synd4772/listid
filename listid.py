#----------------------------------------------------------------------
##2 Loetelu

#vanus_list = []
#vanus_summa = 0
#vanus_list1 = []
#nimi_list = []
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
#for i in range(5):
#    nimi = input("Sisatege nimi : ")
#    nimi_list.append(nimi)
    
#print(f"{sorted(nimi_list)}")
#print(f"Viimane nimi on {nimi_list[4]}")
#while True:
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

#3 Tärnid
#from random import *

#arvud = []
#N = int(input("Mitu rida joonistame? "))
#S = input("Sisestage sümbolit: ")
#for p in range(N):
#    arvud.append(randint(1, 100))
#for p in range(N):
#    print(arvud[p] * S)


#----------------------------------------------------------------------
##4 Postindeks

#linnad = ["Tallinn",
#["Narva","Narva-Jõesuu"],
#"Kohtla-Järve",
#["Ida-Virumaa","Lääne-Virumaa","Jõgevamaa"],
#"Tartu linn",
#["Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa"],
#["Viljanimaa","Järvamaa","Harjumaa","Raplamaa"],
#"Pärnymaa",
#["Läänemaa","Hiiumaa","Sareaa"]
#]
#indeksid = [1,2,3,4,5,6,7,8,9]
#v_indeksid = [1,2,3]

#vastus = ""
#while len(vastus) != 5:
#    vastus = input("Sisesta sulle indeksit: ")
#    if vastus[0] == "0":
#        print("Teie esimene number ei ole õige!")
#        print("Kõik olulised linnade indeksid - \n-------------------------\n")
#        for i in range(8):
#            print(f"{linnad[i]} - {indeksid[i]}")
#        print("\n-------------------------\n")
#    elif len(vastus) < 5 or len(vastus) > 5:
#        print("Indeks on vale")

#for i in range(8):
#    if vastus[0] == str(indeksid[i]):
#        print(f"Sinu linn on {linnad[i]}")
#    if i < 2:
#        if vastus[0] == str(v_indeksid[i]):
#            print("Püsige kodus!")
#            break
#        else:
#            print("Kandke maske!")
#            break

#----------------------------------------------------------------------
##5 Vahetus

#lst = []
#while True:
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

#while True:
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

#----------------------------------------------------------------------
##6: Бесполезные числа

v = int(input("Kui palju numbreid te nimekirjas soovite?"))
lst = []
for i in range(v):
    v = int(input())
    lst.append(v)

suur = 0
indks = -1
v_indeks = 0

for i in lst:
    indks += 1
    if i > 0:
        suur = i
        v_indeks = indks

print(f"suur {suur}, indeks on {v_indeks}")
lst[v_indeks] = suur / len(lst)
print(lst)

#----------------------------------------------------------------------
##7 Sorteerimine

#v = int(input("Sisestage arv: "))
#lst = []
#for i in range(v):
#    lst.append(i)
 
#while True: 
#    v = int(input("Kuidas sa nimekirja näha tahad? Kas kahanevas järjekorras(0) või taassünnikorras(1)?"))
#    if v:
#        break

#----------------------------------------------------------------------
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

#----------------------------------------------------------------------
##9: Nimi kontroll
