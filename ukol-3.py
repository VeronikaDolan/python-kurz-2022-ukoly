import sys
def valid_number(number): #...kontrola, zda je telefonni cislo spravne dlouhe
    if len(number) > 13: #...pokud je vetsi nez 13 cisel, vrati False
        return False
    elif len(number) < 13: #...pokud je kratsi nez 13 cisel, vrati False
        return False
    elif len(number) == 13: #...pokud je 13ti mistne , vrati True
        return True

number = input('Zadejte telefonní číslo: ')
number = number.replace(' ','') #...maze mezery v tel.cisle
format = valid_number(number)

#...kontrola formatu cisla (pred funkci zkontroluje delku telefonniho cisla a pokud je nespravna ukonci program)
if format == False: #...pokud je vysledek funkce valid_number False
    print('Spatne zadany format telefonniho cisla!')
    sys.exit()

#...kontrola predvolby (pred funkci zkontroluje predvolbu a pokud je nespravna ukonci program)
if number[0:4] !='+420': #...pokud prvni 4 pozice nejsou v zadanem formatu
    print('Zadal jsi nespravnou predvolbu!')
    sys.exit()

def message_length(message):
    if len(message)%180 > 0:             #...pokud je zbytek po deleni 180 vetsi nez 0
        return ((len(message)//180)*3)+3 #...pricte navic 3kc za zapocatou zpravu
    elif len(message)//180:              #...pokud je delka zpravy delitelna 180 
        return (len(message)//180)*3     #...za 180 znaku se plati 3kc
    else: #...pokud nesplnuje ani jednu podminku (kratsi zprava nez 180 znaku, cena je 3kc)
        return 3

message = input('Zadejte text zpravy: ')
cost_message = message_length(message)

print(f'Celkova cena za tuto zpravu je {cost_message} Kc.')

