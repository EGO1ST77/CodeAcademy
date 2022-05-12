# Sukurti programą, kuri:
# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
from datetime import datetime


class Worker:
    def __init__(self, name, hour_pay, start_time):
        self.name = name
        self.hour_pay = hour_pay
        self.start_time = start_time

    def _work_day(self):
        work_from = datetime.strptime(self.start_time, '%Y, %m, %d')
        data_now = datetime.now()
        all_work = data_now - work_from
        return all_work.days

    def get_salary(self):
        salary = self._work_day() * 8 * self.hour_pay
        return salary

    def __str__(self):
        return (f'Darbuotojas: {self.name} alga: {self.get_salary()}')


class GoodWorker(Worker):

    def get_salary(self):
        work_days = super()._work_day() * 7 / 10
        salary = self.hour_pay * work_days
        return salary


worker1 = Worker("Ilyas", 2.70, "2022, 03, 12")
goodWorker = GoodWorker("Uladzimir", 65, "2022, 03, 15")
print(worker1)
print(goodWorker)
