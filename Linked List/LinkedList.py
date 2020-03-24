# single Node
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    # head
    def __init__(self):
        self.head = None

    # insert at begin
    def insertBegin(self, data):
        # creating a new node
        n = Node(data)
        n.next = self.head
        self.head = n

    # insert at end
    def insertEnd(self, data):
        ptr = self.head
        # checking for empty list
        if not ptr:
            self.head = Node(data)
            return
        # traversing to the end
        while ptr.next:
            ptr = ptr.next
        # inserting at the end
        ptr.next = Node(data)

    # insert after a node
    def afterNode(self, posValue, data):
        ptr = self.head
        # empty list
        if not ptr:
            raise Exception('EmptyList')
        # traversing the list to find the value
        while ptr.next:
            if ptr.data==posValue:
                tmp = Node(data)
                tmp.next = ptr.next
                ptr.next = tmp
                return
            ptr = ptr.next
        # if value not found
        raise Exception('NotFound')

    # forward traversal
    def printList(self):
        ptr = self.head
        while(ptr):
            print(ptr.data)
            ptr = ptr.next

if __name__ == "__main__":
    llist = LinkedList()
    # blank linked list
    llist.printList()

    while True:
        n = input('enter # to exit else keep entering data: ')
        if n=='#':
            break
        llist.insertEnd(n)
    llist.printList()
    pos = input('enter the pos after which you want to enter: ')
    llist.afterNode(pos, 100)
    llist.printList()