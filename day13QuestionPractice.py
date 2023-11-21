


# class Abstract1(ABC):
#
#     @abstractmethod
#     def abstract_method1(self):
#         pass
#
#
# class Abstract2(ABC):
#     @abstractmethod
#     def abstract_method2(self):
#         pass
#
#
# class implement(Abstract1, Abstract2):
#     def __init__(self):
#         print("inside a implementation class")
#
#     def abstract_method1(self):
#         print("abstract method 1")
#
#     def abstract_method2(self):
#         print("abstract method 2")
#
#
# imp = implement()
# imp.abstract_method1()
# imp.abstract_method2()
# from abc import ABC, abstractmethod
#
# class Abstract1(ABC):
#
#     @abstractmethod
#     def abstract_method1(self):
#         print("hallo world")
#
#
#
# class implementation(Abstract1):
#     def __init__(self):
#         print("inside the implementation")
#
#
# imp = implementation()
# imp.abstract_method1()


#
# class Abstract1:
#
#     def abstract_method1(self):
#         print("this is abstract 1")
#
#
# class Abstract2:
#     def abstract_method1(self):
#         print("this is abstract 2")
#
#
# class implementation(Abstract1, Abstract2):
#     def __init__(self):
#         print("inside the implementation")
#
# imp = implementation()
# imp.abstract_method1()

# class parent:
#     def __init__(self):
#         print("parent")
#
# class child(parent):
#     def __init(self):
#         print("child")
#
# child = parent
# m1 = child()