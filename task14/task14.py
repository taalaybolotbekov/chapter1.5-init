students = input('Введите имя студента: ')
ocenka = int(input('Введите оценку: '))
students1 = input('Введите имя студента: ')
ocenka1 = int(input('Введите оценку: '))
students2 = input('Введите имя студента: ')
ocenka2 = int(input('Введите оценку: '))
students3 = input('Введите имя студента: ')
ocenka3 = int(input('Введите оценку: '))
# user = {students : ocenka, students1 : ocenka1, students2 : ocenka2, students3 : ocenka3}
# mark = max(ocenka, ocenka1, ocenka2, ocenka3)
# print('Ваша оценка: ', mark)
mark = sum([ocenka, ocenka1])
mark2 = sum([ocenka2, ocenka3])
mark3 = sum([mark, mark2])
mark4 = mark3 / 4 + 0.5
print(int(mark4))




