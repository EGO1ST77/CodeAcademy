# Parašyti programą, kuri:
# Išvestų jūsų kurso dienų sąrašą tokiu formatu:
# 2022 - April - 28 - Thursday
# 2022 - May - 02 - Monday
# 2022 - May - 03 - Tuesday
# 2022 - May - 05 - Thursday
# 2022 - May - 09 - Monday
# Ir t.t.
# Dienas patalpinti į sąrašą
# Papildomai galite datas sukelti į text, csv ar kitą failiuką
# Papildomai galite padaryti įvedimą kurso startui
#
# Jūsų kursas viso 480 valandos. Po 4 valandas paskaitai.
# Jei žinote datų kuriose paskaitos nevyks, jas reiktu praleist. Kaip pvz Gegužės 4

def biggest_number(*args):
    print(max(args))
    return max(args)

def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)