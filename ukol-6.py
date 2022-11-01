import csv
from dataclasses import field, fields, replace

# nacteni dat ze souboru
with open('znamky_za_semestr.csv', newline='') as input:
    reader = csv.DictReader(input)
    students = []
    for row in reader:
        students.append(row)
    # nebo jako list comprehension: line = [students.append(row) for row in reader]
print(students) #kontrola dat

# uprava dat ze souboru
for grade in students:  #nahrazeni cisel za pismena
    grade['Test 1'] = grade['Test 1'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
    grade['Test 2'] = grade['Test 2'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
    grade['Test 3'] = grade['Test 3'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
    grade['Test 4'] = grade['Test 4'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
    grade['Test 5'] = grade['Test 5'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
    grade['Test 6'] = grade['Test 5'].replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E')
print(students) #kontrola dat


# zapsani dat do souboru
with open('znamky_za_semestr_upraveno.csv', mode='w', newline='',encoding='utf-8') as output:
    fieldnames = ['Příjmení', 'Jméno', 'Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6'] #nazvy v header
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader() #zapis do hlavicky
    for student in students: #zapis dat do tabulky
        writer.writerow(student)
    # nebo jako list comprehension: write = [writer.writerow(student) for student in students]