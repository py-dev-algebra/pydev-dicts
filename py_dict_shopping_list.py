# Deklaracija
shopping_list = []


# Izvrsavanje programa
shopping_list_size = int(input('Unesite broj namiranica: '))

for i in range(shopping_list_size):
    grocery = input('Unesite ime namirnice: ')
    price = float(input('Unesite cijenu namirnice: '))

    shopping_list_item = {}
    shopping_list_item['grocery'] = grocery
    shopping_list_item['price'] = price

    shopping_list.append(shopping_list_item)



for item in shopping_list:
    for key, value in item.items():
        print(key, value)
