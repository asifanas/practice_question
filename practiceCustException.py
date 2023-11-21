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
# try:
#     print(10 /0)
#
# except:
#     print("except block")
#
# finally:
#     print("Finally block")
#
# print("end")

def foo():
    try:
        print(10/0)
        return 'try'
    except:
        return 'except'
    finally:
        return 'finally'

print(foo())
