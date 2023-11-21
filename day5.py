# List Comprehension
# num1 = [1, 2, 3]
# num2 = [2, 32, 6]
# zip has no sense with different length of the list
# zip function can use to trace multiple list by using for loop
# for n1, n2 in zip(num1,num2):
#     print(n1+n2)


# li = [n1 + n2 for n1, n2 in zip(num1, num2)]
# print(li)

# Loop nesting one another
# super_list = [[1, 2, 3], [10, 20, 40]]
#
# for row in super_list:
#     for col in row:
#         print(col)


# print values in same line
# li = [1, 2, 3]
# for e in li:
#     print(e , end="")


# Function
# def print(*var):

# return show (parameter)
# {
#     body
# }
# show(arguments)

# def show(num1,num2):
#     print(num1+num2)
#
#
# show(10, 20)

# def show2(n1, n2):
#     print(n1, n2)
#
#
# show2(n2=10, n1=20)

# def shows4(n1, n2=10):
#     print(n1+n2)
#
#
# shows4(100)

# def shows5(*num):
#     print(num)
#
#
# shows5(10, 20, 30)
#
#
# def outer_F():
#     print("outer fact")
#     out = 100
#     out = out*out
#     def inner_f():
#         print("inner funct")
#     inner_f()
#     print(out)
#
#
# outer_F()
#
# function -> outside classes . func_name
# method -> inside classes. something method_name
#
# func vs oop question asked by manav



# class remote:
#
#     def __init__(self):
#         self.name = 'asif'
#         self.lg = self.battery()
#
#
#
#     def show(self):
#         print(self.name)
#
#     class battery:
#
#         def __init__(self):
#             self.b_name = 'nippo'
#
#         def display(self):
#             print(self.b_name)
#
# b = remote()
# p = b.lg
# b.show()
# p.display()
















