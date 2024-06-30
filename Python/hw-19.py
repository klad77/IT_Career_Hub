# 1. Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.

# l = ['cat', 'dog', 'tac', 'god', 'act']
# def anagrams(l):
#     groups = []
#     for word in l:
#         for group in groups:
#             if set(word) == set(group[0]):
#                 group.append(word)
#                 break
#         else:
#             groups.append([word])
#     return  [list(group) for group in groups if len(group) > 1]
# print(*anagrams(l), sep=', ')

# 2. Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
#    является ли set1 подмножеством set2.

# def is_subset(s1,s2):
#     p = True
#     for i in s1:
#         if i not in s2:
#             p = False
#     return p
# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5}
# print(is_subset(s1, s2))