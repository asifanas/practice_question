# # f1 = open("mydata.txt", "r")
# # # print(f1)
# # #
# # # for data in f1:
# # #     print(data)
# # #
# # # # or
# #
# # print(f1.read(49))
#
#
# # f1 = open("mydata.txt", "r")
#
# # try:
# #     print(f1.read())
# #     print(10 / 0)
# #
# # except ZeroDivisionError as a:
# #     print("Exception caugth")
# #
# # finally:
# #     print("finally file close")
# #     f1.close()
#
# # print(f1.tell())
# # print(f1.readline())
# # print(f1.readline())
# # print(f1.readline())
# # print(f1.readline())
# # print(f1.readline())
# # print(f1.readline())
# # print(f1.seek(6))
# # print(f1.seek(0))
# # print(f1.readline())
#
# import pickle
#
# # li = ["Asif\n", "Anas\n"]
# #
# # f1 = open("mydata.dat", "wb")
# #
# # pickle.dump(li, f1)
#
# f1 = open("mydata.dat", "rb")
# pickle.load(f1)rfr




# from abc import ABC , abstractmetho
# class Abstract(ABC):
#
#         def __init__(self):
#             print("i am in the abstract class")
#
#         @abstractmethod
#         def abse(self):
#             pass
#
# class alpha(Abstract):
#
#     def abse(self):
#         print("YEs overloaded")
#
# a = alpha()
# a.abse()


# li = [1, 2, [1, 3], 4]
#
# for i in range(0, len(li)):
#     if i==2:
#         for j in li[i]:
#             print(j)



# def fact(num):
#
#     if num == 0:
#         return 1
#     return num*fact(num-1)
#
# result = fact(5)
# print(result)
#
#
# li = [3, 1, 4, 10, 12]
#
# def partition(li, s, e):
#     count = 0
#     for i in range(s, e):
#         if li[i] < li[s]:
#             count += 1
#
#     li[count] =
#
#
# def quick_sort(li , s, e):
#
#     if s >= e:
#         return
#
#     p = partition(li, s, e)
#
#     quick_sort(li, s, p-1)
#     quick_sort(li, p+1, e)


# s = "asif anas"     # method 1
# s1 = s[::-1]
# print(s1)

# s = "asif anas"        # method 2
# for i in range(len(s)-1, 0, -1):
#     print(s[i])


# class Solution:
#     def longestCommonPrefix(self, arr, n):
#         # code here
#         lenth = 1232313
#         pos = -1
#         count = 0
#         s2 = ""
#
#         for k in range(0, len(arr)):
#             if len(arr[k]) < lenth:
#                 lenth = len(arr[k])
#                 pos = k
#         i = 0
#
#         while i < len(arr[pos]):
#             s1 = arr[pos][:len(arr[pos]) - i]
#             count = 0
#
#             for j in arr:
#
#                 if s1 in j:
#                     pass
#                 else:
#                     count += 1
#             i += 1
#             if count == 0:
#                 s2 = s1
#                 break
#
#         if s2 == "":
#             return -1
#         else:
#             return s2
# a = Solution()
# li = ['d', 'd', 'd', 'd']
# n = 4
#
# result = a.longestCommonPrefix(li, n)
# print(result)
#
#


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# maX = len(li)
# q = 0
#
# s = set()
#
# for i in range(1, maX+1):
#     cout = li.count(i)
#
#     if cout == 1:
#         pass
#     elif cout > 1:
#         s.add(i)
#     else:
#         q += 1
#
# print(q, len(s))


# s = "abss;eue;oi"
# z = s.split(';')
# print(z)
# print(len(z))
#
# print(5 != 6)

# import numpy as np
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = a*b
# d = np.dot(a,b)
# print(c)
# print(d)


# a = 20, 30,40
# print(type(a))
# # print(b)
# # print(c)

# sum = lambda x, y : x+y
#
# sum = lambda x, y: x-y
# print(sum(3,1))


# n1 = 5
# n2 = [9, 7, 3, 12, 7]
# n3 = 14
#
#
# def solve(n2, n1, n3):
#     if n3 == 0:
#         return 1
#     elif sum !=0  and n1 == 0:
#         return 0
#
#     elif n2[n1-1]>n3:
#         return solve(n2, n1-1, n3)
#     else:
#         return solve(n2, n1-1, n3) + solve(n2, n1-1, n3-n2[n1-1])
#
# count = solve(n2, n1, n3)
# print(count)

