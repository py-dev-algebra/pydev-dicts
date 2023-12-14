vehicle_db = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000.00], # 45.000,00
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000.00],
    3: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78_000.00],
    4: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97_000.00],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12_000.00],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35_000.00],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9_000.00],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9_300.00]
}

print('Ispis originalnog rjecnika')
for key, value in vehicle_db.items():
    print(f'{key:<5}', end='')
    print(f'{value[0]:<20}', end='')
    print(f'{value[1]:<20}', end='')
    print(f'{value[2]:<15}', end='')
    print(f'{value[3]:<6}', end='')
    print(f'{value[4]:<10.2f}', end='')
    print()
print()
print()


# vehicle_db.clear()

# print('Ispis nakon clear() metode')
# for key, value in vehicle_db.items():
#     print(f'{key:<5}', end='')
#     print(f'{value[0]:<20}', end='')
#     print(f'{value[1]:<20}', end='')
#     print(f'{value[2]:<15}', end='')
#     print(f'{value[3]:<6}', end='')
#     print(f'{value[4]:<10.2f}', end='')
#     print()
# print()



# element_4 = vehicle_db.pop(4)
# print('Vrijednost pop(4) rezultata')
# print(element_4)
# print()
# print('Ispis nakon pop(4) metode')
# for key, value in vehicle_db.items():
#     print(f'{key:<5}', end='')
#     print(f'{value[0]:<20}', end='')
#     print(f'{value[1]:<20}', end='')
#     print(f'{value[2]:<15}', end='')
#     print(f'{value[3]:<6}', end='')
#     print(f'{value[4]:<10.2f}', end='')
#     print()
# print()

# # Sto ako upisem nepostojeci kljuc?
# element_40 = vehicle_db.pop(40, 'Ne postoji trazeni element')
# print('Vrijednost pop(40) rezultata')
# print(element_40)
# print()
# print('Ispis nakon pop(40) metode')
# for key, value in vehicle_db.items():
#     print(f'{key:<5}', end='')
#     print(f'{value[0]:<20}', end='')
#     print(f'{value[1]:<20}', end='')
#     print(f'{value[2]:<15}', end='')
#     print(f'{value[3]:<6}', end='')
#     print(f'{value[4]:<10.2f}', end='')
#     print()
# print()

element_popitem = vehicle_db.popitem()
print('Vrijednost popitem() rezultata')
print(element_popitem)
print()
print('Ispis nakon popitem() metode')
for key, value in vehicle_db.items():
    print(f'{key:<5}', end='')
    print(f'{value[0]:<20}', end='')
    print(f'{value[1]:<20}', end='')
    print(f'{value[2]:<15}', end='')
    print(f'{value[3]:<6}', end='')
    print(f'{value[4]:<10.2f}', end='')
    print()
print()
