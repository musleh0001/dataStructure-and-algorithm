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

    def getNth_iter(self, index):
        tmp = self.__head
        count = 0

        while tmp:
            if count == index:
                return tmp.data
            count += 1
            tmp = tmp.next
        return 0

    def getNth_rec(self, head, index, count=0):
        if count == index:
            return head.data
        return self.getNth_rec(head.next, index, count + 1)


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("U")
    llist.push("F")
    llist.push("P")
    llist.push("M")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")
    print(f"Element at index 3 is: {llist.getNth_rec(llist.head, 3)}")
