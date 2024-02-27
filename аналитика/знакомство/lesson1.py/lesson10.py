# Урок 10. Лекция. Функции высшего порядка, работа с файлами
# def f(x):
#     return x*x
# a=f
# print(a(5))
# print(f(5))

# def cal(a):
#     return a*a
# def call(a):
#     return a+a
# def mat(op,x):
#     print(op(x))
# mat(cal,5) - в mat передали функцию cal


# def cal(a,b):
#     return a*b
# def call(a,b):
#     return a+b
# def mat(op,x,y):
#     print(op(x,y))
# mat(call,5,7)

# def cal(a,b):
#     return a*b
# def mat(op,x,y):
#     print(op(x,y))
# cal = lambda a,b: a+b 
# mat(lambda a,b: a+b,5,7)

# определить четные числа и составить из них пары 1 2 3 4 6 78 999 890
# data =[1, 2 ,3 ,4 ,6 ,78 ,999, 890]
# res =list()
# for i in data:
#     if i%2==0:
#         res.append((i,i**2))
# print(res)

# data =[1, 2 ,3 ,4 ,6 ,78 ,999, 890]
# def select(f,col):
#         return[f(x) for x in col]
# # # возвращает список к каждому F
# def where(f,col):
#         return [x for x in col if f(x)]
# # # прошли проверку F(x)
# res = select(int,data)
# print(res)
# res= where (lambda x: x % 2==0,res)
# print(res)
# res = list(select(lambda x: (x,x**2),res)) 
# print(res)
# [(2, 4), (4, 16), (6, 36), (78, 6084), (890, 792100)]

# map - 2 значения
# 1 - lambda x: x+10 - к какому объекту (х)
# 2 - list_1 - сам объект

# list_1 = [x for x in range (1,16)]
# print(list_1)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# list_1=list(map(lambda x: x+10, list_1))
# print(list_1)
# # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# лист строк в лист чисел
# .split() - преобразует строку в список
# data = '12 34 45 56 78 67'

# print(data)
# 12 34 45 56 78 67
# data = data.split()
# print(data)
# ['12', '34', '45', '56', '78', '67']

# по-другому через map & split()
# data = list(map(int,data.split()))
# print(data)
# [12, 34, 45, 56, 78, 67]


# data =[1, 2 ,3 ,4 ,6 ,78 ,999, 890]
# def where(f,col):
#         return [x for x in col if f(x)]
# # # прошли проверку F(x)
# res = map(int,data)
# print(res)
# res= where (lambda x: x % 2==0,res)
# print(res)
# res = list(map(lambda x: (x,x**2),res)) 
# print(res)
# [(2, 4), (4, 16), (6, 36), (78, 6084), (890, 792100)]

# filter включает 2 объекта 
# 1 - сама функция (lambda x: x%4
# 2 - объект data)
# data =[1, 28 ,3 ,8 ,6 ,78 ,999, 890]
# res=list(filter(lambda x: x%4 ==0,data))
# print(res)
# # [28, 8]

# data =[1, 28 ,3 ,8 ,6 ,78 ,999, 890]
# res = map(int,data)
# print(res)
# res= filter (lambda x: x % 2==0,res)
# print(res)
# res = list(map(lambda x: (x,x**2),res)) 
# print(res)
# [(28, 784), (8, 64), (6, 36), (78, 6084), (890, 792100)]

# zip  1j2 3i4 будет 13 ji 24 кортеж
# us=['i','h','d', 'u', 't']
# id=[1,2,3,4]
# res=['q', 'a', 'z','c','w']
# data=list(zip(us,id,res))
# print(data)
# [('i', 1, 'q'), ('h', 2, 'a'), ('d', 3, 'z'), ('u', 4, 'c')]
 
# enumerate -нумерует объекты (индексы)
# us=['i','h','d', 'u', 't']
# data=list(enumerate(us))
# print(data)
# [(0, 'i'), (1, 'h'), (2, 'd'), (3, 'u'), (4, 't')]

# a- дописывать в файл, в несуществующем начнется запись
# r- открытие для чтения, если нет  файла, ошибка
# w - записывать данные и созлдавать файл
# w+ - открывает для записи и создает, если его нет
# r+ - открыть и дописывать, если нет, ошибка

# col = ['red', 'green','blue']
# data = open('file.txt', 'a')  -сoздается новый файл , в который входят данные col
# data.writelines(col)
# data.close()

# with open('file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# print(56)
# в file.txt  файле поменялись данные на 
# line 1
# line 2

# path='file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# for i in  range (len(list_1)):
#     if list_1[i] >=min_number and list_1[i] <=max_number:
#         print(i)

# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов 
# n будет задано автоматически. 
# Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# a1 = 2
# d = 3
# n = 4
# an= [a1+(i-1)*d for i in range (1,n + 1)]
# for i in an:
#     print(i)













