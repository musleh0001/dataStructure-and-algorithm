"""
    Single Linked list: Node Swap
    1. Node_1 and Node_2 are not head nodes.
    2. Node_1 or Node_2 are head nodes.
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

    def swap(self, key_1, key_2):
        if key_1 == key_2:
            return

        # search key 1
        prev_1 = None
        curr_1 = self.__head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # search key 2
        prev_2 = None
        curr_2 = self.__head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # if one of the key is missing
        if not curr_1 or not curr_2:
            return

        # swap
        if prev_1:
            prev_1.next = curr_2
        else:
            # if head
            self.__head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            # if head
            self.__head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


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
    print("Before Swap: ", end="")
    llist.printList()
    llist.swap("B", "D")
    print("After Swap: ", end="")
    llist.printList()
