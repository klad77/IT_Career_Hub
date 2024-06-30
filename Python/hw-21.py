# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в
# тексте и выводит на экран наиболее часто встречающиеся слова. Для решения задачи
# используйте класс Counter из модуля collections. Создайте функцию count_words, которая
# принимает текст в качестве аргумента и возвращает словарь с количеством вхождений
# каждого слова. Выведите наиболее часто встречающиеся слова и их количество.

# from collections import Counter
# def count_words(text):
#     t = text.lower().replace(",","").replace(".","").split()
#     return Counter(t).most_common(2)
# s = input("Введите текст: ")
# print(f'наиболее часто встречающиеся слова и их количество :', count_words(s), sep='\n')

# 2. Напишите программу, которая создает именованный кортеж Person для хранения
#    информации о человеке, включающий поля name, age и city.

# from collections import namedtuple
# Person = namedtuple("Person", ["name", "age", "city"])
# people = [
#     Person("Alice", 25, "New York"),
#     Person("Bob", 30, "London"),
#     Person("Carol", 35, "Paris")]
# for i in people:
#     name, age, city = i
#     print(f"Name: {name}, Age: {age}, City: {city}")

# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает
# значение для указанного ключа с использованием метода get или setdefault. Создайте
# функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и
# возвращает значение для указанного ключа, используя метод get или setdefault в
# зависимости от выбранного варианта. Выведите полученное значение на экран.

# def get_value_from_dict(dict,key,method):
#     if method:
#         return dict.get(key, 0)
#     return dict.setdefault(key, 0)
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# k = input("Введите ключ для поиска: ")
# m = True if input("Использовать метод get (y/n)? ").lower() == "y" else False
# print(f"Значение для ключа '{k}': {get_value_from_dict(my_dict, k, m)}")

