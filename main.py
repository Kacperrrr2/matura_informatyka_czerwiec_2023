# INFORMATYKA 2023 CZERWIEC FORUMULA 2015

wiersze=open('przyklad.txt','r')
tab=[]

for wiersz in wiersze:
    tab.append(wiersz.strip())
# Zadanie4.1
# liczba_jedynek=0
# liczba_zer=0
# liczba_zrownowazona=0
# liczba_prawiezrownowazona=0
# for i in tab:
#     for j in i:
#         if j=='1':
#             liczba_jedynek+=1
#         if j=='0':
#             liczba_zer+=1
#     if liczba_jedynek==liczba_zer:
#         liczba_zrownowazona+=1
#     if liczba_jedynek==(liczba_zer-1) or (liczba_jedynek-1)==liczba_zer:
#         liczba_prawiezrownowazona+=1
#     liczba_zer=0
#     liczba_jedynek=0
#
# print(str(liczba_zrownowazona) + " " + str(liczba_prawiezrownowazona))
# Zadanie 4.2



