# 3. Удалить в строке все буквы 'b', непосредственно за которыми идёт цифра.
# s = "asbdasdqb2bdsad21ds2bdasb2" + " "
# temp = ""
# for i in range(len(s)):
#     if s[i] == 'b' and s[i+1].isdigit():
#         continue
#     temp += s[i]
# print(s)
# print(temp)

# 4. Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# Написать программу определяющую количество слов,
# заканчивающихся одной и той же буквой 'k'.
# s = 'fqwfqwfq   d   dqwdk    dkqwdqwdk    dqwdk d qw qdwdgk'
# lst = s.split()
# print(lst)
# print(len([elem for elem in lst if elem[-1] == 'k']))
# count = 0
# for elem in lst:
#     if elem[-1] == 'k':
#         count += 1
# print(count)
s = 'fqwfqwfq  d   dqwdk    dkqwdqwdk    dqwdk d qw qdwdgk' + " "
# temp = ""
# count = 0
# for ind in range(len(s)):
#     if s[ind] != ' ':
#         temp += s[ind]
#     elif temp:
#         if temp[-1] == 'k':
#          print(temp)
#         temp = ''
# print(count)
# print(len([s[ind] for ind in range(len(s)) if s[ind] == 'k' and s[ind+1] == " "])) # генератор

# # 6
# lst = [int(i) for i in input().split()]
# print(lst)
# lst2 = []
# if len(lst) == 1:
#     print(lst)
# else:
#     for i in range(len(lst)): # 0 1 2 3 4
#         if i == 0:
#         lst2.append(lst[-1] + lst[1])
#         elif i == len(lst) - 1:
#         lst2.append(lst[-2] + lst[0])
#     else:
#         lst2.append(lst[i-1] + lst[i + 1])
# print(lst2)

# 7. Дан список, упорядочнный по не убыванию элементов в нём.
# Определить, сколько в нём различных элементов.
# lst1 = [ 1, 2, 2, 2, 6, 7, 10, 10, 12]
# lst2 = []
# for elem in lst1:
#     print(lst1.index(elem),elem) # первый способ по индексу

# lst1 = [ 1, 2, 2, 2, 6, 7, 10, 10, 12] # задачи, где нужно отдельно считать индексы или элементы
# lst2 = []
# for ind,elem in enumerate(lst1):
#     print(ind, elem)

# lst1 = [ 1, 2, 2, 2, 6, 7, 10, 10, 12]
# lst2 = []
# for ind in range(len(lst1)):
#     if lst1[ind] not in lst2:
#         lst2.append(lst1[ind])
# print(len(lst2))

# lst1 = [ 1, 2, 2, 2, 6, 7, 10, 10, 12]
# lst1 = [ 1, 1, 1, 1, 1, 1, 1, 1]
# count = 0
# for i in range(len(lst1)-1):
#     if lst1[i] < lst1[i+1]:
#         count += 1
# if lst1[-2] < lst1[-1]:
#     count += 1
# print(count)

# lst1 = [ 1, 2, 2, 2, 6, 7, 10, 10, 12]
# lst1 = [ 1, 1, 1, 1, 1, 1, 1, 1]
# count = 1
# ind = 0
# while ind < len(lst1):
#     if ind == len(lst1)-2:
#         count += 1
#     break
#     if lst1[ind] < lst1[ind + 1]:
#         count += 1
#     ind += 1
# print(count)

# # если какое-то условие не хотим выводить
# number = int(input())
# count = 0
# summa = 0
# while number != 0:
#     summa += number
#     count += 1
#     number = int(input())
#     if number > 10:
#         break
# else: # если условия break не сработает, выведет count(команда else)
#     print('braak не исполнился')
#     print(count)
#
# print(summa)
# # print(count)

# str list
# множества (почти не встречаются). замороженное множество(очень редко встречается)

# set_1 = {5,  5, 2, 2, 4, 'Hello', 'hello', 4.22, (4, 2, 1),True} # пустое множество ({})
# print(set_1)
# # set_1.add(9) # добавить в множество. для неизменямых объектов
# # если есть цифра "1" Thue and False не выведет
# # строки, числа и так далее, не изменяемый элементы могут храниться
# # # set_1.update("home".split()) # добавляет любой элемент распакованным
# # set_1.pop()
# # var = set_1.pop() # удаление случайного элемента и его возращение
# # print(var)
# # set_1.discard(5) # удаляет элемент, если он есть
# # set_1.remove(5) # вернёт ошибку (если элемента нет в списке)
# # if 5 in set_1:
# #     set_1.remove(5)
# # set_1.clear() # удаляем все элементы
# print(set_1)

# понадобиться в задачах
# set_1 = {2, 6, 7,}
# set_2 = {2, 3, 6, 7, 11}
# print(set_1.issubset(set_2))
# print(set_2.issuperset(set_1))
# # print(set_1.update(set_2))
# print(set_1.intersection_update(set_2))
# print(set_2.difference_update(set_1))
# print(set_1.symmetric_difference(set_2)) # можно коротко "^"
# print(set_2)
# set1 = {4,2,1,5}
# f_set1 = frozenset(set1) # показывает пересечение с другими множествами # не изменяемый объект
# for elem in f_set1:
#     print(f_set1)

# Даны два списка чисел. Найдите все числа
# которые не содержатся одновременно в этих двух списках.
# set = [5, 2, 6, 1, 2, 5, 2]
# lst_2 = [5, 2, 5, 1, 2, 9]
# set1 = set(lst)
# set2 = set(lst_2)
# print(set1 ^ set2)


# словари (dict) (key: value) ассоциативный массив
# ключи нельзя заменить, а номера в словаре можно менять
#         key      value
# key unique(уникальны), unmutable(неизменяемы)
# key - str int float bool tuple
# value - любой(могут повторяться)
# friend_phones = {"Vasya":321748721,'Anna':12421412, "Pavel": 421512}
# for key in friend_phones:
#     print(key,friend_phones[key]) # друзей
# for friend, phone in friend_phones.items():
#     print(friend_phones) # телефоны друзей
# for phone in friend_phones.values():
#     print(phone) # телефоны
# friend_phones = {"Vasya":321748721,'Anna':12421412, "Pavel":421512}
# friend_phones["Angelina"] = 43634634
# friend_phones["Vasya"] = 421412412 # добавить номер или заменить текущий
# print(friend_phones)
# if "Paul" not in friend_phones:
#    friend_phones.update({"Paul": 242424242121,"Sergey":413413513})
# print(friend_phones)
# friend_phones.pop("Vasya") # удалим, если есть
# print(friend_phones)
# friend_phones = friend_phones.fromkeys([5, 2, 5, 2], 42)
# print(friend_phones)
# friend_phones.get('Vasya') # вывести номер
# print(friend_phones.get('Vasya'))





