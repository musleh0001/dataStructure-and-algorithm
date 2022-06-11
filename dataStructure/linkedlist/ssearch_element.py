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

    def search_iter(self, key):
        tmp = self.__head
        while tmp:
            if tmp.data == key:
                return True
            tmp = tmp.next
        return False

    def search_rec(self, head, key):
        if not head:
            return False
        if head.data == key:
            return True
        return self.search_rec(head.next, key)


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("U")
    llist.push("F")
    llist.push("P")
    llist.push("M")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")

    key = "P"
    isFound = llist.search_rec(llist.head, key)
    if isFound:
        print(f"{key} found in Linked List")
    else:
        print(f"{key} not found in Linked List")
