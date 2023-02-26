# 1. Имеется текстовый файл.
# Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак.

# file = open("tests.file.txt", 'a',encoding='UTF-8')
# file.write("привет!" + "\n")
# file.write(str("12!") + "\n")
# file.write(str("13!") + "\n")
# file.close()

# 2. Создать файл input.txt и записать в него 10 чисел через пробел.
# Считать из него эти числа.
# Затем записать их произведение в файл output.txt.

# file = open("input.txt", 'w',encoding='UTF-8')
# file.write(str("1 2 3 4 5 6 7 8 9 10"))
# file.close()
# file = open("input.txt", 'r',encoding='UTF-8')
# file.close()
# file_numb = open("output.txt", 'w',encoding='UTF-8')
# import functools
# n = input()
# n = [int(digit) for digit in n]
# mult = functools.reduce(lambda x, y: x * y, n)
# print("Произведение:", mult)
# file_numb.close()
# file_numb = open("output.txt", 'w',encoding='UTF-8')
# file_numb.write(str("1 4 6 8 10 12 14 16 18 20"))


# 3. Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
# цену единицы и дату поступления товара на склад.
# Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р



# 4. Написать программу “Викторина”. У вас есть 2 файла.
# В первом содержаться 10 вопросов(каждый вопрос в своей строке)
# во втором 10 ответов( каждый ответ как и вопрос в своей строке).
# Вам нужно считывать по 1 вопросу из файла с вопросами и давать на них ответ.
# Если ответ верный, добавлять к счётчику верных ответов 1 балл.
# В конце программа выводит количество верных ответов на вопросы.



# 5. Создать словарь в качестве ключа которого будет 5-ти значное число,
# а в качестве значений кортеж состоящий из 2-ух элементов – имя(str) и возраста(int).
# Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата.

# import json
#
# dictionary = {
#     "key" : "12345",
#     "firstName": "Denis",
#     "age1": 29,
#     "twoName": "Alexey",
#     "age2": 25,
#     "threeName": "Vanya",
#     "age3": 24,
#     "fourName": "Pavel",
#     "age4": 24,
#     "fiveName": "Andrey",
#     "age5": 26,
#     "sixName": "Jenya",
#     "age6": 25
# }
# with open("dictionary.json", 'w',encoding='UTF-8') as file_json:
#     json.dump(dictionary,file_json,indent=4)
#
# # 6. Прочитать сохранённый json – файл и записать данные на диск в csv файл.
# # Первое значение каждой строки должно начинаться со слова person, значения разделить;
#
# import csv
#
# with open("dictionary.csv", 'r',encoding='UTF-8') as file_csv_read:
#     person = csv.reader(file_csv_read)
#     for el in person:
#      print(el)
