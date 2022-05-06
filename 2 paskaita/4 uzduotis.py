# Sukurti po vieną norimą sąrašą ir žodyną ir juose:
# Atspausdinti vieną norimą įrašą (abiejuose)
# Pridėti įrašą (abiejuose)
# Ištrinti įrašą (abiejuose)
# Ištrintą įrašą iš žodyno pridėti prie sąrašo (po antro elemento)
# Sukurti naują sąrašą ir jam prilyginti jau prieš tai sukurtą (new_list = old_list)
# Pakeiskite naujame saraše elementą ir išspausdinkite senąjį. Ar matote problemą?
# Užkomentuokite senąjį kodą ir sutvarkykite prieš tai atrastą problemą
# Jei senąjame sąraše tarp elementų būtų sąrašas/žodynas,
# ar jūsų kode problema vėl atsiranda? Jei atrandate problemą, sutvarkykite

auto = ['BMW', 'Mercedes', 'Audi', 'Volvo', 'Saab']
moto = {'sport': 'Yamaha', 'choper': 'Breackout', 'enduro': 'Honda'}

print(auto[1])
print(moto['choper'])

auto.append('Volkswagen')
moto.update(snow='Bombardir')

print(auto)
print(moto)