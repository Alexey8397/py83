# Тема циклы. Циклы - повторение чего-либо.

# №1 цикл с параметром(когда вы знаете конечное число элементов в объекте (цикл перебора с объектом)
# №2 цикл с условием
# for(для, от)
# for var in (итерируемый объект)
# for elem in range(1,10,1):
#     print(elem)
# range(start,stop,step)
# range(1,5,1) 1 2 3 4
# range(1,5) 1 2 3 4 # если шаг равен 1 можно не писать
# range(5) 0 1 2 3 4
# for elem in range(10,0,-1):
#     print(elem,end="+")
# 012345678910
s = "hello world"
# перебор строки по элементам
# for symb in s:
#     print(symb,end=" ")
# print()
# # перебор строки по индексам
# length = len(s)
# for ind in range(len(s)):
#     print(s[ind])
# здесь мы вывели все числа кратные на промежутке от 0 до 100
for numb in range(1,101):
    if numb % 5 == 0:
        print(numb**2,end=" ")
# найти сумму всех чисел на промежутке от 10 до 50
# summa = 0
# for numb in range(10,51):
#     summa += numb
# print(summa)

# дано число, вывести все его делители
# 10 - 1 2 5 10
# 12 - 1 2 3 4 5 6 12
# number = int(input())
# for numb in range(1,number + 1):
#     if number % numb == 0:
#         print(numb,end = " ")



