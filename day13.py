# import DelIT

# print(DelIT.name)
# DelIT.my_fun()
# obj = DelIT.MyObject(10)
# print(obj.num)


# -----------------------------------
# from DelIT import my_fun, num
# my_fun()
# print(name)


# --------------------------------

# from DelIT import MyObject as MClass
# ob = MClass()
# print(ob.name)


# ----------------------------
# Abstraction
# (1)--> Abstract Class (Partial)
# (2)--> INterface (Full)


# Abstraction -> Data Hidding + Show necessary info to user
# Telegram App -> Hidden + UI


# Parent Class --> DownloadFIle(), SendingMsg() --> no logic
# Child Own Class -> stickers, themes, [DownloadFIle(), SendingMsg()]


# Parent Class -> Abstract class
# Abstract Class -> 1. Defined method (with body), 2.static metjod
                 # -> 3. method without body (abstract method)
                   # -> 4. cant create object of abstract class
                   # 5.-> init()


# from abc import ABC,abstractmethod
#
#
# class AbstractClass(ABC):
# 	name = "saif"
# 	@abstractmethod
# 	def abstract_method(self):
# 		pass
# 	@clasmethod
# 	def defied_method():
# 		print("this is methos with body")
#
# 	@staticmethod
# 	def static_method():
# 		print("static method")
#
# 	def _init_(self):
# 		print("This is init method")
#
# 	def body(self):
# 		print("instance method")
#
#
#
# class ImplementedClass(AbstractClass):
# 	def _init_(self):
# 		super()._init_()
# 		print("This is init inside implemented method")
# 	def abstract_method(self):
# 		print("providing body to abstract method")
#
#
#
# obj = ImplementedClass()
# obj.abstract_method()
# AbstractClass.defied_method()
# AbstractClass.static_method()
# obj.body()


# Multi Threading

# Process -> Eclipse
# Thread  -> PROCESS -> typing, error, gra.
# Thread -> ATOMIC, LIGHT WEIGHT
# Atomic -> single task
# Light Weight -> Memory

# PROCESS -> THREAD1, 2,3,4,5...
# Thread -> Resource sharing

# Multi Threading -> ideal time
#  10 persons -> RESTING TIME -> TASK

# OOP ->  Object
# MultiThreading -> Object(THREAD)

# 3 ways
# 1. without class -> functional approch
# 2.  with inheritance
# 3. with simple class


# from threading import Thread
#
# class UserDefinedThreadClass:
#     def work_load(self):
#         for count in range(5):
#             print("USER THERAD")
#
# obj = UserDefinedThreadClass()
# thread1 = Thread(target= obj.work_load)
# thread1.start()
#
# def work_load_other():
#     for count in range(5):
#         print("MAIN THREAD")
#
# work_load_other()
#
#
# from threading import Thread
#
# class UserDefinedThreadClass(Thread):
#     def __init__(self, thread_name):
#         super().__init__()
#         self.thread_name = thread_name
#
#     def run(self):
#         for count in range(5):
#             print(self.thread_name)
#
# thread1 = UserDefinedThreadClass("th1")
# thread2 = UserDefinedThreadClass("th2")
# thread3 = UserDefinedThreadClass("th3")
#
# thread1.start()
# thread2.start()
# thread2.join()
# thread3.start()
#
#
# # 1. without class -> functional approch
# from threading import Thread
#
# def work_load():
#     for count in range(5):
#        print("one")
#
# th1 = Thread(target=work_load)
# # work_load()
# th1.start()
#
# for count in range(5):
#     print("two")
#
#
# # 2.  with inheritance
# # Thread -> Start() -> run()
# # run() -> Override it
# # Life Cycle of Thread
# from threading import Thread
#
# class UserDefinedThreadClass(Thread):
#     def run(self):
#         for count in range(5):
#             print("one")
#
# thread1 = UserDefinedThreadClass()
# thread1.start()




# def main_func(func1):
#     def second_func():
#         print('first statement')
#         func1()
#         print('second statement')
#     return second_func()
#
#
# @main_func
# def main_func_2(func1):
#     def second_func():
#         print('third statement')
#         func1()
#         print('fourth statement')
#     return second_func()
#
#
# @main_func_2
# def template():
#     print('templated value')
#
#
# print(template())
