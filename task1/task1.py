user = input(': ')
user1 = user[::-1]
print(user1)
if user == user1:
    print('палиндром')
else:
    print('не палиндром')