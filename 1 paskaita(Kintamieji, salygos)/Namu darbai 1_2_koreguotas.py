# Parašyti programą, kuri:
# Leistų įvesti krepšininko vardą
# Leistų įvesti krepšininko ūgį (metrais) (pvz 1.86)
# Pagal duotą ūgį priskirtų krepšininkui poziciją. Pvz. daugiau nei 210.4m, tai centras.
# (Galite naudoti ūgius savo nuožiūra, jei duosite įžaidėjui 3m ūgį, nieko tokio)
# Kintamasis pozicija saugotų informaciją apie krepšininko poziciją
# Gražiai išspausdintų tokį sakinį (pavyzdys): Vardas yra krepšininkas, kurio ūgis yra 184cm. Jo pozicija yra centras.
# Parašyti vardą viršutiniame sakinyje didžiosiomis raidėmis, net jei įvesta mažosiomis

vardas = input('Iveskite varda: ')
ugis = float(input('Iveskite ugi : '))
svoris = float(input('Iveskite svori : '))

if 1.2 <= ugis <= 1.6 and 60 <= svoris <= 85:
    print(f'{vardas.title()} yra krepsininkas, kurio ugis {int(ugis * 100)} sm. Jo pozicija yra Lengvas krastas')
elif ugis <= 1.9 and svoris <= 95:
    print(f'{vardas.title()} yra krepsininkas, kurio ugis {int(ugis * 100)} sm. Jo pozicija yra Sunkus krastas')
elif ugis <= 2.1 and svoris <= 105:
    print(f'{vardas.title()} yra krepsininkas, kurio ugis {int(ugis * 100)} sm. Jo pozicija yra Atakojantis ginejas')
elif ugis <= 2.3 and svoris <= 120:
    print(f'{vardas.title()} yra krepsininkas, kurio ugis {int(ugis * 100)} sm. Jo pozicija yra Centras')
else:
    print(f'{vardas} Nestandartinis zaidejas')