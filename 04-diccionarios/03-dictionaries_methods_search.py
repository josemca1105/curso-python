user = {
    'name': 'Jose',
    'age': 24,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .get()
# print(user['name'])
# print(user.get('name'))

# in
print('Jose' in user)

# .keys()
print(user.keys())
print('Jose' in user.keys())

# .values()
print(user.values())
print('Jose' in user.values())

# .intems()
print(user.items())