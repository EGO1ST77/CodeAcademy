laipsnis_out = None

# Grazina int
def pakelti_laipsniu(skaicius, laipsnis):
    global laipsnis_out
    laipsnis_out = laipsnis
    kubu = skaicius ** laipsnis
    return kubu

print(f'{pakelti_laipsniu(2, 3)}')
print(f'Pakelta {laipsnis_out}')
