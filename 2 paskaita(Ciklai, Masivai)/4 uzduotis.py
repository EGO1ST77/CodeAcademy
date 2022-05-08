# 1. Sukurti po vieną norimą sąrašą ir žodyną ir juose:
# 2. Atspausdinti vieną norimą įrašą (abiejuose)
# 3. Pridėti įrašą (abiejuose)
# 4. Ištrinti įrašą (abiejuose)
# 5. Ištrintą įrašą iš žodyno pridėti prie sąrašo (po antro elemento)
# 6. Sukurti naują sąrašą ir jam prilyginti jau prieš tai sukurtą (new_list = old_list)
# 7. Pakeiskite naujame saraše elementą ir išspausdinkite senąjį. Ar matote problemą?
# Užkomentuokite senąjį kodą ir sutvarkykite prieš tai atrastą problemą
# Jei senąjame sąraše tarp elementų būtų sąrašas/žodynas,
# ar jūsų kode problema vėl atsiranda? Jei atrandate problemą, sutvarkykite

# 1
auto = ['BMW', 'Mercedes', 'Audi', 'Volvo', 'Saab']
moto = {'sport': 'Yamaha', 'choper': 'Breackout', 'enduro': 'Honda'}

#2
print(auto[1])
print(moto['choper'])
print()

#3
auto.append('Volkswagen')
moto.update(snow='Bombardir')
print(auto)
print(moto)
print()

#4
auto.remove('Audi')
del moto['choper']
print(auto)
print(moto)
print()

#5
is_zodyno = moto.pop('sport')
auto.insert(2, is_zodyno)
print(is_zodyno)
print(auto)
print(moto)
print()

#6

#new_auto = auto
#print(new_auto)
new_auto = auto.copy()
new_auto.remove('BMW')
print(new_auto)
print(auto)


# DONE