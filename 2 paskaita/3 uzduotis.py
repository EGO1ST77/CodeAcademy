# Sukurti programą, kuri:
# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
import random

a = random.randint(1, 6)
while a == 5:
    print(f' {a} - Pralaimejai...')
    break
else:
    print(f' {a} - Laimejai')
