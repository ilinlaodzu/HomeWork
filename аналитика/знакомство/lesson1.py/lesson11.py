
# transformation = lambda x: x
# values=[1,23,42,12,45,67,89]
# transformed_values=list(map(transformation,values))
# if values ==transformed_values:
#     print('ok')
# else:
#     print('fail')

# from math import pi
# def find(list_of_orbits):
#     list = [i for i  in list_of_orbits if i[0] !=i[1]]
#     # != не равняется 0 и 1 элементы, ддля того , чтобы найти эллипс
#     list_s = [(pi*i[0]*i[1]) for i in list]
#     # list умножили 0 и 1 элемент кортежа, нашли площадь
#     # найти площадь максимального
#     max_s=list_s.index(max(list_s))
#     return list[max_s]
# orbits=[(1,3),(2,5),(7,2),(6,6),(4,3)]
# # создать новый список, гле буддем хранить эллипсы
# # find(orbits)
# print(*find(orbits))
# # *распаковка кортежа

# def same_by(char,object):
#     res=True
#     list=[char(x) for x in object]
#     for i in range(len(list)-1):
#         if list[i] !=list[i+1]:
#             res=False
#     return res
# values=[2,3,4,5,6,7,8,9]
# if same_by(lambda x: x%2, values):
#     print('same')
# else:
#     print('different')


# def print_operation_table(operation, num_rows, num_columns):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"ОШИБКА! Размерности таблицы должны быть больше 2!" for x in i])
#     if num_rows<2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]
#     for i in res:
#         print(*[f"{x} " for x in i])


	

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     for i in range(1, num_rows + 1):
#         a = []
#         for j in range(1, num_columns + 1):
#             a.append(str(operation(i, j)))
#         if num_rows<2:
#             print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#             return
#         print(" ".join(a))
# print_operation_table(lambda x, y: x * y)


# def r(str):
#     list_1=str.split()
#     isRitm = True
#     tmp = -1
#     if (len(list_1))<=1:
#         print('Количество фраз должно быть больше одной!')
#     else: 
#         for word in list_1:
#             sum = 0
#             for i in word:
#                 if i in 'аеёиоуыэюяАЕЁИЩУЫЭЮЯ':
#                     sum += 1
#             if (tmp != -1 and tmp != sum):
#                 isRitm = False
#                 break
#             else:
#                 tmp = sum
#         if (isRitm):
#             print('Парам пам-пам')
#         else:
#             print('Пам парам')        
    
# r(stroka)

# def r(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum += 1
#         list_1.append(sum)
#         return len(list_1) == list_1.count(list_1[0])
#     if (sum)==1:
#         print('Количество фраз должно быть больше одной!')
    


# stroka = 'Пух'
# if r(stroka):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

def r(str):
    str = str.split()   
    list_1=[]
    if len(str) < 2:
         print('Количество фраз должно быть больше одной!')
    else:  
        for word in str:
            sum = 0
            for i in word:
                if i in 'аеёиоуыэюя':
                    sum += 1
                    list_1.append(sum)
    return len(list_1) == 

stroka = 'Пух'
if r(stroka):
    print('Парам пам-пам')
else:
    print('Пам парам')