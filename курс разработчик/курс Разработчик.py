

# Ввод массива с клавиатуры
input_array = input("Введите строки через запятую: ").split(",")
def filter_short_strings(input_array):
    # Создаем массив для хранения строк длиной <= 3 символа
    result_array = []
    # Проходим по всем строкам в входном массиве
    for string in input_array:
        # Если длина строки <= 3 символа, добавляем ее в result_array
        if len(string) <= 3:
            result_array.append(string)
    return result_array
# Получаем отфильтрованный массив
result_array = filter_short_strings(input_array)
# Выводим результат
print("Исходный массив:", input_array)
print("Отфильтрованный массив:", result_array)