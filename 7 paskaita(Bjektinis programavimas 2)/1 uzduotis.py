class Car:
    def __init__(self, metai: int, model: str, fuel: str):
        self.metai = metai
        self.model = model
        self.fuel = fuel
        print(self.print_car())

    def print_car(self):
        return f'Metai auto {self.metai}, Modelis : {self.model}, kuras: {self.fuel}'

    def drive(self):
        print('Vaziuoja')

    def stop(self):
        print('Priparkuota')

    def refuel(self):
        print('Pripiles kuro')


class Electra(Car):
    def refuel(self):
        super().refuel()
        print('Baterija ikrauta')

    def drive(self):
        super().drive()
        print('Važiuoja autonomiškai')

    def stop(self):
        super().stop()



bmw = Car(2023, 'BMW X5', 'benzin')
leaf = Electra(2022, "Nissan", "Elektra")
bmw.refuel()
bmw.stop()
bmw.drive()
leaf.refuel()
leaf.stop()
leaf.drive()

