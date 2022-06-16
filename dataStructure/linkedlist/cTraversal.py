class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CirularLinkedList:
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    # insert at the begineering of the circular linked list
    def push(self, data):
        ptr1 = Node(data)
        tmp = self.__head
        ptr1.next = self.__head

        if self.__head is not None:
            while tmp.next != self.__head:
                tmp = tmp.next
            tmp.next = ptr1
        else:
            ptr1.next = ptr1
        self.__head = ptr1

    def __str__(self):
        cstr = ""
        tmp = self.__head
        while tmp:
            cstr += str(tmp.data) + " "
            tmp = tmp.next
            if tmp == self.__head:
                break
        return cstr


if __name__ == "__main__":
    clist = CirularLinkedList()
    clist.push(12)
    clist.push(56)
    clist.push(2)
    clist.push(11)

    print("Contents of circular linked list")
    print(clist)
