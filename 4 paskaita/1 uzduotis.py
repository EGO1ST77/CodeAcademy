# Sukurkite ir išsibandykite funkcijas, kurios:
# Gražintų paduoto sąrašo iš skaičių, sumą.
# Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
# Gražintų paduotą stringą atbulai.
# Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
# Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
# Gražintų, ar paduotas skaičius yra pirminis.
# Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# Gražina, ar paduoti metai yra keliamieji, ar ne.
# Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.


# Gražinti trijų paduotų skaičių sumą.
def suma_triju(skaicius1, skaicius2, skaicius3):
    summ = skaicius1 + skaicius2 + skaicius3
    print(f'Suma triju {summ}')

suma_triju(1, 2, 3)


# Gražintų paduoto sąrašo iš skaičių, sumą.
def list_sum(*args, skaicius):
    return sum(list)

list = [1, 2, 3, 4]
print(list_sum(1, 2, 3, 4, skaicius=6))

#a = [1, 2, 3]

# Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def big_string(*args, skaicius):
    if skaicius > skaicius:
    print(skaicius)