employee_123456 = {
    'employee_id': '123456',
    'first_name': 'Pero',
    'last_name': 'Peric',
    'email': 'pero.peric@example.com',
    'address': {
        'street': 'Ilica 123',
        'postal_code': '10000',
        'city': 'Zagreb',
        'country': 'Hrvatska'
    }
}

employee_654321 = {
    'employee_id': '654321',
    'first_name': 'Iva',
    'last_name': 'Ivic',
    'email': 'pero.peric@example.com',
    'address': {
        'street': 'Ilica 123',
        'postal_code': '10000',
        'city': 'Zagreb',
        'country': 'Hrvatska'
    }
}


employees = []
employees.append(employee_123456)
employees.append(employee_654321)


# print(employees)
for employee in employees:
    # print(employee) -> employee je rjecnik ili dict
    print()
    for key, value in employee.items():
        print(key, value)
