# Циклы

# факториал
# n=int(input())
# s=1 -счетчик цикла
# result=1 - переменная которую ищем
# while s<=n: - пока элемент цикла меньше или равно числу которое вводим, будет идти цикл
#     result*=s - умножение 
#     s+=1 -новый круг
# print(result)

# фибонначи 01=1+1=2+1=3+2 (0112358)
# n=int(input())
# n0=0
# n1=0 
# n2=1
# i=2
# while n0<n: 
#     n0=n1+n2 
#     n1=n2
#     n2=n0
#     i+=1
#     if n0>n:
#         i=-1
# print(i)

# n=int(input()) -ввод количества чего либо
# k=0 - колво дней сколько оттепели
# max=0 - самая длинная оттепель 
# for i in range(n): - сколько раз идет цикл
#     x=int(input()) - вводит температуру 
#     if x>0:
#         k+=1 - оттепели на один день больше
#     else:
#         if max<k: макс оттепель меньше чем текушая 
#             max=k - 
#         k=0 - новый цик
# print(max)


# выбор наименьшего и наибольшего

# n=int(input())
# max=0
# min=3001
# for i in range(n):
#     x=int(input())
#     if x>max:
#         max=x
#     if x<min:
#         min=x
# print('Теще' , min)
# print('Себе', max)

# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

# coins = [0, 1, 0, 1, 1, 0]
# gerbCount=0
# reshkaCount=0
# for i in range(len(coins)):
#     if coins[i]==0:
#        gerbCount=gerbCount+1
#     else:
#        reshkaCount=reshkaCount+1
# if gerbCount<reshkaCount:
#    print(gerbCount)
# else:
#    print(reshkaCount)

# s = 12
# p = 27
# for y in range(1,1001):
#     for x in range(1,y+1):
#         if x+y==s and x*y==p:
#             print(x,y)

# n=16
# k=1
# result=1
# while result<=n:
#     print(result) 
#     result*=2
#     k+=1 



    

    



