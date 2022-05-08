# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių .
# Atspausdinti True, jei skaičius teigiamas ar neigiamas
# Atspausdinti False, jei skaičius lygus 0 ir pabaigti programą
# True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį skaicius_ne_nulis
# Patarimas: naudoti input, boolean
#
# Papildomai: Padaryti, kad programa sustotų įvedus netinkama simbolį (0.1, “f” ir t.t)

skaicius_ne_nulis = []

while True:
    try:
        s = int(input('Iveskite skaiciu : '))
        if s > 0 or s < 0:
            print(bool(s))
            skaicius_ne_nulis.append(s)
        else:
            print(bool(0))
            break
    except:
        print(f'Ivestas ne skaicius, bandykite dar karta')
print('Ivesti skaiciai : ', *skaicius_ne_nulis)

# DONE