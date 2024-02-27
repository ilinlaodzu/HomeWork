# программа для ввода данных, вывода данных, использование функций и нелинейная
from lesson12_1 import input_data, print_data
from lesson12_4 import add_entry, update_entry, delete_entry,find_entry
def interface():
    print("Добрый день. Это справочник \n 1 - записать данные \n 2 - выводить данные")
    command=int(input('Введите число '))
    while command!=1 and command!=2:
        print("Неправильное число")
        command = int(input('Введите число '))
    if command ==1:
        input_data()
    elif command ==2:
        print_data()

def main():
    while True:
        choice = input("Выберите действие (add,update,delete,find,quit): ").lower()
        if choice == "quit":
            break
        elif choice == "add":
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone = input("Введите номер телефона: ")
            addres =input("Введите адрес: ")
            add_entry(name,surname, phone,addres)
        elif choice == "update":
            name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
            surname = input("Введите фамилию: ")
            phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
            addres =input("Введите новый адрес (оставьте пустым, чтобы не менять): ")
            update_entry(name,surname, phone,addres)
        elif choice == "delete":
            surname = input("Введите фамилию для удаления: ")
            delete_entry(surname)
        elif choice == "find":
            surname = input("Введите фамилию для поиска: ")
            entry = find_entry(surname)
            if entry:
                print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Номер телефона: {entry[2]}, Адрес: {entry[3]}")
            else:
                print("Запись не найдена.")
        else:
            print("Неизвестное действие.")