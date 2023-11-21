#
# # Types of method
# # inctance method ---> Object
# # static method  ---> Class
# # class method  ---> Class
#
# class MyMethod:
#     count = 100
#
#     def instance_method(self):
#         print("this is a intance method")
#
#     @staticmethod
#     def static_method():
#         print("this is static method")
#
#     @classmethod
#     def class_method(cls):
#         print("this is a class method")
#
#
# obj = MyMethod()
# obj.instance_method()
# MyMethod.static_method()
# MyMethod.class_method()
# print(obj.count)
#
#
# # Constructor
# # init of object
# # no return type
# # auto called whenever object is created
#
# class MyConstructor:
#     def __init__(self):
#         print("this is default constructor")
#
#
# obj = MyConstructor()
# obj1 = MyConstructor()
#
#
# class Mobile:
#     def __init__(self, cam, r):
#         camera = cam
#         ram = r
#         print(camera, ram)
#
#
# m1 = Mobile(50, 0)
# m2 = Mobile(100, 0)
#
#
# # Questions
# class Mobile:
#     def __init__(self, cam, r):
#         print("init1")
#
#     def __init__(self, cam, r):
#         print("init2")
#
#
# m1 = Mobile(50, 0)
#
#
# class Mobile:
#     def __init__(self, cam, r):
#         print("init1")
#
#     def _init_(self, cam, r):
#         print("init2")
#
#     def _init_(self, cam, r):
#         print("init3")
#
#
# m1 = Mobile(50, 0)
# m1._init_(40, 0)
#
#
# # Access Specifier
# # public Specifier ====> Visibility in Packages
# # Private Specifier ===> Visibility inside the class
# # Protected Specifier ===> inside the class and outside the class
#
#
# class MyClass:
#     num = 1000
#     __num = 1200
#     _num = 1400
#
#
# obj = MyClass()
#
#
# # print(obj.num) ---> can be access due to public
# # print(obj._num) ---> can be access due to protected
# # print(obj.__num) ---> can not be access due to private instance variable
#
#
# class MyClass:
#
#     def _protected_method(self):
#         print("protected method call")
#
#     def __private_method(self):
#         print("private method is call")
#
#     def public_mehtod(self):
#         print("public method is called")
#
#
# obj = MyClass()
# obj.public_mehtod()
# obj._protected_method()
#
#
# # obj.__private_method() --> can not be call due to private method
