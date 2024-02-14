
# Loetelu

vanus_list = []
vanus_summa = 0
vanus_list1 = []
nimi_list = []
#2v
#while True:
#    if len(nimi_list) < 5:
#        nimi = input("Sisatege nimi : ")
#        if len(nimi_list) != 0:
#            if nimi_list.count(nimi) != 0:
#                print("See nimi on juba olemas.")
#                pass
#            else:
#                nimi_list.append(nimi)
#                pass
#        else:
#            nimi_list.append(nimi)
#            pass
#    else:
#        break
#1v
for i in range(5):
    nimi = input("Sisatege nimi : ")
    nimi_list.append(nimi)
    
print(f"{sorted(nimi_list)}")
print(f"Viimane nimi on {nimi_list[4]}")
while True:
    print("Vaata lehte(0)\nNime muuta(1)\nVanusenimede lisamine(2)\nKorduva nime kustutamine(3)\nLoo vanusenimekiri(4)")
    v = int(input("Mida te tahate? "))
    if v == 1:
        v = input("Millist nime soovite muuta? ")
        nimi_len = -1
        for i in nimi_list:
            nimi_len += 1
            if v == str(i):
                print(f"Mis nimele sa {v} muuta tahad? ", end="")
                uus_nimi = input("")
                nimi_list.remove(v)
                nimi_list.insert(nimi_len, uus_nimi)
                print(nimi_list)
    elif v == 0:
        nimi_len = len(nimi_list)
        for i in range(nimi_len):
            if vanus_list[i] in vanus_list:
                print(f"{nimi_list[i]} - {vanus_list[i]}")
            else:
                print(nimi_list[i])
    elif v == 2:
        for i in range(5):
            print(f"kui vana '{nimi_list[i]}' on? ", end="")
            vanus = int(input(""))
            vanus_list.append(vanus)
        print(nimi_list)
        print(vanus_list)
    elif v == 3:
        nimi_set = set(nimi_list)
        nimi_list = list(nimi_set)
        print(nimi_list)
    elif v == 4:
        v = int(input("Kui palju vanuseid? "))
        for i in range(v):
            vanus1 = input("Mitu ")
            vanus_list1.append(vanus1)
        vanus_list1_sorted = sorted(vanus_list1,reverse=True)
        for i in vanus_list1:
            vanus_summa += int(i)
        print(f"{vanus_list1_sorted[0]} on suurim vanus, {vanus_list1_sorted[-1]} on väikseim vanus. {vanus_summa} on summa , " )