# n1 = 3
# n2 = 5
# n3 = [[75, 76, 65, 87, 87],[78, 76, 68, 56, 89],[67, 87, 78, 77, 65]]
#
# avg = 999999.0
# index = 0
# sum = 0
#
# for i in range(0, n2):
#     sum = n3[0][i] + n3[1][i] + n3[2][i]
#     p = sum / n1
#     if avg > p:
#         avg = p
#         index = i
#
# sum1 = 0
# for i in range(0, n2):
#     if i != index:
#         sum1 += n3[0][i]
# sum2 = 0
# for i in range(0, n2):
#     if i != index:
#         sum2 += n3[1][i]
# sum3 = 0
# for i in range(0, n2):
#     if i != index:
#         sum3 += n3[2][i]
#
# print(sum1,sum2,sum3)


# p = ('table', 'asd', 'asda')
# t = ('asif', 'anas')
# commonlist = (t[0],) + (t[1],) + p
# print(type(commonlist))


# decorator is a powerfull tools which is used to modify the behaviour of the fuctions or class

# def call(x):
#     return x;
#
# def ycall(func):
#     return func(10)
#
# def xcall(func):
#     def inner():
#         x = func(10)
#         print(x)
#     return inner
#
# x = xcall(call)
# print(x())

# s = "string"
# p = iter(s)
# print(next(p))
# print(next(p))
#
# se = set()
# se.add(2)
# se.add(2)
# se.add(3)
# se.add(52)
# se.add(50)
# print(se)
#
# t = (3,5,23,123,123,1,4)
# print(t)

# def func():
#     for i in range(1,10):
#         return i
#
# def func1():
#     i = 1
#     while(i<10):
#         yield i
#         print("Hallo")
#         i += 1
#
#
#
# j = func1()
# print(j)
# for i in j:
#     print(i)
#     break
#
# for i in j:
#     print(i)
#     break


# shallow copy and deep copy
# from copy import copy,deepcopy
#
# li = [1, 2, 3, 4, 6]
# li1 = copy(li)
# li1[2]=8
# print(li)
# print(li1)
#
# li2 = deepcopy(li)
# li2[3]=10
# print(li)
# print(li2)


# def uppercase(func1):
#     def inner(args):
#         s = ""
#         for i in args:
#             if i.islower() and i != ' ':
#                 s = s + i.upper()
#             else:
#                 s = s + i.lower()
#         func1(s)
#     return inner
#
# @uppercase
# def small(args):
#     print(args)
#
# small('Asif Anas')
#
# Exception-> exception means when breaking of the normal of the execution due to some statement

'''
error --> logical error
          syntax error
          exception
          hanle:try and except
          1-> exception occur
          2-> type of exception occur
          3-> provide solution
'''

#
# '''Custom Exception
#
#  '''


# class myexception(Exception):
#     def __init__(self,error_msg):
#         print(error_msg)
#
#
# marks = int(input("Enter the number"))
# if marks < 80:
#     raise myexception("marks less than required")
# else:
#     print("pass")


# from abc import ABC,abstractmethod
#
# class myabstract(ABC):
#
#
#     @abstractmethod
#     def myname(self):
#         print("Asif anas")
#
# class yesmyname(myabstract):
#     def myname(self):
#         print("yes")
#
# obj = yesmyname()
# obj.myname()

# from threading import Thread
#
# def work_load():
#     for i in range(0,20):
#         print(i)
#
# thread1 = Thread(target=work_load)
# thread2 = Thread(target=work_load)
# thread2.start()
# thread2.join()
# thread1.start()

# student.py
# class myname():
#     def work_load(self):
#         for count in range(0,20):
#             print(count)
#
# obj = myname()
# th1 = Thread(target=obj.work_load)
# th1.start()
# th2 = Thread(target=obj.work_load)
# th2.start()

