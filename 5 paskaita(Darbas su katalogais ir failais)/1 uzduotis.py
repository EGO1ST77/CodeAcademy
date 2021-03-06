# Sukurti programą, kuri:
# Nukopijuoja šalia direktorijoje esantį paveikslėlį, tik pakeičia pavadinimą (išsaugoti tam pačiame kataloge)
# Kiekvieną kartą paleidus išsaugo tekstinį failą su šiandienos data
# Tame faile nurodytas paveikslėlio pavadinimas
# Tekstinis failas turėtų būt patalpintas šalia darbinio failo esančiame kataloge (Datos)
# Jei katalogas jau sukurtas, pasirūpinti, kad programa nebemėgintų kurti katalogo
# (ar katalogas jau sukurtas galima pažiūrėti su os.path.isdir())

import datetime
import os

copied_image_name = 'bmw.jpg'
new_image_name = 'new_copy.jpg'
date_today = datetime.date.today()+datetime.timedelta(days=1)

if not os.path.isdir('Datos'):
    os.mkdir('Datos')

with open(copied_image_name, 'rb') as failas_read:
    with open(new_image_name, 'wb') as failas_write:
        failas_write.writelines(failas_read.readlines())

with open(os.path.join('Datos', f'{date_today}.txt'), 'w') as failas:
    failas.write(new_image_name)

