# Sukurti programą, kuri:
# Vienu lygiu žemiau darbinio katalogo sukurtų katalogą „Naujas Katalogas“
# (pvz. jei dirbate direktorijoje Desktop -> CodeAcademy, tai sukurti aplanką Desktop vietoje)
# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data,
# laikas ir direktorija iki failo. Po laiko padaryti naują eilutę
# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
#
# Papildomai:
# Sukurti katalogą/failą su savo norimu pavadinimu
# Panaudoti try/catch kuriant tą patį katalogą

import os
from datetime import datetime

katalogas_pavadinimas = 'Naujas katalogas'
failo_pavadinimas = 'failas.txt'

os.chdir('..')
try:
    os.mkdir(katalogas_pavadinimas)
except:
    print('Failas egzistoja')

os.mkdir(katalogas_pavadinimas)

os.chdir(katalogas_pavadinimas)

with open(failo_pavadinimas, 'w') as failas:
    failas.write(str(datetime.today()) + '\n')
    failas.write(str(os.getcwd()))

print("sukurimo data:", os.start('data.txt'))