# import pickle as pk
#
# class myname:
#     def __init__(self, name, rollnumber):
#         self.name = name
#         self.rollnumber = rollnumber
#         print("hi asiff")
#
# obj = myname("asif mas",123)
#
# f1 = open('myname.txt','rb')
# # pk.dump(obj,f1)
# pk.load(f1)
#
#

# def uppercase(func1):
#     def inner(args):
#         s = ""
#         for i in args:
#             if i.islower() and i != ' ':
#                 s = s + i.upper()
#             else:
#                 s = s + i.lower()
#         func1(s)
#     return inner
#
# @uppercase
# def small(args):
#     print(args)

# import sys
# print(type(tuple))
# print(sys.getsizeof(tuple))
# list = [1, 2, 4, 2, 3]
# print(type(list))
# print(sys.getsizeof(list))
# print(list.index(2))
# print(list)
# list1 = list.copy()
# list1[1]="sting"
# print(list)
# print(list1)
# print(list.remove(2))
# print(list)
# def func():
#     for i in range(0,6):
#         yield i
# list.extend(func())
# print(list)
# list.insert(1,"asif")
# print(list)
# list.reverse()
# print(list)


# ---------------------------------------------------------------

# def container(args):
#     l = len(args)
#     string = 'aeiou'
#     count = 0
#     for i in range(0, l):
#         if string.find(args[i]) != -1:
#             count = 1
#             break
#
#     if count != 0:
#         print("Contain vowel")
#     else:
#         print("Does not contain vowel")
#
# container('ffffffffffff')

# dict = {'name':'asif','rollnumber':1234}
#
# print(dict)
#
# print(dict.pop('name'))
# print(dict)
# for i,j in dict.items():
#     print(i)


# list = ['apple', 'orange', 'banana', 'cherry']
# new_list = []
# for i in list:
#     if 'a' in i:
#         new_list.append(i)
#
# print(new_list)
#
# new = [i for i in list if 'a' in i]
# print(new)


# n1 = [10, 20, 40]
# n2 = [30, 50, 80]
#
# l1 = len(n1)
# l2 = len(n2)
# new_list = []
# for i in range(0, l1):
#     for j in range(i, i+1):
#         new_list.append(n1[i]+n2[j])
#
# print(new_list)
# new1=[]
# for i, j in zip(n1, n2):
#     new1.append(i+j)
#
# print(new1)
#
#
# new2 = [i+j for i,j in zip(n1, n2)]
# print(new2)

#
# list = [1, 3, 4, 5, 5, 4]
# new = list[::-1]
# print(new)
# new[0] = 'anas'
# print(new)
# print(list)


import numpy as np

# list = [1, 2, 3, 4]
# arr = np.array(list)
# n = len(arr)
# for i in range(0, n):
#     print(arr[i])

# arr = np.arange(0, 20)
# print(arr)
# n = len(arr)
# arr1 = arr.reshape(2,10)
# print(arr1)


# s = "asif@sd?dsmks13fds"
# s1 = "abcdefghijklmnopqrstuvwxyz"
# s2 = []
# l = len(s)
# d = {}
# for i in range(l-1,-1,-1):
#     if s[i] in s1:
#         s2.append(s[i])
#
# for i in range(0,l):
#     if s[i] in s1:
#         pass
#     else:
#         d[s[i]] = i
#
# for i,j in d.items():
#     s2.insert(j,i)
#
#
# print(s2)


# from abc import ABC, abstractmethod
#
# class mine(ABC):
#
#     def __init__(self, name):
#         self.name = name
#         print("asif anas")
#
#     @abstractmethod
#     def solve(self):
#         pass
#
#
# class optum(mine):
#
#     def solve(self):
#         print("abstract method")
#
#     def __init__(self, name):
#         super().__init__(name)
#         print("base class")
#
#
# m = optum("asif")
# print(m.name)


# class a:
#
#     def __init__(self, name, add):
#         self.name = name
#         self.add = add
#     def mine(self):
#         print(f"{self.name} {self.add}")
#
#
# asif = a("asif", "pahar")
# anas = a("anas", "california")
# anas.mine()


# class iteretor():
#
#    def __iter__(self):
#        self.a = 1
#        return self
#
#    def __next__(self):
#        x = self.a
#        self.a += 1
#        return x
#
# myclass = iteretor()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))

