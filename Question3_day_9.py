# A super market showroom owner needs a console based application so that he/ she can
# 1. view total avaialable items
# 2. update items
# 3. delete items
#
# Note -> i) it should provide all the options to console so the owner can chhose accordingly
#         ii) it should keep on asking for the options so that owner need not to worry about re running
# 		    the console application
#         iii) use only functional approch for programming

item = list()


def total_Available():
    if len(item) == 0:
        print("There is no item available")
        return

    print("Available items are:")
    print(item)


def update(i):
    item.append(i)
    print("Item update successfully:")


def delete(it):
    count = 0
    for i in item:
        if i == it:
            count  = 1
            item.remove(it)

    if count == 0:
        print("items is not available in the market")
    else:
        print(f"{it} item is deleted successfully")


while True:
    print('''Choose Operation
     1.view total avaialable items
     2.update items
     3.delete items
     4.Exit''')
    print()

    operation = int(input())

    if operation == 1:
        total_Available()

    if operation == 2:
        print("Enter the item name:")
        it = input()
        update(it)

    if operation == 3:
        print("Enter item which you want to delete:")
        it = input()
        delete(it)

    if operation == 4:
        print("thank you")
        quit()







