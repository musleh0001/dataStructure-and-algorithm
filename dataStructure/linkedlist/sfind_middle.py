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

    @head.setter
    def head(self, val):
        self.__head = val
        return self.__head

    def __len__(self) -> int:
        count = 0
        tmp = self.__head
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def __str__(self) -> None:
        tmp = self.__head
        llstr = ""
        while tmp:
            llstr += str(tmp.data) + " "
            tmp = tmp.next
        return llstr

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.__head
        self.__head = new_node

    def get_middle(self):
        slow_ptr = fast_ptr = self.__head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print(f"Middle of Single Linked List is: {slow_ptr.data}")


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("U")
    llist.push("F")
    llist.push("P")
    llist.push("H")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")
    llist.get_middle()
