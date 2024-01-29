# #dict(dictionary) - словарь
# #key: value
# data = {"Ivan": 27, "Petr": 31, "Alina": 18,
#         "Egor": 23, "Anna": 45, "Vladimir": 60,
#         "Mariy":19}
# print(data.keys()) #возврат всех ключей
# print(data.values()) #возвращаются все значения
# print(data.items()) #возвращается коллекция данных, которая содержит кортеж
# #Кортеж состоит из двух значений (ключ, значение)
#Задача 25
# data = input("Введите символы через пробел: ").split()
# frequancy_dict = {}
# for elem in data:
#     if elem not in frequancy_dict:
#         print(elem, end= ' ')
#         frequancy_dict[elem] = 1
#     else:
#         print(f'{elem}_{frequancy_dict[elem]}', end=' ')
#         frequancy_dict[elem] += 1
#Очищение текста от лишних разделителей(плюс 27 задача)
# text = input("Input text: ").lower()
# separator = "!,.?@;:"
# for i in separator:
#     text = ''.join(text.split(i))
# print(len(set(text.split())))
#Задача 29
# chislo = int(input("Введите число: "))
# max = chislo
# while chislo != 0:
#     chislo = int(input("Введите число: "))
#     if chislo > max:
#         max = chislo
# print(f'Максимальное число: {max}')
#Пересечение двух множеств
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
# list_1 = var2.split()
# list_2 = var3.split()
# sp = list()
# for i in range(len(list_1)):
#     for j in range(len(list_2)):
#         if list_1[i] == list_2[j]:
#             sp.append(int(list_1[i]))
# sp.sort()
# print(*sp)
#Черника
arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
print(max(arr_count))
