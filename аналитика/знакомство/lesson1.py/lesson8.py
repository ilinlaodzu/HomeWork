# # фибонначи 0 1 1 2 3 5 8 13 21
# # рекурсия 
# def f(n):
#     if n==0 or n==1:
#         return 1
#     return f(n-1)+f(n-2)
# n=int(input())
# print (f(n-2))

# замена максимальных на минимальных
# n=int(input())
# list1=list()
# for i in range(n):
#     x=int(input())
#     list1.append(x)
# max_n=max(list1) -конструкция ищет макс 
# min_n=min(list1) - ищет мин
# for i in range (len(list1)): -меняет 
#     if list1[i]==max_n:
#         list1[i]=min_n
# print(list1)

# ищет простое число
# def prime(n):
#     flag=True - переменные делители
#     i=2
#     while i<n and flag: пока i<n ищем простые числа делим на 1 или саму себя
#         if n%i==0:
#             flag=False
#         i+=1
#     if flag:
#         return 'yes'
#     else:
#         return 'no'
# n=int(input())
# print(prime(n))

# обратный порядок сделать
# def f(n):
#     if n==0: -нужно, чтобы закончить. выйти
#         return '' -пока не будет равен, рекурсия не остановится
#     k =int(input())
#     return f(n-1)+f'{k}' - сама рекурсия 
# n=int(input())
# print(f(n))
