# списки по сути массив

# генератор списка
# list_1 = [exp for iten in iterable]

# list_1 = [exp for iten in iterable (if conditional)]

# 1 способ генерайции списков
# list_1=[] 
# for i in range (1,100):
#     list_1.append(i)
# print(list_1)
    
# 2 способ генерайции списков
# list_1=[i for i in range(1,101)]
# print(list_1)

# только четные числа
# list_1=[i for i in range(1,101) if i%2 ==0]
# print(list_1)

# пары каждому из чисел
# list_1=[(i,i) for i in range(1,101) if i%2 ==0]
# print(list_1)

# list_1=[1,1,2,0,-1,3,4,4]
# print(len(set(list_1))) , len -считает элементы массива, set  - уникальные элементы определяет

# умножать, делить и т.д
# list_1=[i*2 for i in range(10) if i%2 ==0]
# print(list_1)

# list_1=[] -пустой список

# list_1=[2 , 4 , 4, 7 ] - список со значениями 

# print(*list_1) - просто выводит значение * - убирает квадратные скобки

# for i in значение  - перебирает значение в списке
# for i in list_1:
#     print(i)

# print(len(list_1)) -выводит количество элементов в списке

# print(list_1[3]) - в скобочках элемент к которому хотим c начала обратиться

# print(list_1[-1]) - в скобочках элемент к которому хотим с конца обратиться

# list_1=[1, 5]
# print(list_1)
# list_1.append(9)-добавляет в конец списка элемент
# print(*list_1)

# list_1=[]
# for i in range(5):
#     list_1.append(i)
#     print(*list_1)
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# list_1 = [12,5,89,13]

# удаление последнего элемента в  списках
# print(list_1.pop())
# print(list_1)

# удаление конкретного элемента из спискf
# print(list_1.pop(1))
# print(list_1)

# добавление элемента в нужную позиицию
# print(list_1.insert(2,345)) - 2 - номер элемента, 345 - число, которое нужно вставить
# print(list_1)

# выводим значение определеенного элемента из списка
# print(list_1[3]) -выводим 3 элемент
# print(list_1[-2]) - предпоследний элемент
# print(list_1[:]) - [12, 5, 89, 13] -выводит значение списка с начала
# print(list_1[ :2]) - [12, 5] сначала и до 2 индекса
# print(list_1[len(list_1)-2:]) - [89, 13] - последние  2 элемента
# print(list_1[0:2]) - [12, 5] - интервалjn от 0 до 2 элемента
# print(list_1[0:len(list_1):2]) - cначала и с шагом 2

# Кортеж - неизменяемый список
# t=()
# print(type(t))
# t=(1,4,5,)
# print(type(t))

# преобразование списка в кортеж
# v=[1,4,5,6]
# print(v)
# print(type(v))
# v=tuple(v)
# print(v)
# print(type(v))

# # a =d =1
# # c=2

# a,b,c = v
# print(a,b,c)


# t=(1, 3, 2, 4, 5, )
# print(t[1])- выводит элемент 1 из кортежа
# проход по списку, выводит все
# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(t[i])

# нельзя поменять так как кортеж
# t[0] = 2
# print(t)

# словарь -доступ по ключу, нет индексов
# d={'food', 'good', 'left'}
# d=dict()
# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['w'])

# добавление элементов в словарь
# d[987]=68868968
# print(d)
# print(d.items())

# del d["food"] - удаление эленмента
# print
# for item in d:
#     print('{})

# print(d)
# d.add('food')
# print(d)
# d.clear()
# print(d)

# операции с перечсечениями
# a={4, 6, 5, 4, 3, 2}
# b={5, 3, 4, 5, 6, 67}
# c=a.copy() -c копирует а, 
# u=a.union(b)  - одинаковые не копирует
# print(u)
# i=a.intersection(b) -пересечения-одинаковые
# print(i)
# d=a.difference(b) - есть в а, нет в б
# print(d)
# d=b.difference(a)  - есть в б, нет в а
# print(d)
# q=a.union(b).difference(a.difference(b))
# print(q)

# замороженное множесмтво? когда нельзя изменять множество
# a={1,3,4,5,6}
# b=frozenset(a)
# print(b)