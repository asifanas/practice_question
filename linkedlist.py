class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

        else:
            self.head = newNode

    def traverse(self):
        current = self.head
        while current:
            print(f'{current.data}-->', end=' ')
            current = current.next

    def extrawork(self, m):
        current = self.head
        newcurrent = self.head
        prnode = None
        count = 0
        i = 0
        while current:
            if i < m+1:
                i += 1
                current = current.next
            else:
                count = 1
                prnode = newcurrent
                newcurrent = newcurrent.next
                current = current.next

        if count == 1:
            prnode.next = newcurrent.next
        else:
            print('Cant performed delete operation')

l = linkedList()
l.insertNode(1)
l.insertNode(2)
l.insertNode(3)
l.insertNode(4)
l.insertNode(5)
l.insertNode(6)
l.insertNode(7)
l.insertNode(8)
l.insertNode(9)
l.insertNode(10)
l.traverse()
print()
l.extrawork(2)
l.traverse()

