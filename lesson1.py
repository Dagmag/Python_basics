"""
1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
# name = input('Укажите свое имя >>> ')
# age = int(input('Укажите свой возраст >>> '))
# country = input('Укажите свою страну >>> ')
# city = input('Укажите свой город >>> ')
# print(f'Имя: {name}, Возраст: {age}, Страна: {country}, Город: {city}')


# a, b, c = int(input('Введите число a >>> ')), int(
#     input('Введите число b >>> ')), int(input('Введите число c >>> '))
# num1 = (a + b - c)
# num2 = a // b % c
# print(num1, num2)


"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""


# time = int(input("Введите время в секундах >>> "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"{hours} : {minutes} : {seconds}")


"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""

# n = input('Введите число >>> ')
# nn = int(n+n)
# nnn = int(n+n+n)
# n = int(n)
# result = n+nn+nnn
# print(result)

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

"""

# n = abs(int(input("Целое положительное число >>> ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Самая большая цифра ", max)
#         break


"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


# revenue, costs = float(input('Выручка >>> ')), float(input('Издержки >>> '))

# if revenue > costs:
#     profit = revenue - costs
#     profitability = (profit / revenue) * 100
#     print('Прибыль', profit, '$', 'Рентабелонсть', round(profitability, 2), '%')
#     workers = int(input("Количество сотрудников >>> "))
#     print('Прибыль на сторудника', round((profit / workers), 2), end=' $')

# elif revenue == costs:
#     print('Компания работает в 0')
# else:
#     print('Компания работает в убыток')


"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""


# a = int(input('Результат первого дня: '))
# b = int(input('Желаемый результат: '))
# day = 1
# first_day = a
# while first_day < b:
#     a = a + 0.1 * a
#     day += 1
#     first_day = a
# print('Вы достигнете требуемых показателей на', day, 'день')


"""
Важно!
При отправке домашнего задания обязательно нажимайте галочку "Показать задание ментору".

"""
