# Klase Cat i konstruktorius

class Cat:
    def __init__(self):
            self.mood = 50

    def step_on_tail(self):
        self._alter_mood(-10)

    def pet(self):
        self._alter_mood()

    def interact(self):
        if self.mood == "bad":
            print("Hissss")
        else:
            print("Miau")

    def _alter_mood(self, change: int):
        self._mood += change

    def __str__(self):
        return (f'Cat with a {self.mood} mood')

cat1 = Cat()
print(cat1)