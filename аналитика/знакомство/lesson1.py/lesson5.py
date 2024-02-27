# list_1=[1,1,2,0,-1,3,4,4]
# list_1_unique=[]
# for i in list_1:
#     if i not in list_1_unique:
#         list_1_unique.append(i)
# print(len(list_1_unique))

# цуклически меняеит местами значение , стало [5, 4, 3, 1, 2]
# list_1 =[1,2,3,4,5]
# k=3
# list_res=[]
# for i in range(k):
#     list_res.append(list_1[len(list_1) -1 -i])
# for i in range(len(list_1)-k):
#     list_res.append(list_1[i])
# print(list_res)

# a=[{'V': 'S001'},{'VI': 'S002'} , {'VII': 'S003'},
# {'V': 'S001'},{'VI': 'S002'} , {'VIII': 'S003'} ]
# # set_1=set()
# # for i in a:
# #     for j in i:
# #         set_1.add(i[j]) 
# # print(set_1)

# list_1=[6,-7,6,8,9,2,3]
# count=0
# for i in range(1,len(list_1)):
#     if list_1[i] > list_1[i-1]:
#         count+=1
# print(count)

# list_1=[]
# k=int(input)
# for i in range(10):
#     list_1.append(i)
#     print(*list_1)
#     if 

# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# sum=0
# for i in list_1:
#     if i==k:  
#         sum+=1
# print(sum)


# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# # list_1 = [1, 2, 3, 4, 5,6,7,8,9,10]
# list_1=[i for i in range(1,21)]
# print(list_1)
# list_1 = [2, 4, 1, 6, 8, 2, 3, 2, 5]
# k = 5
# element=int()
# diff=abs(list_1[0]-k)
# # diff=int()
# print(element)
# # print(diff)
# for i in list_1:
#     if abs(i-k) < diff:
#         element=i
#         diff=abs(i-k)
# print(element)

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так: 
# a_1="AEIOULNSTRАВЕИНОРСТ"
# b_2="DGДКЛМПУ"
# c_3="BCMPБГЁЬЯ"
# d_4="FHVWYЙЫ"
# # l_5="KЖЗХЦЧ"
# m_8="JXШЭЮ"
# s_10="QZФЩЪ"
# k = 'ноутбук'
# k=k.upper()
# sum=0
# for i in k:
#     if i in a_1:
#         sum=sum+1
#     elif i in b_2:
#         sum=sum+2
#     elif i in c_3:
#         sum=sum+3
#     elif i in d_4:
#         sum=sum+4
#     elif i in l_5:
#         sum=sum+5
#     elif i in m_8:
#         sum=sum+8
#     elif i in s_10:
#         sum=sum+10
# print(sum)










 