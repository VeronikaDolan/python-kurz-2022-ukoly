from dataclasses import dataclass


@dataclass
class Recept:
    nazev: str
    narocnost: str
    url_adresa: str
    vyzkouseno: bool

    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        return (f' Recept: {self.nazev}, na adrese: {self.url_adresa}, narocnost: {self.narocnost},vyzkouseny: {self.vyzkouseno}.')

    def zmen_narocnost(self, nova_hodnota): #...zmeni narocnost receptu
        self.narocnost = nova_hodnota
        return self.narocnost

    def zkusit(self, vyzkouseno): #...zmeni atribut vyzkouseno na True
        self.vyzkouseno = True
        return self.vyzkouseno

tiramisu = Recept('Tiramisu', '4', 'https://www.recept.cz/tiramisu') #...vlozeni receptu na tiramisu
print(str(tiramisu))

muffiny = Recept('Muffiny', '2', 'https://www.recept.cz/muffiny') #...vlozeni receptu na muffiny
print(str(muffiny))

babovka = Recept('Babovka', '1', 'https://www.recept.cz/babovka') #...vlozeni receptu na babovku
print(str(babovka))

tiramisu.zmen_narocnost('5') #...zmena narocnosti receptu
print(str(tiramisu))

tiramisu.zkusit(True) #...zmena receptu z nevyzkouseno na vyzkouseno
print(str(tiramisu))

class Kucharka(Recept):
    name: str
    autor: str
    recepty: list

    def __init__(self, name, autor, recepty=[]):
        self.name = name
        self.autor = autor
        self.recepty = recepty

    def __str__(self):
        return (f'Kucharka: {self.name}, od autora: {self.autor}, recepty: {self.recepty}')
    
    def pocet_receptu(self): #...vraci cislo reprezentujici pocet receptu v atributu recepty
        pocet = len(self.recepty)
        return pocet

    def pridej_recept(self, recepty): #...prida recept do kucharky
        self.recepty.append(recepty)

#Bonus
    def vyzkousene_recepty(self): 
        for recept in self.recepty: #...pro recept v listu receptu
            if recept.vyzkouseno == True: #...pokud je v receptu na pozici 'vyzkouseno' nastaveno True
                print(recept) #...vypis dany recept




kucharka = Kucharka('Varime s Pajou', 'Pavlik', [muffiny, tiramisu]) #...prida do kucharky jeji nazev, autora a recepty, ktere chceme a jsou jiz definovane
print(str(kucharka))

babovka = Recept('Babovka', '1', 'https://www.recept.cz/babovka') 
kucharka.pridej_recept(babovka) #...prida novy recept na babovku
print(str(kucharka))

babovka.zkusit(True) #...zmena receptu z nevyzkouseno na vyzkouseno
print(str(babovka))

print(kucharka.pocet_receptu()) #...spocita pocet zadanych receptu

# Bonus (vypise vsechny vyzkousene recepty)
kucharka.vyzkousene_recepty()

