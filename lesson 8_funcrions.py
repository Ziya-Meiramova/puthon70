# print(1)
# a = [1, 2, 3]
# print(len(a))

# def my_func(a, b, c):
#     print(a, b, c + 1)
#
# # my_func()
# name = input("Enter your name: ")
# surname = input()
# age = int(input())
# my_func(name, surname, age)

# def func(*a): # *a = когда кол аргументов неизвестно
#     print("Самый младший ребенок ", a[-1])
#
# func("Akbota", "Derbes", "Anel", "AAA", "BBB")

# def country(a = "Kazakhstan"):
#     print('I am from: ', a)
# country("Sweden")
# country()

# a = ['banana', 'orange', 'apple']
# def BBB(w):
#     for i in range(len(w)):
#         if w[i][0] == "b":
#             print(w[i])
# BBB(a)

# return
# a = 5
# arr = []
# def multi(a):
#     return a*2
# arr.append(multi(a))
# print(arr)

# list1 = [1, 2, 3, 4]
# list2 = [-5, 3, 2, 100]
# def min_a(a):
#     mx = -123456
#     for i in a:
#         if i > mx:
#             mx = i
#     return mx
# print(min_a(list1) * 10)
# print(min_a(list2) / 10)

# def pow1(a, b):
#     return a**b
# print(pow1(2, 10))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# def find_min(a, b, c, d):
#     list1 = []
#     mn = 1111111
#     list1.append(a)
#     list1.append(b) # 3 4 -9 0
#     list1.append(c)
#     list1.append(d)
#     for i in list1:
#         if i < mn:
#             mn = i
#     return mn
# print(find_min(a, b, c,d))


# x = int(input())
# y = int(input())
# def mn(a, b):
#     if a == 1 and b == 0 or a == 0 and b == 1:
#         return 1
#     else: return 0 # 0 1 или 1 0
# print(mn(x, y))

# ana nan tabat
word = input()
def is_polindrom(a):
    for i in range(len(a)):
        if a[i] == a[-1 - i]:
            print("YES")



