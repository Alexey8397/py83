# 1) Напишите программу, которая проверяет последнюю цифру числа.

# a = int(input('Введите число'))
# if a % 10 == 3:
#     print(True)
# else:
#     print(False)

# 2) Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно.
# Если нет вывести False. Числа вводятся с клавиатуры в одной строке.

# a, b, c = map(int, input().strip().split(" "))
# print(a < 0 or b < 0 or c < 0)

# 3)

# numb1, numb2 = map(int, input('введите 2 числа') .split())
# print(numb1 % 2 == numb2 % 2)

# length = 56
# speed = int(input('введите скорость км/ч:'))
# hours = int(input('введите часы'))
# minutes = int(input('ведите минуты'))
# time_trevel = hours + minutes / 60
# trevel_dist = time_trevel * speed
# print(time_trevel)
# print(trevel_dist)
# print(trevel_dist % length)

# for i in range(5):
#     print("Hello, world")

# задачи со строками из второй домашки

# s = input()
# print(s == s[::-1])

# s = input()
# count_f = s.count('f')
# if count_f == 1:
#     print(-1)
# elif count_f == 0:
#     print(-2)
# else:
#     first_ind = s.find('f')
#     print(s.find('f', first_ind + 1))

# s = input().lower()
# count_g = s.count('g')
# count_c = s.count('c')
# length = len(s)
# print(count_c + count_g)/length * 100



