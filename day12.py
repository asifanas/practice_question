# # custom Exception
#
# # part1
# # marks = int(input("enter the marks : "))
# #
# # if marks < 80:
# #     print("Go furthure")
# #     print("need practice")
# # else:
# #     print("Go for next module")
# #
# #
# # # part2
# # marks = int(input("enter the marks : "))
# #
# # if marks<80:
# #     raise Exception("Need practice")
# #     print("Go furthure")
# #     # print("need practice")
# #
# #
# # else:
# #     print("Go for next module")
# #
#
# # part 3
#
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
#
#
# class collegeExcp_lower(Exception):
#     def __init__(self, error_age):
#         super().__init__(error_age)
#
#
# class collegeExcp_upper(Exception):
#     def __int__(self, error_age):
#         super().__init__(error_age)
#
#
# age = int(input("Enter Age : "))
#
# if 18 < age < 24:
#     print("Satisfied")
# elif age < 18:
#     raise collegeExcp_lower("Age under")
# else:
#     raise collegeExcp_upper("Upper age")
#
#
# # # f1 = open("mydata.txt", "r")
# # # # print(f1)
# # # #
# # # # for data in f1:
# # # #     print(data)
# # # #
# # # # # or
# # #
# # # print(f1.read(49))
# #
# #
# # # f1 = open("mydata.txt", "r")
# #
# # # try:
# # #     print(f1.read())
# # #     print(10 / 0)
# # #
# # # except ZeroDivisionError as a:
# # #     print("Exception caugth")
# # #
# # # finally:
# # #     print("finally file close")
# # #     f1.close()
# #
# # # print(f1.tell())
# # # print(f1.readline())
# # # print(f1.readline())
# # # print(f1.readline())
# # # print(f1.readline())
# # # print(f1.readline())
# # # print(f1.readline())
# # # print(f1.seek(6))
# # # print(f1.seek(0))
# # # print(f1.readline())
# #
# # import pickle
# #
# # # li = ["Asif\n", "Anas\n"]
# # #
# # # f1 = open("mydata.dat", "wb")
# # #
# # # pickle.dump(li, f1)
# #
# # f1 = open("mydata.dat", "rb")
# # pickle.load(f1)
# #
# #
# #
# #

