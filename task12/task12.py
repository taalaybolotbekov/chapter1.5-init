username = input('Введите имя: ')
userlast = input('Введите фамилию: ')
userage = int(input('Введите год рождения: '))
userplace = input('Введите место рождения: ').capitalize()
userage1 = 2018 - userage
print('Hello', username, userlast, 'You are ', userage1 , 'years old. You are living in ', userplace)