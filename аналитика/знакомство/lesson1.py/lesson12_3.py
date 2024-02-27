# from lesson12_4 import add_entry, update_entry, delete_entry,find_entry
# def main():
#     while True:
#         choice = input("Выберите действие (add,update,delete,find,quit): ").lower()
#         if choice == "quit":
#             break
#         elif choice == "add":
#             surname = input("Введите фамилию: ")
#             name = input("Введите имя: ")
#             phone = input("Введите номер телефона: ")
#             addres =input("Введите адрес: ")
#             add_entry(surname, name, phone,addres)
#         elif choice == "update":
#             surname = input("Введите фамилию: ")
#             name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
#             phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
#             addres =input("Введите новый адрес (оставьте пустым, чтобы не менять): ")
#             update_entry(surname, name, phone,addres)
#         elif choice == "delete":
#             surname = input("Введите фамилию для удаления: ")
#             delete_entry(surname)
#         elif choice == "find":
#             surname = input("Введите фамилию для поиска: ")
#             entry = find_entry(surname)
#             if entry:
#                 print(f"Имя: {entry[0]}, Номер телефона: {entry[1]}")
#             else:
#                 print("Запись не найдена.")
#         else:
#             print("Неизвестное действие.")