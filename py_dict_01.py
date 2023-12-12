# Deklaracija
employees = {
    '123': 'Pero Peric',
    '321': 'Ana Anic',
    '456': 'Marko Maric',
    '654': 'Iva Ivic'
}

shopping_list = {
    5: ['Kulen', 8.99],
    1: ['Cvarci', 3.59],
    7: ['Seka', 4.99]
}
# print(shopping_list)

# # Izvrsavanje programa
# print(employees['654'])
# print(shopping_list[5])


# shopping_list[10] = 'Krvavice'

# print(shopping_list)

# shopping_list[10] = 'Kobasice'
# print(shopping_list)



# print(shopping_list.keys())
# print(employees.keys())

# for key in shopping_list.keys():
#     print(key)
# print()

# for key in shopping_list.keys():
#     print(shopping_list[key])
# print()

# for value in shopping_list.values():
#     print(value)
# print()

# lista = []
# for index, value in enumerate(lista):
#     print(index, value)


for key, value in shopping_list.items():
    print(key, value)







# Pospremanje, oslobadanje resursa, pozdravna poruka
print('\nHvala sto ste koristili nas program, vidimo se uskoro!\n')
