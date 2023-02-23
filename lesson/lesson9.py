# новая тема: files (файлы)
# бывают текстовый и бинарный
# режимы доступа:
# w - write - запись(всё, что было то пропало..)
# r - read - чтение(считываем всё из файла)
# a - append - дозапись(записывает в конец файла)
# x - запишет в файл информации если файла не существовало
# w+ r+ a+ wb rb ab xb+ rb+
# file = open("test_file.txt",'w',encoding='UTF-8')
# file.write(str(61) + "\n")
# file.write(str(68) + "\n")
# file.write(str(60) + "\n")
# file.close() # чтобы не потерять данные
# file = open("test_file.txt",'r',encoding='UTF-8')
# students = {}
# for line in file:
#     lst = line.rstrip().split()
#     marks = list(map(int,lst[1:]))
#     print(marks)
#     students[lst[0]] = marks
# file.close()
# print(students)
# file_avg = open("avg_mark",'w',encoding='UTF-8')
# for name,marks in students.items():
#     file_avg.write(name + " " + str(sum(marks) / 5) + "\n")
# file_avg.close()
# print(repr(some_str))
# lst = some_str.replace('\n', " ").rstrip().split()
# lst = list(map(int,lst))
# print(lst)

# что такое контекстный менеджер - работает на открытие и закрытие информации
# enter - вход exit выход

# with open("test_file.txt",'r',encoding="utf-8") as file:
#     lst = []
#     for line in file:
#          lst.extend(line.rstrip().split())
#
# print(lst)
#
# max_len = 0
# number = 1
# s = ""
# for id, line in enumerate(lst):
#     if len(line) > max_len:
#         max_len = len(line)
#         s = line
#         number = id + 1
# print(s)
# print(max_len)
# print(number)

# csv - comma separate values (набор данных разделенный запятой, точкой с запятой, точкой и т.д.)
# import random
# import csv
#
# lst = [str(random.randint(1,10)) for _ in range(100)]
# # print(lst)
# # print()
# # with open('test csv.csv','w') as file_csv:
# #     file_csv.write(';'.join(lst))
# lst_read = []
# with open('test_csv.csv', 'r') as file_csv_read:
#     s = csv.reader(file_csv_read,delimiter=';')
#     print(s)
#     for el in s:
#         lst_read += list(map(int,el))
# print(lst_read)

# json
# import json
# person = {
#     "name" : "John",
#     "lastname" : "Watson",
#     "age": 24
# }
# # dump - для закидываения данных
# # dumps - сериализуе объект (число в строку сериализует)
# # print(repr(json.dumps([42, 2, 5, 2, 1])))
# with open("test_json.json", 'w', encoding='uft-8') as file_json:
#     json.dump(person, file_json,indent=4)
#
# with open("test_json.json",'r',encoding='uft-8') as file_json_read:
#     person2 = json.load(file_json_read)
#
# print(person2)





