# A Laptop company wants to build a laptop for which they requires  ram, camera and os
#
#
# RAM must have features that is size and name
# CAMERA must have feature that is megapixel
# OS must have features that is version, os_name and os_release_date
# LAPTOP must have features that is ram, camera, os and laptop_company_name
#
#
# NOTE -> each laptop values must be diff.
#         create atleast 2 laptops
# 		use appropriate access specifiers whenever required
# 		use OOP approch for programming

class Laptop:

    def __init__(self, laptop):

        self.laptop_name = laptop
        self.__ram()
        self.__camera()
        self.__os_version()
        print("Laptop Name: ", self.laptop_name)

    def __ram(self):
        print("Enter the size and name of the ram")
        self.__size = int(input())
        self.__name = input()

    def __camera(self):
        print("Enter megapixel of the camera:")
        self.__megapixel = int(input())

    def __os_version(self):
        print("Enter version name and os name and os release date:")
        self.__version = input()
        self.__os_name = input()
        self.__release_date = input()

    def display(self):
        print("RAM:")
        print("size: ", self.__size)
        print("name: ", self.__name)
        print("Camera:")
        print("Megapixel: ", self.__megapixel)
        print("OS_VERSION:")
        print("version: ", self.__version)
        print("Os name: ", self.__os_name)
        print("release date: ", self.__release_date)

laptop1 = Laptop("HP ProBook")
laptop1.display()

laptop2 = Laptop("MACBOOK")
laptop2.display()

