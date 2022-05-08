#   Parašyti programą, kuri:
#   Leistų vartotojui įvesti skaičių.
#   Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
#   Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
#   Patarimas: Naudoti ciklą while, sąlygą if, break

summ = 0
while True:
    s = int(input('Iveskite skaiciu :'))
    if s >= 0:
        summ += s
    else:
        break
print('Summa = ', summ)

# DONE