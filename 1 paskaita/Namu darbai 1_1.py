# Parašyti programą, kuri:
# Leistų įvesti skaičių
# Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
# Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
# Išvesti į ekraną „Skaičius dalijasi iš 3“, jei skaičius dalijasi iš trijų
# Patarimas: naudoti input(), if, print, %, <, >

a = int(input('Iveskite skaiciu : '))
if a % 2 == 0:
    print('Skaicius yra lyginis')
if a % 2 != 0:
    print('Skaicius yra NElyginis')
if a % 3 == 0:
    print('Skaicius dalijasi is 3')