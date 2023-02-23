# 1. Дано число n. Вывести все числа от 1 до n.

# n = int(input('введите конечное число:'))
# start = 1
# while start <= n:
#     print(start,end=" ")
#     start += 1
# print('цикл завершён')

# 2. Дано число n. Посчитать сумму всех чётных чисел от 0 до n.

# summa = 0
#
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     summa += a
#
# print(summa)

# 3. Дано натуральное число.
# Определить произведение цифр в нем которые кратны 2, кроме числа 0.

# numb = int(input())
# mult - 1
# while numb:
#    if numb % 10 % 2 == 0 and numb % 10 != 0:
#        mult *= numb % 10
#    numb //= 10
# print(mult)

# 4. Дано число n.
# Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9

# n = 149
# s = 15
# i = 1
# while i <= n:
#
#     print(i)

# 6. 6.	Дано число n. Определить первую цифру этого числа.

# abs - модуль, который делает минус на плюс в цифрах.

# n = abs(int(input()))
# while n > 9:
#     n //= 10
# print(n)

# 5.	Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
# Sample Input :
# 5
# Sample Output :
# 9

# numb = 1
# n = int(input())
# while numb ** 2 < n:
#     numb += 1
# print(numb ** 2)

# 8. Дано натуральное число n.
# Найти значение минимальной цифры в данном числе.

# number = int(input())
# mib_num = number % 10
# while number:
#     if min_num > number % 10:
#         min_num = number % 10
#     number //= 10
# print(min_num)