# def fun():
#     for i in range(0, 10):
#         return i
#         print(f"yes it is {i}")
#
# print(fun())
#
#
# def fun():
#     for i in range(0, 10):
#         yield i
#         print(f"yes it is {i}")
#
# g = fun()
# for i in g:
#     print(i)

#
# s = "asif"
# li = []
# li.append(s)
# print(li)


# s = "asif"
# li = {'name':'asif'}
# def fun(args):
#     args = args + "anas"
#     print(args)
#
# def fun1(args):
#     args['add'] = 'pahar'
#     print(args)
# fun(s)
# print(s)
# fun1(li)
# print(li)

# 0 1 1 2 3 5 8 13
# n = int(input('enter the number'))

# def fibo(n):
#     if n == 1:
#         return 0
#
#     if n == 2:
#         return 1
#
#     return fibo(n-1) + fibo(n-2)
#
# for i in range(1, n+1):
#     print(fibo(i))

from threading import Thread

# Thread -> thread is a smallest unit of programm which is execute independently

# def work():
#     for i in  range(0,10):
#         print(i)
#
# t1 = Thread(target=work)
# t2 = Thread(target=work)
# t1.start()
# t2.start()


# class uicorn:
#     def work(self):
#         for i in range(0, 20):
#             print(i)
#
# u = uicorn()
# t1 = Thread(target=u.work)
# t2 = Thread(target=u.work)
# t1.start()
# t2.start()

# class unicorn(Thread):
#     def run(self):
#         for i in range(0, 10):
#             print(i)
#
# u = unicorn()
# u1 = unicorn()
# u.start()
# u1.start()
#
# num = 10
#
# def find():
#     print(num)
#
# print(num)
# find()

# num = 20
#
# def find():
#     num = 10
#     print(num)
#
# find()
# print(num)

# def square(args):
#     return args*args
#
# f = lambda args: args*args
# print(f(10))

# def summation(**args):
#     sum = 0
#     for i, j in args.items():
#         print(f'{i} and {j}')
#
# summation(name='asif')

# old_list = ['banana', 'apple', 'orange', 'grapes']
# new_list = []
# for i in old_list:
#     if 'g' in i:
#         new_list.append(i)

# print(new_list)
# print(old_list)

# new_list1 = [i for i in old_list if 'g' in i]
# print(new_list1)



# monkey patching

# class monkey:
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'my name is {self.name}')
#     def f1(self):
#         self.get_name()
#
#     def f2(self):
#         self.get_name()
#
# mon = monkey('asif')
#
# def after(self):
#     print(f'new name is {self.name}')
#
# monkey.get_name = after
# mon.f1()
# mon.f2()


# class method:
#
#     gender = 'male'
#
#     def __init__(self):
#         self.name = 'asif'
#         self.age = 23
#
#     def info(self):
#         return self.name + str(self.age) + self.gender
#
#     @classmethod
#     def cla(cls):
#         cls.gender = 'Female'
#
# p = method()
# print(p.info())
# method.cla()
# print(p.info())

# s = '(]'
# l = []
# for i in s:
#     if len(l) == 0:
#         l.append(i)
#
#     elif i == '{' or i == '[' or i == '(':
#         l.append(i)
#
#     else:
#         last = l[-1]
#         if i == ')':
#             if last == '(':
#                 l.pop()
#             else:
#                 break
#
#         elif i == '}':
#             if last == '{':
#                 l.pop()
#             else:
#                 break
#         else:
#             if last == '[':
#                 l.pop()
#             else:
#                 break
#
# if len(l) == 0:
#     print('true')
# else:
#     print('False')

# s = '{[[((((()))))]]}'
#
# if len(s)%2 == 0:
#     mid = len(s)//2
#     start = mid-1
#     end = mid
#     while(start >= 0 and end < len(s)):
#         if s[start] == '(':
#             if s[end] == ')':
#                 pass
#             else:
#                 break
#         elif s[start] == '{':
#             if s[end] == '}':
#                 pass
#             else:
#                 break
#
#         else:
#             if s[start] == '[':
#                 if s[end] == ']':
#                     pass
#                 else:
#                     break
#         start -= 1
#         end += 1
#
#     if start == -1:
#         print('balanced')
#     else:
#         print('unbalaneced')
#
#
#
# else:
#     print('unbalanced')

