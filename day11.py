# PolyMorphism
# 4 Types
# Method Overloading
# Method Overriding
# Operator Overloading
# Duck Typing

# Method Overloading -> 1 class(min 2 methods) -> Methods with(same name, diff signature)
#                    -> signature(parameters -> Count)
# Not Possible in Python
class Calc:
    def add(self):
        print("One")

    def add(self, num):
        print("Two")

obj = Calc()
obj.add()


# Method Overriding -> 2 classes each having at least one method(same name + same signature)
#                   -> inheritance relationship
# Runtime Poly, dynamic Binding
# 1950s
class Mechanic:
    def gear_box(self):
        print("4 gears")


# 2022s
class MechanicPro(Mechanic):
    def gear_box(self):
        print("6 gears")


# QUESTION
class Parent:
    def my_method(self, number):
        print("Parent")


class Child(Parent):
    def my_method(self):
        print("Child")


obj = Child()
obj.my_method(100)


# Operator Overloading
# print("Hi" + "Hello") -> Concate
# print(10 + 20) -> addition
# Magic Method -> + -> __add__()
class Numbers:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __gt__(self, other):
        return self.num > other.num

num1 = Numbers(10.3)
num2 = Numbers(17)

print(num1.num + num2.num)
print(num1 + num2)
print(num1 * num2)
print(num1 > num2)


# Duck Typing
class Trainer:
    def think(self):
        print("think")


class Student:
    def learning(self):
        print("learning")

tr1 = Trainer()
st1 = Student()


def access(obj_passed):
    obj_passed.think()
    obj_passed.learning()

access(tr1)


# Exception -> Error ->
# Ex1
# Ex2
# 1. print message
print("Start")
num1 = float(input("enter num1 -"))
num2 = int(input("enter num2 -"))
# Ex3
# e = ZeroDivisionError()
# 2. print type of problem
print("Start")
try:
    print(10 / 0)

except ZeroDivisionError as e:
    print(e)
print("End")
# Ex4
# 3. provide solution
print("Start")
num1 = float(input("enter num1 -"))
num2 = int(input("enter num2 -"))
try:
    print(num1 / num2)

except ZeroDivisionError as e:
    print("Please dont use 0 for div")
    num2 = 1
    print(num1 / num2)

print("End")


# try -> multi except
# Ex5
print("Start")
try:
    li1 = [10, 20, 30]
    print(li1[7])

except IndexError as e:
    print(e)

except Exception as e:
    print(e)

print("End")


# Ex6
print("Start")
try:
    li1 = [10, 20, 30]
    print(li1[7] / 0)

except ZeroDivisionError as e:
    print("Block1")

except Exception as e:
    print("Block2")


print("End")

# EX7 ----> Termination
print("Start")
try:
    li1 = [10, 20, 30]
    print(li1[7] / 0)

except ZeroDivisionError as e:
    print("Block1")

print("End")


# EX8
# Only go for Specific to Genric  classes
print("Start")
try:
    li1 = [10, 20]
    print(li1[5])

except Exception as e:
    print("Block2")

except ZeroDivisionError as e:
    print("Block1")

print("End")


# Nested Exception
# try -> (try -> except) -> except
# EX9
print("Start")
try:
    print(10 / 0)
    try:
        print(50 / 0)
    except ZeroDivisionError as e:
        print("Inner Block")

except Exception as e:
    print("Outer Block")

print("End")


# EX10
print("Start")
try:
    try:
        li1 = [10, 20]
        print(li1[4])

    except ZeroDivisionError as e:
        print("Inner Block")

    print(10 / 0)

except IndexError as e:
    print("Outer Block")

print("End")


# EX11
print("Start")
try:
    try:
        print(50 / 0)
    except ZeroDivisionError as e:
        print("Inner Block")
        print(10 / 0)

except Exception as e:
    print("Outer Block")

print("End")
