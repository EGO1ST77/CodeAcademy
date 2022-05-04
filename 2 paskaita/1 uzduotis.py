
#   Sukurti programą, kuri:
#   Leistų vartotojui įvesti 5 žodžius
#   Pridėtų įvestus žodžius į sąrašą
#   Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
#   Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
#   Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index


sarasas = []
for i in range(5):
    sarasas.append(input('Iveskite 5 žodžius : '))

for j in sarasas:
    print(f'Zodis : {j}, jo ilgis : {len(j)}, numeris sarase : {sarasas.index(j)+1}')


#   DONE  :)
