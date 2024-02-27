# # 2 массива чисел , найти в 1 , которых нет во 2
# n=int(input())
# x=0
# list_1=list()
# for i  in range(n):
#     x=int(input())
#     list_1.append(x)
# m=int(input())
# list_2=list()
# for i  in range(m):
#     x=int(input())
#     list_1.append(x)

# count =0
# for i in range(n):
#     for j  in range(m):
#         if list_1[i]==list_2[j]:
#             count+=1
#     if count==0:
#         print(list_1[i])
#     count=0
        
# проход по массиву и сравнение элементов который мениьше
# n=int(input())
# list_1=list()
# x=0
# count =0
# for i in range(n):
#     x=int(input())
#     list_1.append(x)
# for i in range(1,n-1):
#     if list_1[i-1] < list_1[i] and list_1[i]>list_1[i+1]:
#         count+=1
# print(count)

#  список,сколько пар одинаковых чисел
# list_1=[1,2,3,2,3]
# count =0
# for i in range(len(list_1)):
#     for j in range(i+1, len(list_1)):
#         if i !=j and list_1[i]==list_1[j]:
#             count+=1
# print(count)

# дружественные числа до 300
# k=int(input())
# list_1=list()
# for i in range(k):
#     sum=0
#     for j in range(1,i//2+1):
#         if i % j ==0:
#             sum+=j
#     list_1.append(tuple([i,sum])) - создали кортеж

# for i in range(len(list_1)): - определение одинаковых элеементов
#     for j in range(i, len(list_1)):
#         if i!=j and list_1[i][0]==list_1[j][1] and list_1[i][1]==list_1[j][0]:
#             print(*list_1[i]) -* раскрыла скобки кортежа



