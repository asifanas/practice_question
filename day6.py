# # functional --> data type, data strct, function
# # OOP --> class, object, acess specifier, constructor
#
# # c--> Functional
# # C#, java, --> OOP
# # Python, JS--> Functional, OOP
#
# # Modularity, secuirity, states, reusablity
#
#
# # object
# # class --> user define data type
#
# class My_Components:
#     keyboard = 1
#     display = 2
#
#
# laptop1 = My_Components()
# print(laptop1)
#
#
# class My_Components:
#     keyboard = 1
#     display = 2
#
#
# l3 = My_Components()
# l3.display = 3
# print(l3.display)
# print(laptop1.display)
#
# # object refrence by lap3 and lap1
# lap1 = l3
# print(lap1.display)
#
#
# class My_Components:
#     def os(self):
#         print("this is os method")
#
#
# lap1 = My_Components()
# lap1.os()
#
#
# class MyClass:
#     count = 10
#
#     def access(self):
#         print(self.count)
#
#     def change(self):
#         self.count = 99
#
#     def local_variable(self):
#         count = 50
#         print(count)
#
#
# m1 = MyClass()
# m1.local_variable()
#
#
# # inside self object is pass
# # self is holding current calling object
# # self is not keyword
#
#
# class MyClass:
#     count = 99
#
#     def my_method(self):
#         print("THis is actual self")
#
#     def change(self):
#         self.count = 10
#
#
# m1 = MyClass()
# m1.my_method()
# print(m1.count)
# # same
# MyClass.my_method(m1)  # this is same as line 78
# m2 = MyClass()
# m2.change()
# print(m2.count)
#
#
# # -->
# # static variable and method in python
# # by inclass variable are static
#
#
# class MyClassData:
#     count = 10
#
#
# m1 = MyClassData()
# print(m1.count)
# MyClassData.count = 30
# m2 = MyClassData()
# print(m2.count)
#
# # Question  asked by sir
#
# li = [1, 2, 3]
# li1 = [4, 5, 6]
#
#
# class MyAdd:
#
#     def method1(self, li1, li2):
#         for n1, n2 in zip(li1, li2):
#             print(n1 + n2)
#
#
# m1 = MyAdd()
# m1.method1(li, li1)
