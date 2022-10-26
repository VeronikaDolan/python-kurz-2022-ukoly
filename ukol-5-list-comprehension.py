#1 Seznamy čísel
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

cisla_1 = []

# puvodni cyklus
#for cislo in cisla:
#    cisla_1.append(cislo*2)
#print(cisla_1)


print([cislo*2 for cislo in cisla]) # každé z čísel ze seznamu cisla vynásobené dvěma
print([cislo*(-1) for cislo in cisla]) # každé z čísel ze seznamu cisla s opačným znaménkem
print([cislo**2 for cislo in cisla]) # každé z čísel ze seznamu cisla umocněné na druhou
print([str(cislo) for cislo in cisla]) # každé z čísel ze seznamu cisla jako řetězec

#2 Seznamy řetězců
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

jmena_1 = []

# puvodni cyklus
#for jmeno in jmena:
#    jmena_1.append(len(jmeno))
#print(jmena_1)

print([len(jmeno) for jmeno in jmena]) # počty písmen ve všech jménech
print([(jmeno.upper()) for jmeno in jmena]) # všechna jména napsaná velkými písmeny
print([jmeno+'a' for jmeno in jmena]) # všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména)
print([jmeno.lower()+'@email.cz' for jmeno in jmena]) # všechna jména převedená na malá písmena s koncovkou



#3 Seznam teplot
from statistics import mean

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# puvodni cyklus
#for teplota in teploty:
#    x = sum(teplota)
#    print(x)

print([mean(teplota) for teplota in teploty]) # seznam průměrných teplot pro každý den
print([teplota[0] for teplota in teploty]) # seznam ranních teplot.
print([teplota[-1] for teplota in teploty]) #seznam nočních teplot.
print([[teplota[1], teplota[-1]] for teplota in teploty]) # seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu

#Spocita celkovou průměrnou teplotu za celý týden

#puvodni cyklus
# result = []
#for teplota in teploty:
#   for val in teplota:
#       result.append(val)
#print(result)

result = [val for teplota in teploty for val in teplota] # prevede vsechny hodnoty na jeden list
average = mean(result) # vypocita prumernou hodnotu
print(average)