# s = 'bbbbb'
# li = []
# for i in range(0, len(s)):
#     s1 = ''
#     for j in range(0, i + 1):
#         s1 = s1 + s[j]
#
#     li.append(s1)
# longest = ''
# for i in li:
#     dic = {}
#     for j in range(0, len(i)):
#         if i[j] in dic:
#             dic[i[j]] += 1
#         else:
#             dic[i[j]] = 1
#
#     count = 0
#     for j,k in dic.items():
#         if k>1:
#             count += 1
#             break
#
#     if count == 0:
#         longest = i
# print(li)
# print(longest)

# strs = ["dog","racecar","car"]
# largest = ''
# for i in strs:
#     if len(i) > len(largest):
#         largest = i
#
# li = []
# for i in range(0, len(largest)):
#     s1 = ''
#     for j in range(0, i + 1):
#         s1 = s1 + largest[j]
#
#     li.append(s1)
# pos = -1
# for i in range(0, len(li)):
#     count = 0
#     li1 = []
#     for j in range(0, len(strs)):
#         if li[i] in strs[j]:
#             x = strs[j].find(li[i])
#             li1.append(x)
#             s = set(li1)
#             if len(s) > 1:
#                 count += 1
#                 break
#         else:
#             count += 1
#             break
#
#     if count != 0:
#         break
#     else:
#         pos = i
#
#
# print(pos)
# print(li)

# nums = [1,1,2]
# s = set(nums)
# li = list(s)
# li.sort()
# print(li)


# s = "   fly me   to   the moon  "
# li = s.split(' ')
# print(li)
# s = "Hello World"
# s1 = ''
# for i in range(0, len(s)):
#     if s[i] == ' ' and s[i+1] == ' ':
#         pass
#     else:
#         s1 = s1 + s[i]
# print(s1)
# li = s1.split(' ')
# # if li[-1] == '':
# #     li.pop()
# # if len(li) == 0:
# #     print(len(s))
#
# print(li)

# digits = [999]
# n = 0
# for i in range(0, len(digits)):
#     n = n * 10 + digits[i]
#
# n = n + 1
# li = []
# while (n != 0):
#     d = n % 10
#     li.append(d)
#     n = n // 10
#
# li1 = []
# for i in range(len(li)-1, -1, -1):
#     li1.append(li[i])
#
# print(li1)

# def binarytodecimal(num):
#     j = 0
#     n = 0
#     for i in range(len(num) - 1, -1, -1):
#         n = n + 2 ** j * int(num[i])
#         j += 1
#
#     return n
#
# print(binarytodecimal('0'))
#
#
# def decimaltobinary(number):
#     li = []
#     while (number != 0):
#         d = number % 2
#         li.append(d)
#         number = number // 2
#     print(li)
#
# decimaltobinary(0)

# def sqrt(x):
#     li = []
#     for i in range(1, x+1):
#         li.append(i)
#
#     start = 0
#     end = len(li) - 1
#
#     while (start < end):
#         mid = start + end // 2
#
#         number = li[mid] * li[mid]
#
#         if number > x:
#             end = mid-1
#
#         elif number < x:
#             start = mid
#
#         else:
#             return mid+1
#
# print(sqrt(100))

# n = 2
# b = False
# d = {}
# def visited(nums):
#     if nums in d:
#         return True
#     else:
#         d[nums] = 1
#     return False
#
# def findnumber(nums):
#     sum = 0
#     while nums != 0:
#         d = nums % 10
#         sum = sum + d * d
#         nums = nums // 10
#     print(sum)
#     return sum
#
#
# number = n
# while True:
#     if number % 10 == 1:
#         b = True
#         break
#     if visited(number):
#         b = False
#         break
#     else:
#         number = findnumber(number)
#
# print(b)

# name = 'asif anas qamar ahamad haseena khatoon and make my date easy to jump and hava '

