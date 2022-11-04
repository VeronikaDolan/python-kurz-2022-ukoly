import datetime 
from datetime import datetime
input_date = input('Zadejte datum(dd.mm.yyyy): ')
input_persons = int(input('Zadejte pocet osob: '))

tickets_date = datetime.strptime(input_date,'%d.%m.%Y')

#prvni_udalost = 01.07.2021 - 10.08.2021
#druha_udalost = 11.08.2021 - 31.08.2021

prvni_udalost_open = datetime(2021, 7, 1)
prvni_udalost_close = datetime(2021, 8, 10)
druha_udalost_open = datetime(2021, 8, 11)
druha_udalost_close = datetime(2021, 8, 31)

if (tickets_date >= prvni_udalost_open) and (tickets_date <= prvni_udalost_close):
    print(f'Cena vstupenek je: {input_persons*250} Kc.')
elif (tickets_date >= druha_udalost_open) and (tickets_date <= druha_udalost_close):
    print(f'Cena vstupenek je: {input_persons*180} Kc.')
else:
    print('V tento datum je letni kino zavrene.')