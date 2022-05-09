# Sukurti programą, kuri:
# Leistų vartotojui įvesti norimą eilučių kiekį (pvz. įvesti 5 ar 8 eilutes)
# Pvz. vartotojas pasirenka įvesti du sakinius ir įveda “Python programavimo kalba” ir “JavaScript programavimo kalba”
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą (failas tegu būna sukuriamas tame pačiame kataloge kur dirbame)
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Išspausdintų failo turinį
# Išspausdintų po vieną sakinį (nauja eilutė -  naujas sakinys, be tarpų tarp eilučių)

import os
text = ''

line_number = int(input('Enter line number : '))

for line in range(line_number):
    text += input("Iveskite eilute : ") + '\n'

file_name = input('Iveskite failo pavadinima : ')

with open(f'{file_name}.txt', 'w') as write_file:
    write_file.write(text)

with open(f'{file_name}.txt', 'r') as read_file:
    for line in read_file:
        print(line)