# list = [1, 2, 3]
# print(list[1])
# list[0] = 0
# print(list)

#TUPLE
# tuple1 = (1, 2, 3, 4) # неизменяемый список
# print(tuple1)
# print(tuple1[2])
# list1 = list(tuple1) # меняем тип данных с tuple на список
# list1[0] = 0  # меняем первые элемент
# tuple1 = tuple(list1) # переводим опять в тип данных tuple
# print(len(tuple1))

# a = ("cherry", "banana", "apple", "orange", "strawberry")
# print(a[1:4])
# for i in range(1, len(a) - 1):
#     print(a[i], end=" ")
# a = (1, 2, 3, 3, 3, 3, "hi")
# b = ('a', 'b', 'c')
# c = a + b
# print(c*2)
#
# print(a.count(3)) # кол элементов
# print(a.index('hi')) #возвращает индекс элемента
# list1 = [1, 2, 33]
# list2 = ['m', 'h']
# print(list1+list2)

# SETS !неупорядоченные ! сортируют (цифры) ! не хронит дубликаты
# set1 = {1, 1, 1, 1, 1}
# print(len(set1))
#
# list1 = [1, 1, 2, 3, "Hi", "a", 'b', 66]
# set1 = set(list1)
# print(set1)

# создайте свой лист и проверьте есть ли дубликаты
#если они есть вывести "YES", иначе "NO"

# list1 = [1, 2, 3, 4, 5]
# set1 = set(list1) # set1 = (1, 2, 3, 4, 5)
# if len(list1) == len(set1):
#     print("NO")
# else:
#     print("YES")

# методы
# set1 = {1, 2, 3, 10, "Hi", "J"}
# set1.add("Hello") # добавить элемент НЕ С КОНЦА
# b = {1, 56, 57}
# set1.update(b) # суммирование двух set
# set1.remove("J") # удаление по элементам
# set1.discard("Hi")
# set1.pop() # удаление рандомного эл
# b.clear() # удаление полностью
# print(set1, b)
# for i in set1:
#     print(i, end=" ")

#DICTIONARY
# key - int, str
# value - любые типы данные
# dict1 = {
#     "Almaty": [1, 2, 3],
#     "Astana": 7272,
#     "Kokshetau": 7163
# }
# print(dict1['Kokshetau'])

# person={}
# inform = input() # имя возраст рост город 5, 3, 4, 2, 5, 4
# s = inform.split() # s = ["name", age, height, city, [5, 3, 4, 2, 5, 4]]
# person['name'] = s[0]
# person['age'] = s[1]
# person['height'] = s[2]
# person['city'] = s[3]
# person['marks'] = []
# for i in s[4:]:
#     person['marks'].append(int(i))
# print(person.keys())

students = [
    {
        'name': 'Ruslan',
        'age': 20,
        'gpa': 3.3
    },
    {
        'name': "Ailana",
        'age': 18,
        'gpa': 2.7
    },
    {
        'name': 'Derbes',
        'age': 21,
        'gpa': 3.6
    }
]
sum = 0
res = 0
for i in students:
    # if i['name'][0] == "A":
    #     print(i['name'])
    # if i['gpa'] > 3:
    #     print(i['name'])
    sum += i['gpa']
    res = sum / len(students)
print(res)









