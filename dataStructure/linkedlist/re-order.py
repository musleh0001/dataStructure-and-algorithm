"""
    Reorder Linked List
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

    @head.setter
    def head(self, val):
        self.__head = val
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

    def __str__(self) -> None:
        tmp = self.__head
        llstr = ""

        while tmp:
            llstr += str(tmp.data) + " → "
            tmp = tmp.next

        llstr += "None"
        return llstr

    def reorder(self):
        slow, fast = self.__head, self.__head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = self.__head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("E")
    llist.push("D")
    llist.push("C")
    llist.push("B")
    llist.push("A")
    print("Length of Single Linked List (iter): ", len(llist))
    print("Before reverse: \t", end="")
    print(llist)

    print("Reorder Linked List: \t", end="")
    llist.reorder()
    print(llist)
