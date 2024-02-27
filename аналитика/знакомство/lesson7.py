# функции

# def sum_n(n):
#     summa=0
#     for i in range(1,n+1):
#         summa +=i
#     print (summa)
# sum_n(3)

# def sum_n(n):
#     summa=0
#     for i in range(1,n+1):
#         summa +=i
#     return summa
# print (sum_n(3))

# def sum_n(n, y='Hello'):
#     summa=0
#     for i in range(1,n+1):
#         summa +=i
#     return summa
# print (sum_n(3,'qwerty'))

# принимает неограниченное количесвто аргументов поставить *
# def sum(*args):
#     res=''
#     for i in args:
#         res+=i
#     return res
# print (sum('q','w','e','r', 't','y'))
# qwerty


# модуль - в отдльном файле множество функций

# def max(a,b):
#     if a>b:
#         return a
#     # else:
#     return b
# отсюда ушли данные в lesson7.1


# рекурсия

# фибонначи (1+1=2,1+2=3, и т.д. )
# def fib(n):
#     if n in [1,2]:  - базис обязателен
#         return 1
#     return fib(n-1)+fib(n-2) - прошлое +позапрошлое
# list_1=[] - собирает значения 
# for i in range(1,10): - значения от 1 до 10 сумма 
#     list_1.append(fib(i))

# алгоритмы  сортировка (быстрая)

# def qw(array): сортировка масва
#     # if len(array)<=1: еслидлина массива меньше  1 возвращаем массив
#         return array иначе что то делаем
#     else: - рекурсия 
#         pi =array[0] -куда сохранаяется 
#         less=[i for i in array [1:] if i<=pi]   - где хранится меньше значение первого элемента  pi, генерация списков 1: срез списка по всему спска которые меньше pi 
#         grea=[i for i in array [1:] if i>pi]  - где хранится большее значение первого элемента  pi
#         return qw(less)+[pi]+qw(grea) - сортировка qw , [pi] - стал с вписок, так как был число
# print (qw([1,3,4,5,6,7,8,9,767,6]))


# сортировка
# def merge_sort (nums):
#     if len(nums)>1:
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i=j=k=0
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 nums[k]=left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k] = right[j]
#             j+=1
#             k+=1
# list1 = [1,5,4,23,2,54,5,56,44,4,3]
# merge_sort(list1)
# print (list1)