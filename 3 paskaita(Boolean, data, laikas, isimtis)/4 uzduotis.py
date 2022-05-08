# Parašyti programą, kuri:
# Apsirašytumėte du skirtingus sąrašus senas ir naujas
# Naudojant for ciklą ir append užpildytumėte naują sąrašą dvigubai
# didesniomis reikšmėmis nei senąjame (pvz senas = [1,2], naujas = [2,4]
# Tą patį padarytumėte su list comprehension (žiurėti Ciklai/Masyvai skaidres) (pvz element * 2 for element in a)
# Panaudojant datetime palyginti šių dviejų technikų įvykdymo laiką. Kuris sąrašo užpildymas buvo greitesnis?
#
# Antra dalis:
# Lygiai tas pats kas viršuje, tik šįkart visiškai tuščią sąrašą užpildyti skaičiais nuo 0 iki 1000000000
# Vėl palygint for ciklo ir list comprehension veikimo laikus. Kas greičiau?

# 1
import datetime

start_time_sarasas = datetime.datetime.now()

senas_sarasas = []
naujas_sarasas = []

for a in range(1000):
    senas_sarasas.append(a)

for i in range(len(senas_sarasas)):
    naujas_sarasas.append(senas_sarasas[i])

end_time_sarasas = datetime.datetime.now()
time_sarasas = end_time_sarasas - start_time_sarasas
print(f'Pirmas laikas : {time_sarasas}')
print('--------------------------------')

start_time_list = datetime.datetime.now()

a = senas_sarasas.copy()
b = [j ** 2 for j in a]

end_time_list = datetime.datetime.now()
time_list = end_time_list - start_time_list
print(f'Antras laikas : {time_list}')
print('------------------------------')

start_time = datetime.datetime.now()

million = []
for k in range(100000000):
    million.append(k)

end_time = datetime.datetime.now()
time_million = end_time - start_time
print(f'Trecias laikas : {time_million}')
print('------------------------------')

# DONE