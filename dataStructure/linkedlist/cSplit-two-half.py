class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, val):
        self.__head = val
        return self.head

    def __str__(self):
        cstr = ""
        tmp = self.head

        while tmp:
            cstr += str(tmp.data) + " "
            tmp = tmp.next
            if tmp == self.head:
                break
        return cstr

    def push(self, new_data):
        new_node = Node(new_data)
        tmp = self.head
        new_node.next = self.head

        if self.head:
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def splitList(self, head1, head2):
        slow_ptr = self.head
        fast_ptr = self.head

        if not self.head:
            return

        # if there are odd nodes then
        # fast_ptr->next becomes head else
        # fast_ptr->next->next becomes head
        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        # if there are even nodes then move fast_ptr
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

        # set the head pointer of first half
        head1.head = self.head

        if self.head.next != self.head:
            head2.head = slow_ptr.next

        # make second half circular
        fast_ptr.next = slow_ptr.next

        # make first half circular
        slow_ptr.next = self.head


if __name__ == "__main__":
    clist = CircularLinkedList()
    clist1 = CircularLinkedList()
    clist2 = CircularLinkedList()

    clist.push("D")
    clist.push("C")
    clist.push("B")
    clist.push("A")

    print(f"Original Circular Linked list: {clist}")

    clist.splitList(clist1, clist2)

    print(f"\nFirst Circular Linked list: {clist1}")
    print(f"\nSecond Circular Linked list: {clist2}")
