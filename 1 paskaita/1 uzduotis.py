#   Parašyti programą, kuri:
#   Leistų įvesti skaičius a ir b(vienas int, kitas float)
#   Išvestų į ekraną „a mažesnis už b“, jei taip yra
#   Išvestų į ekraną „a lygu b“, jei taip yra
#   Išvestų į ekraną „a didesnis už b“, jei taip yra
#   Pirmu ir trečiu atveju išvestų didesnio skaičiaus iš mažesnio dalybos rezultatą
#   Antru atveju sudėtų skaičius

a, b = int(input('A skaicius: ')), float(input('B skaicius: '))
if a < b:
    print('A mazesnis uz B, dalyba: ', b/a)
elif a == b:
    print(('A lygus B, summa: ', a + b))
else:
    print('A didesnis uz B, dalyba: ', a/b)