# var1 = 5
# var2 = 4
# print(var1, var2)
# temp = var1
# var1 = var2
# var2 = temp
# print(var1,var2)
# var1, var2 = var2, var1
# print(var1,var2)

# логические выражения(boolean)
# >(больше) >= (больше или равно) <(меньше) <=(меньше или равно) != (не равно) ==(равно) is (есть)
# and(и) or (или) not(не) sor(одно или)
# var1 = 'hello world'
# var2 = 'hello world'.lower()
# print(var1)
# print(var2)
# print(id(var1),id(var2))
# print(var1 is var2)
# print(not 5 == 5 or 6 > 3)
# print(15 % 2 == 1)
# if если else иначе
# season = input('enter season of year')

# if season == 'winter':
# print('winter is here')
# elif season == 'autumn':
    # print('autumn is here')
# elif season == 'spring':
    # print('spring is here')
# elif season == 'sumer':
    # print('sumer is here')
# lse:
    # print('unknown season')

# var1 = 10
# var2 = 2
# exp = var1 > var2
# print(exp)
# if  exp:
#     print(var1)

# тернарный оператор
# что написать if условие верно else что написать
# number = int(input())
# print('чётное' if number % 2 == 0 else "нечётное")

# строки str '' ""
# \n перенос курсора \t табуляция \a перенос курсора в начало строки
# some_str = """
# hello world
# I learn python
# """
# some_str = some_str.replace('\n','')
# print(repr(some_str))

# str_1 = 'hello'
# str_2 = 'world'
# print(str_1 * 3)

# name[1] = 'a'
# numb = name.find('z')
# numb = name.index('z')
# print(repr(name))
# name = name.split()
# print(repr(name))
# name = 'John Watson'
# # slice (срез) str[start:end:step] str[start:end] str[::step]
# print(name[:4])
# print(name[5:])
# print(name[3:0:-1])
# print(name[::2])
# print(name[::-1])
# print(name[:2]+name[5:8])

# name1 = 'John'
# name2 = 'Pit'
# print(name1 < name2)

# name = 'John Watson'
# str1 = name[0:4]
# str2 = name[5:]
# print(str2)
# name2 = str2 + " " + str1
# print(name2)

# str1 = "192.168.0.1"
# print(str1.replace('.',''))
# print(str1([0:3])+ str1([4:7])+ str1([8])+str1([10]))

# 7) Дан прямоугольник со сторонами a см и b см, сколько квадратов со стороной 30 см можно отрезать от него.
# a и b задаются в одной строке с клавиатуры.
# Sample Input :
# 150 65
# Sample Output :
# Можно отрезать 10 квадратов.
# (a * b) / (30*30);

# num1, num2 = map(int, input().strip().split(" "))
# num1 = int(num1)
# num2 = int(num2)
# result = (num1 * num2) // (30 * 30)
# print("Sample Input :", int(num1), int(num2))
# print("Sample Output :", "Можно отрезать", result, "квадратов.")

# 6) Напишите программу, которая вычисляет сколько полных недель прошло за период, если прошло 182 дня.
number = int(input("Введите число : "))
print(int(number / 4000))
# или
print(number // 4000)










