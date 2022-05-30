"""
    Single Linked list: Delete node from given position.
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

    def __len__(self) -> int:
        count = 0
        tmp = self.__head
        while tmp:
            count += 1
            tmp = tmp.next
        return count
    
    def deleteNode(self, position: int) -> None:
        if self.__head is None:
            return

        # if given position is head
        if position == 0:
            self.__head = self.__head.next
            return
        
        index = 0
        current = self.__head
        prev = self.__head
        tmp = self.__head
        while current is not None:
            if index == position:
                tmp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = tmp


    def printList(self) -> None:
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
    print("Length of Single Linked List (iter): ", len(llist))
    print("Before Delete: ", end="")
    llist.printList()
    llist.deleteNode(2)
    print("After Delete: ", end="")
    llist.printList()
