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

    def frequency_iter(self, key):
        count = 0
        tmp = self.__head

        while tmp:
            if tmp.data == key:
                count += 1
            tmp = tmp.next

        return count

    def frequency_rec(self, head, key, count=0):
        if not head:
            return count
        if head.data == key:
            count += 1
        return self.frequency_rec(head.next, key, count)


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("F")
    llist.push("E")
    llist.push("U")
    llist.push("F")
    llist.push("P")
    llist.push("H")
    llist.push("F")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")
    print(f"Count: {llist.frequency_rec(llist.head, 'F')}")
