# different type of compiler
# pycharm , spyder , programiz , jupiter, notebook


# Yes , we can run same python .class file on different operating system because python is platform independent language
# as long as bytecode and virtual machine is same on different operating system.


# Why tuple is faster than list


# what are the benefits of object oriented programming


# generator in python


# Decorator in python

# Function
# step1 -> function name(function body)
# step2 -> inner function comp. -> return
# step 3 -> return total inner function

# def my_deco(func_passed):
#     def inner_func():
#         print("hello decorator")
#         return func_passed(10)
#     return inner_func
#
#
# @my_deco
# def oldi(num):
#     print("hi oldi")
#     return num
#
# print(oldi())

# function, method, class



# can we create object inside the class

# getter setter method
# class Student:
#     def __init__(self):
#         self.__marks = 0
#
#     @property
#     def marks(self):
#         return self.__marks
#
#     @marks.setter
#     def marks(self, marks):
#         if marks > 40:
#             self.__marks = marks
#
#
# s1 = Student()
# print(s1.marks)
#
# s1.marks = 33
# print(s1.marks)
#
# s2 = Student()
# print(s2.marks)


# Encapsulation => Class (members + security (Access speci))


# can we create class inside a class


# class Student:
#
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#
#     def show(self):
#         print(self.name, self.rollno)
#
#     class Laptop:
#         def __init__(self):
#             self.brand = "hp"
#
#
# s1 = Student.Laptop()
# print(s1.show())




