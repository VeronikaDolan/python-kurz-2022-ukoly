class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti


import sys

from defer import return_value
class Koronavirus(Nemoc):

    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni, varianty=[]):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = varianty

    def __str__(self):
        list_to_str = ', '.join(map(str, self.varianty)) # prevadi list varianty na string a oddeluje je carkami
        
        if len(self.varianty) == 0:
            return f'{super().__str__()} (zadne nalezene varianty)'
        else:
            return f'{super().__str__()} (varianty: {list_to_str})' #{self.varianty}

    def zmen_pocet_obeti(self, pocet_obeti): #...zdedena metoda zmen_pocet_obeti
        return super().zmen_pocet_obeti(pocet_obeti)


    def pridej_variantu(self, varianty): #...do atributu varianty prida novou variantu
        self.varianty.append(varianty)

nemoc = Nemoc('Coronavirus', 15, 10000, 'vzduchem')
print(nemoc)

corona = Koronavirus('Coronavirus', 15, 10000, 'vzduchem')
print(corona) # Jmeno: Coronavirus (zadne nalezene varianty)

print(corona.pocet_obeti)
corona.zmen_pocet_obeti(20000) #nefunguje
print(corona.pocet_obeti)

print(corona.inkubacni_doba) #pevne dane volanim super().__init

corona.pridej_variantu('omicron')
corona.pridej_variantu('delta')

print(corona) # Jmeno: Coronavirus (varianty: omicron, delta)
corona.pridej_variantu('alpha')
print(corona) # Jmeno: Coronavirus (varianty: omicron, delta, alpha)
