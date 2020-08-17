a = []
user = input('Введите число : ')
b = 'end'
while True:
    if user == b:
        break
    uint = int(user)
    a.append(uint)
    markia = sum(a)
    user = input('Введите число: ')
    average = markia / len(a)
print('you entered: ', a)
print('Total: ', markia)
print('Average: ', average)