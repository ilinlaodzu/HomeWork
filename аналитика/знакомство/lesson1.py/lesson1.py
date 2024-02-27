

# n = 4+7+8
# print(n)
# n = 'food'
# print(n)
# n1 = "root"
# print(n) 

# a=4
# b=4.55
# c="food"
# print(a,b,c)
# print(a, ' - ',  b, ' - ',  c)
# print (f"{a} - {b} - {c}")
# print("{} - {} -{}".format(a,b,c))

# print("Введите первое число ")
# n=input()
# print(n)

# print("Введите первое число ")
# n=input()
# m=input("Введите второе число ")
# print (n, "+", m, "=", n+m)

# v=3.45
# print(v)
# print(type(v))   
# # выводит тип на целое число 
# v=int(v)
# # int -значение целого числа
# print(v)
# print(type(v))

# v=4.4
# print(v)
# print(type(v))   
# # выводит тип на целое число 
# v=str(v)
# # int -значение целого числа
# # str - значение строки
# print(v + "45")
# # добавляем текст к строке
# print(type(v))

# c=5
# print(c)
# print(type(c))
# c=bool(c)
# print(c)
# print (type(c))

# print("Введите первое число:  ")
# a=int(input())
# b=int(input("Введите второе число:  "))
# print(a,"+", b, "=", a+b) 

# округление 
# a=3.56564
# b=4.78960
# print(round(a+b, 2))

# iter =1

# a=1>4
# print(a)

# a=1<4 and 2<5
# print(a)

# a=1==1
# print(a)

# a=1!=2
# print(a)

# a="food"
# b="good"
# print(a==b)

# a=1<3>23
# print(a)

# username=input("Введите имя: ")
# if username =="Маша":
#     print("Привет, Маша!")
# elif username == "Катя":
#     print("Привет, Катя!")
# elif username == "Сергей":
#     print("Привет, Сергей!")
# else:
#     print("Привет," ,username)

# i=0
# while i<5:
#     if i==5:
#         break
#     i=i+1
# else:
#     print("Вводить")
#     print("не нужно")
# print(i)
          
# n=int(input())
# flag=True
# i=2
# while flag:
#     if n%i==0:
#         flag=False
#         print(i)
#     elif i>n//2:
#         print(n)
#         flag=False
#     i+=1

# # вывод цифр в диапазоне
# n=range(90, 9,-2)
# for i in n:
#     print(i)

# a="food"
# for i in a:
#     print(i)

# line = ""
# for i in range (3):- цикл выполняется 3 раза
#     line=""
#     for J in range (2):
#          line+="8"
#     print (line)
# восьмерки 2 штуки 3 ряда

# text = "Благословение небожителей"

# print(len(text))
# размер строки (выдвет количество элементов), но он начинаетс 0, поэтому показывает 25



# print("небожителей" in text)
# проверяет есть ли слово неборжителей в строке (правда или ложь)

# print(text.lower())
# делает все в нижнем регистре (маленькие буквы)

# print(text.upper())
# делает все в верхнем регистре (большие буквы)

# print(text.replace("небожителей", "НЕБОЖИТЕЛЕЙ"))
#  меняет слово

# срезы - вывод определенного элемента из текста
# print(text[2])- вывел букву а, она 2
# print(text[len(text)-1]) -выводим нужный элемент , -1 так как все начинается с 0
# print(text[-1]) - то же самое
# print(text[:]) - выводит все
# print(text[:2]) - выводит первые 2
# print(text[15:16]) -выводит определенные элементы
# print(text[::7]) - выводит элементы только с шагом 7 или что напишешь\

# print(text[2:9]+text[-5]+text[:2]) - агословтБл

# n = 1+2+3
# print(n)

# n = 123

# Введите ваше решение ниже
# nStr = str(n)
# res = int(nStr[0]) + int(nStr[1]) + int(nStr[2])
# print(res)

n=int(input())
if n%6==0:
    p=int(n/6)
    k=int(4*n/6)
    s=int(p)
    print(p,' ', k, ' ', s)
else:
  print("Задача в целых числах не может быть решена")

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# n=int(input())
# nstr = str(n)
# v=len(nstr)
# if v%2==0:
#     m1=nstr[0:v//2]
#     m2=nstr[v//2:v]
#     sum1=0
#     sum2=0
#     for i in m1:
#         sum1=sum1+int(i)   
#     for i in m2:
#         sum2=sum2+int(i) 
#     if sum1==sum2:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("no")

# Определите, можно ли от шоколадки размером a × b 
# долек отломить c долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить
# шоколадку на два прямоугольника). 
# a=int(input("Введите длину шоколадки: "))
# b=int(input("Введите ширину шоколадки: "))
# c=int(input("Введите колиичество долек, которые хотите отломить одним разломом: "))

# if c<a*b and (c%a==0 or c%b==0):
#     print("yes")
# else:
#     print("no")

 

