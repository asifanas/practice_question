# A Bank owner wants to have a console app which should have features like
#
# 1. Savings account
# 2. debit amount
# 3. credit amount
# 4. display the current balance

# Note - > 1. There are n numbers of accounts for users so the amount should be differnt for each user
#          2. use oop approch of programming

import sys


class Account:
    amount = 0

    def __init__(self, name = None, acc_number = None):
        if name == None:
            return
        self.name = name
        self.acc_number = acc_number
        print("Account Holder name: ", self.name)
        print("Account number : ", acc_number)

    def debit(self, amount):

        if self.amount < amount:
            print("Insufficeint Balance")
        else:
            self.amount = self.amount-amount
            print("Amount is debited")

    def credit(self):
        amount = 0
        print("Enter the amount you want to credtt:")
        amount = int(input())
        self.amount = self.amount + amount
        print("Your amount is credited")

    def balance(self):
        print("Your current balanace is : " , self.amount)


print("Enter The number of User :")
n = int(input())

i = 0
li = list()
while i<n:
    m1 = Account()
    li.append(m1)
    while(True):
        print("Please enter Operation number which is you want to perform:"
              "1.Savings account"
              "2.debit amount"
              "3.credit amount"
              "4.display the current balance"
              "5.Exit")

        input1 = int(input())

        if input1 == 1:
            print("Enter name of user:")
            name = input()
            print("Enter Account number")
            acc = input()
            # m1 = Account(name, acc)
            Account(name, acc)

        if input1 == 2:
            print("Enter the debited amount:")
            amount = int(input())
            li[i].debit(amount)

        if input1 == 3:
            li[i].credit()

        if input1 == 4:
            li[i].balance()

        if input1 == 5:
            print("Thank You:")
            quit()

    i = i + 1





