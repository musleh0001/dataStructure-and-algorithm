"""
    Single Linked list: Length
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.__head
        self.__head = new_node

    def printList(self):
        tmp = self.__head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("D")
    llist.push("C")
    llist.push("B")
    llist.push("A")
    llist.printList()
