#  1) Вывести на экран число "10" 20 раз столбиком.

# for i in range(20):
#     print(10)

# 2) 2.	Даны два числа a и b. Составить программу вывода на экран всех чисел от a до b.

# int(input('введите число:'))
# for i in range(0,10,2):
#      print(i)

# 3) 3.	Дано число N. Составить программу выводящую кубы чисел от 1 до N в одну строку.

# int(input('введите число:'))
# for number in range(1,10):
#     if number % 1 == 0:
#       print(number**3, end=" ")

# 4) Выведите на экран в одну строку числа от 100 до
# -100 включительно.

# int(input('введите число:'))
# for numb in range(100,-101,-1):
#     print(numb, end=" ")

# 5) 5.	Необходимо вывести все четные числа на отрезке [a; a * 10]

# a = int(input('от:'))
# b = int(input('до:'))
# for numb in range(2,10,2):
#     print(numb)

# 6. Найти сумму всех целых чисел от 100 до 500 включительно.

# int(input('введите число:'))
# summa = 0
# for numb in range(100,501):
#     summa += numb
# print(summa)

# 7. Найти произведение всех целых чисел от 5 до 20 включительно. (сделано не верно)

# a = int(input("Введите число a: "))
# n = 5
# if 5 <= a and a <= 20 :
#     for i in range(a, 21):
#         n *= i
#     print(n)
# else :
#     print("Введите число от 5 до 20")

# 8.Дано натуральное число n. Вывести на экран факториал этого числа.
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# n = int(input('введите число:'))
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
# print(factorial)