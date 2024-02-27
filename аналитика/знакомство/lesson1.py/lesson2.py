# n=int(input())
# m=int(input())
# print((m + n - 1)//n) - 1 для того чтобы сделать кратность 

# a=int(input())
# b=int(input())
# c=int(input())

# print(a//2)
# print((b+1)//2)
# print(c//2)

# # s=a//2
# # o=(b+1)//2
# # n=c//2
# # print(s+o+n)

# print((a//2)+((b+1)//2)+(c//2))

# a=int(input())
# a1=a//2
# if a%2==1:
#     a1=((a+1)//2)

# b=int(input())
# b1=b//2
# if b%2==1:
#     b1=((b+1)//2)

# c=int(input())
# c1=c//2
# if c%2==1:
#     c1=((c+1)//2)

# print(a1+b1+c1)

# i=int(input())
# j=int(input())
# if i-j==0:
#     print(-1)
# else:
#     print(i+j-1)

# a=int(input())
# if a%4==0 and a%100!=0 or a%400==0:
#     print("Yes")
# else:
#     print("No")

n=int(input())
if n%6==0:
    p=n/6
    k=4*n/6
    s=p
    print(p,' ', k, ' ', s)
else:
  print("Задача в целых числах не может быть решена")
  

