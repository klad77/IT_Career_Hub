# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в
#    качестве аргументов и возвращает новый словарь, объединяющий все входные словари.

# def merge_dicts(*c):
#     k = {}
#     for i in c:
#         for key, value in i.items():
#             if key in k:
#                 k[key].append(value)
#             else:
#                 k[key]=[value]
#     return k
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'c': 5, 'd': 6}
# print(merge_dicts(dict1, dict2, dict3))

# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает
#    количество уникальных символов в этой строке.

# def count_unique_chars(x):
#     unique_chars = set(x)
#     return len(unique_chars)
# s = (input("Введите строку: "))
# print(f'Количество уникальных символов :', count_unique_chars(s))

# 3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.

# grades = {
# 'Alice': [85, 90, 92],
# 'Bob': [78, 80, 84],
# 'Carol': [92, 88, 95]
# }
#
# def calculate_average_grade(x):
#     return {name: sum(value)/len(value) for name, value in grades.items()}
# print(calculate_average_grade(grades))
