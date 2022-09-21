
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod = input('Zadejte kod baliku: ')

if kod in baliky:
    if True == baliky[kod]:
        print(f'Balík {kod} byl předán kurýrovi')
    else:
        print(f'Balík {kod} zatím nebyl předán kurýrovi')
else:
    print('Balík neni v seznamu.')