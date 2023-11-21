# inheritance

# variable , special method , methods
# simple, multilev, multiple, hybrid, hir

# java, C#-> do not have(multiple , hubrid
# c++ -> Error


# Multilevel inheritence
# class GParent():
#     def gp_method(self):
#         print("Gparent Method")
#
#
# class Parent(GParent):
#     def gp_method(self):
#         print("Parent Method")
#
#
# class Child(Parent):
#     pass
#
# ch = Child()
# # ch.p_method()
# ch.gp_method()


# class parent:
#     def __init__(self):
#         print("parent")
#
#
# class Child(parent):
#     def __init__(self):
#         super().__init__()  # whenever we inherit its should be write for ignorance of warning
#
#         print("Child")
#
#
# ch = Child()  # parent



# class Parent:
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#         print("Parent")
#
#
# class Child(Parent):
#     def __init__(self, f_name):
#         self.f_name = f_name
#         super().__init__("asif", "anas")
#         print("Child")
#         print(self.f_name, self.l_name)
#         print(super().self.f_name)
#
#
# ch = Child("Asif")




