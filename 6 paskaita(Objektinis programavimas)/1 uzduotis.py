class Sakinys:
    def __init__(self, string):
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

    def change_text(self, new):
        return self._text.replace(new)


text = Sakinys("Laba diena")
print(text.atbulai())
print(text.mazom())
print(text.didelem())
print(text.pagal_num(2))
print(text.simbol("a"))
print(text.change_text("Vakaras"))