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

    def nthFromLast(self, n):
        tmp = self.__head
        length = self.__len__()

        if n > length:
            print("Location is greater than the length of Linked List")
            return

        tmp = self.__head
        for i in range(0, length - n):
            tmp = tmp.next
        print(tmp.data)

    def nthFromLastNode(self, n):
        main_ptr = self.__head
        ref_ptr = self.__head

        count = 0
        if self.__head is not None:
            while count < n:
                if ref_ptr is None:
                    print(f"{n} is greater than the no. pf node")
                    return
                ref_ptr = ref_ptr.next
                count += 1

        if ref_ptr is None:
            print(f"Node no. {n} from last is {main_ptr.data}")
        else:
            while ref_ptr is not None:
                main_ptr = main_ptr.next
                ref_ptr = ref_ptr.next
            print(f"Node no. {n} from last is {main_ptr.data}")


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("U")
    llist.push("F")
    llist.push("P")
    llist.push("M")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")
    llist.nthFromLastNode(5)
