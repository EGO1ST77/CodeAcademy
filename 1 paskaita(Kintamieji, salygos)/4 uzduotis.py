# Parašyti programą, kuri:
#
# Leistų įvesti pirmą skaičių
# Leistų įvesti antrą skaičių
# Paklaustų, kokį matematinį veiksmą reiktų atlikti (sudėtis, atimtis, daugyba, dalyba) (galima ir daugiau)
# Atspausdintų rezultatą: pasirinktų skaičių sumą, daugybą ar pan.
# Patarimas: naudoti input(), if, print

a = int(input('Ivesti pirma skaisiu : '))
b = int(input('Ivesti antra skaiciu : '))
x = input('Iveskite MATH veiksni (+, -, *, /) : ')

if x == '+':
    print('Suma : ', a + b)
elif x == '-':
    print('Minus : ', a - b)
elif x == '*':
    print('Dauginam : ', a * b)
else:
    print('Dalinam : ', a / b)

