# # словари, множества , профилирование 
# #  сколько раз каждый символ встречался, кол-во повторов добавляется 
# # к символам с полмощью профикса формата _N
stroka=input().split()
# # преобразование строки в массив
res={}
for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}',end=' ')
    else:
        print(i,end=' ')
          
    res[i]=res.get(i,0) + 1
# # если на вход новая буква, в словаре рес 
# # создаем новое значение
# # ключ i, который преобретает новое значение 
    

# сколько слов в тексте одинаковых
# set= множество
# униkальность ,используем множество
# stroka=input().split()
# set_1=set()
# # пройдемся по массиву
# for i in stroka:
#     set_1.add(i.lower())
# # считаем его размер len
# print(len(set_1))



