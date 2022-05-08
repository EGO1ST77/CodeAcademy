# 1. Sukurti žodyną kuris skirtas filtruoti darbuotojus ir parodyti jų algas 
#    Raktui panaudoti vardą, pavardę
# Išspausdinti tik darbuotojus kurių pavardė yra daugiau nei penki simboliai (len) ir jie uždirba daugiau nei 9000
# Nenaudoti string karpymo funkcionalumo (pvz “John Parker”[5:11] arba .split()) 
# Išspausdinti tokiu formatu: Employees name is: John Parker, employee earns: 9999
# Patalpinti gautas pavardęs į vieną iš duomenų struktūrų ir išspausdinti su for ciklu:
# Išspausdinti tokiu formatu: If you have this surname, you have good salary: Parker
# Pavardės neturi kartotis
#
# Papildomai (nebūtina):
# Leisti įvesti darbuotojų info (vardas, pavardė, alga) vartotojui (darbuotojų kiekį pasirenka pats programos naudotojas)
# Kitos pradedančiųjų kurse išmoktos temos (pvz duomenų bazės)

# 1
alga = dict({
    'Jonas Jonaitis': 9500,
    'Antanas Antanaitis': 8500,
    'Giedrius Giedraitis': 10000,
    'Marius Marcius': 8900,
    'Jon Jon': 10500
})
for i in alga:
    if len(i[' ':]) > 5:
        print(i)

