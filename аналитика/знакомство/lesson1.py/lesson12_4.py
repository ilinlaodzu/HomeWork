
from lesson12_2 import name_data, surname_data, phone_data,addres_data
def add_entry(name, surname, phone, addres):
    # name=name_data()
    # surname = surname_data()
    # phone = phone_data()
    # addres=addres_data()
    f"{name};{surname};{phone};{addres}\n"
    with open('data2.csv', 'a', encoding='utf-8') as f:
        f.write (f"{name};{surname};{phone};{addres}\n\n")

def update_entry(name, surname, phone, addres):
    rows=[]
    with open('data2.csv', 'r', encoding='utf-8') as f:
        rows=f.readlines()
        j=0
        for i in range(len(rows)):
            # print(data2[i])
            data2_list = rows[i].split(';')
            if len(data2_list) ==1 and data2_list[0] == '\n':
                continue
            elif data2_list[1]==surname:
                new_name=data2_list[0]
                if name != "":
                    new_name = name
                new_phone=data2_list[2]
                if phone != "":
                    new_phone = phone
                new_addres=data2_list[3]
                if addres != "":
                    new_addres = addres
                rows[i]=new_name + ';' + surname + ';' + new_phone + ';' + new_addres
    with open('data2.csv', 'w', encoding='utf-8') as f:
        f.writelines(rows)

def delete_entry(surname):
    new_rows=[]
    with open('data2.csv', 'r', encoding='utf-8') as f:
        rows=f.readlines()
        j=0
        for i in range(len(rows)):
            # print(data2[i])
            data2_list = rows[i].split(';')
            if len(data2_list) ==1 and data2_list[0] == '\n':
                continue
            elif data2_list[1]!=surname:
               new_rows.append(rows[i])
    print(new_rows)
    with open('data2.csv', 'w', encoding='utf-8') as f:
        f.writelines(new_rows)

def find_entry(surname):
    # print(surname)
    with open('data2.csv', 'r', encoding='utf-8') as f:
        data2=f.readlines()
        data2_list=[]
        j=0
        for i in range(len(data2)):
            # print(data2[i])
            data2_list = data2[i].split(';')
            if len(data2_list) ==1 and data2_list[0] == '\n':
                continue
            elif data2_list[0]==surname:
                # print(data2_list[1])
                return data2_list


    
            
      
          


