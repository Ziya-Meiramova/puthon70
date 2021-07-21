# class Students:
#     name = "Ziya"
#     age = 24
#     gpa = 3.6
#
# ziya = Students()
# a = Students()
# print(ziya.age)
# print(a.name)

# class Students:
#     def __init__(a, name, age, gpa):  #конструктор для объектов
#         a.name = name
#         a.age = age
#         a.gpa = gpa
#     def say_hi(self): # метод любого студ
#         print("Hello", self.name)
#     def year(self): # self == r
#         print("В след году этому студенту будет: ",self.age + 1 )
#
# derbes = Students("Derbes", 22, 2.8)
# r = Students("Arai", 18, 4.0)
# derbes.year()
# r.year()
# r.say_hi()
# derbes.say_hi()
# print(derbes.name, derbes.age, derbes.gpa)


# class Animals:
#     def __init__(self, type, age, name):
#         self.type = type
#         self.age = age
#         self.name = name
#     def run(self):
#         return self.name + " бегает"
#     def eat(self):
#         return self.name + " кушает"
#
# animal1 = Animals("lion", 10, "Alex")
# animal2 = Animals('pig', 2, "Gloria")
# print(animal2.eat())
# print(animal1.run(), animal1.eat())

# class Employees:
#     cnt = 0
#     def __init__(self, surname, name, age, salary, is_good):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.is_good = is_good
#         Employees.cnt += 1
#     def empp(self):
#         return "В этой компании работают ", Employees.cnt, " сотрудников"
#     def sal(self):
#         return "Этот сотрудник зарабатывает: ", self.salary
# emp1 = Employees("Utebaliyev", "Arnur", 25, 200000, True)
# emp2 = Employees("Syzdykova", "Anara", 45, 150000, False)
# print(emp1.empp())
# print(emp2.is_good)
# print(emp1.sal(), emp2.sal())


# class Rectangle:
#     def __init__(self, color, sideA, sideB):
#         self.color = color
#         self.sideA = sideA
#         self.sideB = sideB
#     def per(self):
#         return (self.sideA + self.sideB) * 2
#     def sq(self):
#         return self.sideB * self.sideA
#
# rect1 = Rectangle("red", 3, 6)
# rect2 = Rectangle("blue", 8, 5)
# rect3 = Rectangle("green", 12, 3)
#
# print(rect1.sq(), rect2.sq(), rect3.sq())


banana = 6
apple = 4
orange = 8
text = "У меня в корзине есть {}  бананов, {} яблок, {} апельсинов"
print(text.format(banana, apple, orange))

print("У меня в корзине", banana, "бананов", apple, "яблок")