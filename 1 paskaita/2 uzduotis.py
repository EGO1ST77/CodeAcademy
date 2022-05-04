# Parašyti programą, kuri atspausdintų jūsų:
# Vardą bei pavardę
# Atspausdintų paskutinį pavardės simbolį
# Atspausdintų pirmą vardo simbolį
# Atspausdintų tik vardą
# Atspausdintų tik pavardę
# Išspausdintų vardą bei pavardę didžiosiomis raidėmis
# Atspausdintų vardą/pavardę atbulai
# Atskirtų žodžius tarp atskirų kabučių (padarytų sąrašą)
# Jūsų pavardę pakeistų į „Python Specialistas“ ir atspausdintų naują sakinį

vardas = 'Igor Masevic'

print(f'Mano vardas ir pavarde : {vardas} ')
print(f'Paskitine pavardes raide: {vardas[-1]}')
print(f'Pirmas vardo simbolis: {vardas[0]}')
print(f'Tik vardas : {vardas[:vardas.find(" ")]}')
print(f'Tik pavarde : {vardas[vardas.find(" ")+1:]}')
print(f'Didziosiomis : {vardas.upper()}')
print(f'Atblai : {vardas[::-1]}')
print(f'Atskirti ir ideti i sarasa : {vardas.split()}')
print(f'Keicaim : {vardas.replace("Masevic", "Python Specialistas")}')

#   DONE :)