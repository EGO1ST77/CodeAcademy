#   Parašyti programą, kuri:
#   Leistų vartotojui įvesti skaičių.
#   Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
#   Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
#   Patarimas: Naudoti ciklą while, sąlygą if, break

summ = 0
while int(input('Iveskite skaiciu :')) >= 0:
    summ += int(input())
    if n < 0:
        break
print('Summa = ', summ)
