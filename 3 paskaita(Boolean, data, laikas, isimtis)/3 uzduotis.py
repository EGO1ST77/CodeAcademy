# Parašyti programą, kuri:
# Paprašytų įvesti laiką tokiu formatu (2021-02-11)
# Iš įvesto laiko atimtų 14 savaičių
# Išspausdintų rezultata tokiu formatu (2020 - November - 05 - Thursday)
# Jeigu data įvedama neteisingai išspausdinti:
# Klaidą
# Dabartinę datą tokiu formatu (2022 - May - 03 - Tuesday)
# Patarimas: naudoti input, strptime, strftime

import datetime

try:
    ivesta = input('Iveskite metus formatu (YYYY-MM-DD): ')
    ivesta_data = datetime.datetime.strptime(ivesta, '%Y-%m-%d')
    print(f'Ivesta data : {ivesta_data}')

    data_minus_14sav = ivesta_data - datetime.timedelta(weeks=14)
    print(data_minus_14sav.strftime(f'Minus 14 dienu : %Y - %B - %d - %A'))
except ValueError:
    print('Klaida')

# DONE
