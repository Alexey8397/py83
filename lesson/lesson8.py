# unmutable(неизменяемая) в функцию передаются по значению
# mutable в функцию передаются по ссылкам
# name = "Vova"
#
# def greeting(name):
#     # процедура (функция, которая ничего не возврашает)
#     # "str,int - нотации(подсказки, что должно будет быть вызвано)
#     # local scope - локальная облость
#     name = name.capitalize()
#     print(f"hello {name}")
#     return name
# name = greeting(name)
# print(name)
# peolpe = ['Karl',"Vasya","Petya"]
# def workers():
#     peolpe.append("Anna")
#     print(peolpe)
# workers()
# "*" позиционный аргумент (args) любая переменная с "*"
# менять менстами нельзя(привязано по ключу) только если по ключу передадим значение
# "**" kwargs key words arguments приходит как пара слов, которые приходят по ключу
# def workers(date,*args,balance,balance_many = 1000, **kwargs):
#     print(date)
#     print(balance)
#     print(args)
#     print(**kwargs)
#
# workers('06.08.1992','Vasya','Petya','Anna', balance=510000,
#         balance_many=998, balance1=421, balance2=429, balance3=488)
# def fun(*args,**kwargs): # все аргументы в таком виде примутся

# анонимные функции (используются один раз)
# fun = lambda x,y: x + y
#
# def fun_2(x,y):
#     return x + y


# print(fun_2(2,1))
# print(fun(5,2))
# def chet(number):
#     return number % 2

# сортировка

# kr = lambda x: True if x % 3 == 0 else False # тернарная операция(вывод в одну строку
# # print(kr(7))
# lst = [8,9,2,6,1,7]
# lst.sort(key=kr)
# print(lst)

# сортировка имён по первой букве
# print(kr(7))
# lst = ["John","Marz","Jack","Willy"]
# # lst.sort(key = lambda x: x[-1]) # сортировка по последней букве
# lst.sort(key = lambda x: len(x)) # сортировка по длинне
# print(lst)

# map
# lst = (input().split())
# a = int(lst[0])
# a = int(lst[1])
# a = int(lst[2])

# lst = [5, 2, 5, 1, 7, 2]
#
#
# lst = list(map(lambda x: x ** 3 if x%2 ==0 else x ** 5, lst)) # возвело числа в куб
# print(lst)

# lst = [5, 2, 5, 1, 7, 2]
# balance = {"John":231, "Mark": 199, "Anna":120}
#
# for name in map(lambda name,money: balance[name]+20 if balance[name] < 200 else balance[name], balance):
#     print(name,balance[name])

# # filter
# lst = [5, 2, 6, 1, 6, 7, 1]
# lst_2 = list(filter(lambda x: not x % 2, lst)) # фильтрует список по чётным числам
# print(lst_2)

# lst = [5, 2, 6, 1, 6, 7, 1]
# lst_2 = list(filter(lambda x: not x % 2, lst)) # оставим то, где есть буква "о"
# words = ["hell","world","price",'gold']
# words2= list(filter(lambda elem: 'o' in elem, words))
# print(words2)

# lst = [5, 2, 6, 1, 6, 7, 1]
# lst_2 = list(filter(lambda x: not x % 2, lst)) # выводит все слова с двумя гласными
# words = ["hello","world","price",'gold']
# words2= list(filter(lambda elem: len([sym for sym in elem if sym in "aeyuio"]) == 2, words))
# print(words2)

# global
# x = 2
# def fun():
#     global x # обращаемся к внутренней и наружней функции
#     x += 3
#     print(x)
#
# fun()

# def fun(numb):
#     def wrapper():
#         print("Hello")
#         print(numb)
#     wrapper()
# fun(42)

# облости:
# bgel
# global
# local
# enclosing
# build it (встроенная функция)

# def fun(numb):
#     def wrapper():
#         nonlocal numb # используется как замыкающая облость (nonlocal)
#         numb += 1
#         print(numb)
#     wrapper()
# fun(42)

# def person(name):
#     def wrapper():
#         print(name.capitilize())
#     return wrapper
#
# print(person("Oleg"))

# def person(name):
#     def wrapper():
#         print(name.capitilize())
#     return wrapper
#
# p = person("oleg")
# p()
# p()
# p()
# p()
# # closure (замыкающая облость) запоминает историю изменения объекта. Можно к переменной
# которую мы запомнили, прибавлять значение

# добавляет или отнимает к запоминающемуся объекту

# запоминающиеся данные в фунциях

# def counter(x):
#     def wrapper(a):
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper
# c = counter(0)
# c(1)
# c(1)
# c(1)
# c(1)

# декоратор - это фунция принимает функцию, её же модернизирует и возвращает

# def say():
#     print("Hello")
#
#
# def decorator(fun):
#     def wrapper():
#         print("before decorated")
#         fun()
#         print("after decorated")
#     return wrapper
#
# decor_say = decorator(say)
# decor_say()

# def greeting(name: str):
#     return 'hello' + name
#
# def decorator(fun):
#     def wrapper(name: str):
#         if name.capitalize() == name:
#             return fun(name)
#         else:
#             return 'hello ' + name.capitalize()
#
#     return wrapper
#
#
# decor_gr = decorator(greeting)
# # print(greeting('peter'))
# print(decor_gr('peter'))

# users = {"John":1234,"Jack":590,"Anna":900}
#
#
# def balance(**kwargs):
#     for name,price in kwargs.items():
#         if price < 1000:
#             kwargs[name] += 100
#     return kwargs # return для возврата функции
#
# users = balance(**users)
# print(users)





























































