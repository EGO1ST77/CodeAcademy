# Padaryti vieną kintamąjį iš dviejų sakinių ir:
# Iškarpyti kiekvieną sakinį su string karpymo įrankiais bei sumažinti visas didžiąsias raides. Išspausdinti
# Sugrąžinti didžiąsias raides. Išspausdinti. (turim viena kintamaji, ir ji isprintinam su funkcija)
# Sujungti sakinius iš naujo bei išspausdinti
# Išspausdinti sakinius atbuline tvarka
#
# Papildoma užduotis:
# Padaryti taip, kad du sakiniai būtų tinkamai iškarpyti ir sujungti atgal, nepaisant jų dydžio su tuo pačiu kodu.

string = 'Улыбок тебе, дед Макар'

first = string[0: string.find(",")].lower()
second = string[len(first) + 1:].lower().strip()

print(first)
print(second)

print(first.capitalize())
print(second.capitalize())

s = first + " " + second
print(s)
print(s[::-1])