class Node():
    def __init__(self, data=None):
        self.data = data
        self.prev, self.next = None, None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    # insert at begin
    def insertBegin(self, data):
        start = self.head

        tmp = Node(data)
        #empty lsit
        if not start:
            self.head = self.tail = tmp
            return
        # note that below for insert at begin, tail will not change because it is already pointing last index
        tmp.next = start
        start.prev = tmp
        start = tmp

    # insert at end
    def insertEnd(self, data):
        end = self.tail

        tmp = Node(data)
        # empty list
        if not end:
            self.head = self.tail = tmp
        # note that below for insert at end, head will not change because it is already pointing first index
        tmp.prev = end
        end.next = tmp
        end = tmp

    # forward traversal
    def printListForward(self):
        ptr = self.head

        while ptr:
            print(ptr.data)
            ptr = ptr.next

    # backward traversal
    def printListBackward(self):
        ptr = self.tail

        while ptr:
            print(ptr.data)
            ptr = ptr.prev