# def palindrome(pal):
#     s = pal
#     s1 = pal[-1::-1]
#     if s1 == s:
#         return True
#     else:
#         return False
#
# name = 'mynameirrrrrrrrrrrrrrrrrrrrrrrrrrrras'
# li = []
# for i in range(0, len(name)):
#     for j in range(i+1, len(name)+1):
#         li.append(name[i:j])
#
# index = ''
# l = -1
# for i in li:
#     if palindrome(i):
#         if len(i) > l:
#             l = len(i)
#             index = i
#
# print(f'the longest substricng in the word which is palindrome is {index} and {l}')

# properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
# # properties = [[1,5],[10,4],[4,3]]
# if len(properties) == 0 or len(properties) == 1:
#     print(0)
# s = set()
# count = 0
# for i in range(0, len(properties)):
#     for j in range(0, len(properties)):
#         if i != j:
#             if properties[j][0] > properties[i][0] and properties[j][1] > properties[i][1]:
#                 t = (properties[j][0], properties[j][1])
#                 s.add(t)
#
#                 print(t)
# print('as')
# print(s)
# print(len(s))


# name = 'asif'
# li= []
# for i in range(0, len(name)):
#     for j in range(i+1, len(name)+1):
#         li.append(name[i:j])
# print(li)


############################
###########################
##########################
##########################

# from abc import ABC, abstractmethod
# class asif(ABC):
#
#     @abstractmethod
#     def display(self):
#         pass
#
# class demo(asif):
#     msg = 'massage'
#
#     def display(self):
#         print(self.msg)
#
#     def show(self):
#         print(self.msg)
#         self.msg = 'new massage'
#
# d = demo()
# d.show()
# d.display()


# arr = [5, 6, 7, 11, 12, 13]
# input = 6
# output = True
#
#
# def search(li, target):
#     start = 0
#     end = len(li)
#     count = 0
#     while start<=end:
#         mid = (start + end) // 2
#         if li[mid] == target:
#             count = 1
#             return True
#         elif li[mid] < target:
#             start = mid
#         else:
#             end = mid - 1
#
#     if count == 0:
#         return False
# print(search(arr, input))

# s = 'as3477'
# li = []
# for i in range(len(s)):
#     for j in range(i, len(s)+1):
#         li.append(s[i:j])
#
# print(len(li))
# n = 499
# def prime(nums):
#     i = 2
#     while(i*i<=nums):
#         if nums % i == 0:
#             return False
#         i += 1
#     return True
#
# count = 0
# for i in range(0, n):
#     if n < 3:
#         print(0)
#     if prime(i):
#         count += 1
#
# print(count)

# find out the array is sorted or not with the help of recursion
# li = [2, 4, 6, 9, 12, 30]
#
# def sorted(li, size):
#     print(li)
#     if size == 0 or size == 1:
#         return True
#
#     if li[0] > li[1]:
#         return False
#
#     else:
#         ans = sorted(li[1:size], size-1)
#         return ans
# print(sorted(li, len(li)))
# a = 2
# b = 3
# sum = a&b
# print(sum)
# t = int(input())
#
# while t != 0:
#     li = []
#     n = int(input())
#     m = int(input())
#     for i in range(1, m + 1):
#         for j in range(1, m + 1):
#             li.append([i, j])
#     sum = 0
#     print(li)
#     print(len(li))
#     for i in li:
#         p = i[0] & i[1]
#         sum = sum + p
#         print(sum, end=' ')
#
#     sum = sum % 998244353
#     print(sum)
#     t = t - 1


# bit masking
# li = [4, 1, 9]
# list = []
# n = len(li)
# counter = 1<<n
# for i in range(counter):
#     li1 = []
#     for j in range(n):
#         if (i & (1<<j)) != 0:
#             li1.append(li[j])
#     list.append(li1)
# print(list)

def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    map = {}
    for i in range(len(words)):
        s = words[i]
        if s in map:
            map[s] += 1
        else:
            map[s] = 1
    print(map)
    sorted_dict = sorted(map)
    print(sorted_dict)
    li = []
    j = -1
    for i in range(k):
        li.append(sorted_dict[j])
        j -= 1
    li1 = []
    j = -1
    for i in range(len(li)):
        li1.append(li[j])
        j -= 1

    print(li1)

words = ["i","love","leetcode","i","love","coding","i","i","leetcode","leetcode"]
k = 2
topKFrequent(words, k)










