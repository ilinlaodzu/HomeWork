# функция def
# def sum_numbers(n,y='mmm'):
#     summa=0
#     for i in range (1, n+1):
#         summa+=i
#     return summa
#     print('stop')
# print(sum_numbers(5,'nvnvn'))

# функция , которая будет 
# принимать в себя неограниченное количесвто аргументов
# def sum_str(*args):
#     res=''
#     for i in args:
#         res+=i
#     return res
# print(sum_str('d', 'a','f'))
#  ответ daf

# модуль (импорт)
# import lesson6_2 as l62
# print(l62.max1(5,6))

# фиббоначчи
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1)+fib(n-2)- суммирование предыдущих
# list_1=[]
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)
# [1, 1, 2, 3, 5, 8, 13, 21, 34]

# алгоритмы
# сортировка быстрая большое на маленькое угадать число
# quick_sort - сортировка 
# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot=array[0] - первое значение 
#     less=[i for i in array[1;] if i<=pivot] - генерация массива
#     great=[i for i in array[1;] if i>pivot] - генерация массива
#     return quick_sort(less)+[pivot]+quick_sort(great)
# print(quick_sort)

# сортировка слияние  -делим на 2
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

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.
# def f(a, b):
#      if  b == 0:
#          return 1
#      elif b == 1:
#          return a
#      else:
#          return a * f(a,b-1)

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# def sum(a,b):
#     if a==0:
#         return b
#     if b==0:
#         return a
#     return a+b
# print (sum(2,3))


