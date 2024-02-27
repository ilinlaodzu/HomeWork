# str=input().split() -вводж строки и преобразование ее в массив
# res={}
# # print(str)
# for i in str:
#     if i in res:
#         print ( f'{i}_{res[i]}', end= ' ')
#     else:
#         print (i, end=' ')
    
#     res[i]=res.get(i,0) + 1

# stroka=input().split()
# set_1=set()
# for i in stroka:
#     set_1.add(i.lower())
# print(len(set_1))

# import random
# n=random.randint(0,10)
# max=-1
# max=n
# while n!=0:
#     n=random.randint(0,10)
#     print(n)
#     if n>max:
#         max=n
# print(max)
    


# словари, множества , профилирование 
#  сколько раз каждый символ встречался, кол-во повторов добавляется 
# к символам с полмощью профикса формата _N
# stroka=input().split()
# # преобразование строки в массив
# res={}
# for i in stroka:
#     if i in res:
#         print(f'{i}_{res[i]}',end=' ')
#     else:
#         print(i,end=' ')
# res[i]=res.get(i,0) + 1
# если на вход новая буква, в словаре рес 
# создаем новое значение
# ключ i, который преобретает новое значение 

# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5'
# mas_1=str.split(var2)
# mas_2=str.split(var3)
# resalt=set(mas_1).intersection(mas_2)
# sorted_resalt=sorted(resalt,reverse=False)
# из массива в строку
# string = ' '.join(str(sorted_resalt) for sorted_resalt in sorted_resalt) 
# print(string)

arr = [5, 9, 6, 4, 9, 9, 7, 3]
max=0
sum=[]
for i in range (0,len(arr)):
    if i==0:
        sum.append(arr[i]+arr[i+1]+arr[len(arr)-1])
    elif i==len(arr)-1:
        sum.append(arr[len(arr)-2]+arr[len(arr)-1]+arr[0])
    else:
        sum.append(arr[i-1]+arr[i]+arr[i+1])
sorted_sum=sorted(sum,reverse=False)
max=sorted_sum[len(sorted_sum)-1]     
print(max)
