# 1. Sukurti žodyną kuris skirtas filtruoti darbuotojus ir parodyti jų algas
#    Raktui panaudoti vardą, pavardę
# Išspausdinti tik darbuotojus kurių pavardė yra daugiau nei penki simboliai (len) ir jie uždirba daugiau nei 9000
# Nenaudoti string karpymo funkcionalumo (pvz “John Parker”[5:11] arba .split())
# Išspausdinti tokiu formatu: Employees name is: John Parker, employee earns: 9999
# Patalpinti gautas pavardęs į vieną iš duomenų struktūrų ir išspausdinti su for ciklu:
# Išspausdinti tokiu formatu: If you have this surname, you have good salary: Parker
# Pavardės neturi kartotis
#
# Papildomai (nebūtina):
# Leisti įvesti darbuotojų info (vardas, pavardė, alga) vartotojui (darbuotojų kiekį pasirenka pats programos naudotojas)
# Kitos pradedančiųjų kurse išmoktos temos (pvz duomenų bazės)

# 1
darb_skaicius = int(input('Iveskite darbuotoju skaiciu : '))
darb_zodynas = {}
gera_alga = set([])

for i in range(darb_skaicius):
    darb_vardas = input('Iveskite darbuotojo varda : ')
    darb_pavarde = input('Iveskite darbuotojo pavarde : ')
    darb_alga = float(input('Iveskite darbuotojo atlyginima :'))
    darb_zodynas[(darb_vardas, darb_pavarde)] = darb_alga

for j, k in darb_zodynas.items():
    if len(j[1]) > 5 and k > 9000:
        print(f'Darbuotojas {j[1]} uzdirba {k}')
        gera_alga.add(j[1])

for m in gera_alga:
    print(f'Jei tavo pavarde {m}, tu gauni labai gera atlyginima')

# DONE
