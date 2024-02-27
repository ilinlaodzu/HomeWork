
from lesson12_2 import name_data, surname_data, phone_data,addres_data
def input_data():
    name=name_data()
    surname = surname_data()
    phone = phone_data()
    addres=addres_data()
    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 вариант:  \n"
    f"{name}\n{surname}\n{phone}\n{addres}\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{addres}\n"
    f"Выберите вариант: "))
    
    while var!=1 and var!=2:
        print("Неправильное число")
        var = int(input('Введите число '))
    if var==1:
        with open('data1.csv', 'a', encoding='utf-8') as f:
            f.write (f"{name}\n{surname}\n{phone}\n{addres} \n\n")
            print ()
    elif var==2:
        with open('data2.csv', 'a', encoding='utf-8') as f:
            f.write (f"{name};{surname};{phone};{addres}\n\n")

def print_data():
    pass

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data1.csv', 'r', encoding='utf-8') as f:
        data1=f.readlines()
        data1_list=[]
        j=0
        for i in range(len(data1)):
            if data1[i]=='\n' or i==len(data1)-1:
                data1_list.append(''.join(data1[j:i+1]))
                j=i
        print(''.join(data1_list))
     
    print('Вывожу данные из 2 файла: \n')
    with open('data2.csv', 'r', encoding='utf-8') as f: 
        data2=f.readlines()
        print(data2)     

print_data   
