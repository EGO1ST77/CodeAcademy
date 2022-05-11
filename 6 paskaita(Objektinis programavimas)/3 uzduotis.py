# Perdaryti:
# 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas, veiksmai turi būti atliekami su „default“ tekstu
# 2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data, veiksmai turi būti atliekami su programuotojo gimtadieniu

class Sakinys:
    def __init__(self, string='Labas'):
        self._text = string

    def atbulai(self):
       return self._text[::-1]

    def mazom(self):
        return self._text.lower()

    def didelem(self):
        return self._text.upper()

    def pagal_num(self, num):
        return self._text.split()[num - 1]

    def simbol(self, chr):
        return self._text.count(chr)


a = Sakinys()

print(a.atbulai())
print(a.simbol('a'))
print(a.mazom())
print(a.didelem())
