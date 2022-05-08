# Parašyti programą, kuri:
# 1. Atspausdintų dabartinę datą ir laiką
# 2. Atimtų iš dabartinės datos ir laiko 5 dienas ir atspausdintų
# 3. Pridėti prie dabartinės datos ir laiko 8 valandas ir atspausdintų
# 4. Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta
#
# Papildomai: papildomi aritmetiniai veiksmai su data
import datetime

# 1
data_now = datetime.datetime.now()

# 2
data_minus_5days = data_now - datetime.timedelta(days=5)
print(data_minus_5days)

# 3
data_plus_8hour = data_now + datetime.timedelta(hours=8)
print(data_plus_8hour)

# 4
print(data_now.strftime('%Y %m %d, %X'))


# DONE