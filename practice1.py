# custom Exception

# part1
# marks = int(input("enter the marks : "))
#
# if marks < 80:
#     print("Go furthure")
#     print("need practice")
# else:
#     print("Go for next module")
#
#
# # part2
# marks = int(input("enter the marks : "))
#
# if marks<80:
#     raise Exception("Need practice")
#     print("Go furthure")
#     # print("need practice")
#
#
# else:
#     print("Go for next module")
#

# part 3

# class MarksNotEligableException(Exception):
#     def __init__(self, error_msg):
#         print(error_msg)
#
# marks = int(input("enter the marks : "))
#
# if marks < 80:
#     raise MarksNotEligableException("Need practice")
#     print("Go furthure")
#     # print("need practice")
# else:
#     print("Go furthur")
#
#
# # part4
#
# class MarksNotEligableException(Exception):
#     def __init__(self, error_msg):
#         super().__init__(error_msg) # to call base class
#
# marks = int(input("enter the marks : "))
#
# if marks < 80:
#     raise MarksNotEligableException("Need practice")
#     print("Go furthure")
#     # print("need practice")
# else:
#     print("Go furthur")

# with open("mydata.txt", "w") as f1 , open("mydata.txt", "r") as f2:
#     f1.write("Asif")
#
# f1 = open("mydata.txt", "r")
# print(f1.read())


# class MyMethod:
#     count = 100
#
#     def instance_method(self):
#         print("this is a intance method")
#
#     @staticmethod
#     def static_method():
#         count = 100
#         print("this is static method")
#
#     @classmethod
#     def class_method(cls):
#         print("this is a class method")
#
#
# obj = MyMethod()
# obj1 = MyMethod()
# MyMethod.static_method()
# MyMethod.class_method()
# print(obj.count)
# print(obj1.count)


# class Mobile:
#
#     def __init__(self, cam = None, ram = None):
#         print("init3")
#
#     def __str__(self):
#         return "asif"+"Anas"
#
# m1 = Mobile()
# print(m1.__str__())


# practice on inheritence

# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#
# obj = B()
# obj1 = A()
# __init__(obj1)


# l = ["hallo", 10, 20, 30, 30, 40]
#
# di = dict()
#
# for i in l:
#     if i in di:
#         di[i] +=1
#     else:
#         di[i] = 1
#
# for i in di:
#     if di[i] == 1:
#         print(i)


# li = ["hallo", 10, 20, 30, 40, 40]
# li1 = []
# for i in li:
#     if li.count(i)>1:
#         pass
#     else:
#         li1.append(i)
#
# print(li1)
#


import sys


# li = [1, 2, 23, 2]
# if 10 in li:
#     print("element is present")
# else:
#     print("Not present")

# li = [12, 2, 23]
# print(li.index(12))
#
# del li
# print(li)

# li = [1, 2, 3, 23, 32]
#
# for i in range(0, len(li)):
#     li[i] = li[i]+2
# print(li)

# import copy
#
#
# li = [[12, 23, 23], [344, 123]]
# li1 = copy.deepcopy(li)
#
# li1[0][1] = 23123
#
# print(li1)
# print(li)














