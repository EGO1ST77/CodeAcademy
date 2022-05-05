# Sukurkite ir išsibandykite funkcijas, kurios:
# Gražinti trijų paduotų skaičių sumą.
# Gražintų paduoto sąrašo iš skaičių, sumą.
# Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
# Gražintų paduotą stringą atbulai.
# Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
# Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
# Gražintų, ar paduotas skaičius yra pirminis.
# Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# Gražina, ar paduoti metai yra keliamieji, ar ne.
# Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

def suma_triju(skaicius1, skaicius2, skaicius3):
    summ = skaicius1 + skaicius2 + skaicius3
    print(f'Suma triju {summ}')

suma_triju(1, 2, 3)

def list_sum(list):
    return sum(list)

my_list = [1, 2, 3]

a = [1, 2, 3]

def string_back(zodis):
    zodis[::-1]
    print()