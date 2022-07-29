"""
    Single Linked list: Reverse.
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

    def reverse_iter(self) -> None:
        """
            * Time Complexity: O(n)
            * Space Complexity: O(1)
        """
        prev = None
        current = self.__head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.__head = prev

    def reverse_rec(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse_rec(head.next)
        head.next.next = head
        head.next = None
        return rest

    def reverseUsingStack(self):
        stack, tmp = [], self.__head

        while tmp:
            stack.append(tmp)
            tmp = tmp.next

        self.__head = tmp = stack.pop()

        while len(stack) > 0:
            tmp.next = stack.pop()
            tmp = tmp.next

        tmp.next = None
    
    def __str__(self) -> None:
        tmp = self.__head
        llstr = ""

        while tmp:
            llstr += str(tmp.data) + " -> "
            tmp = tmp.next
        llstr += "None"
        return llstr


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
    llist.head = llist.reverse_rec(llist.head)
    # llist.reverseUsingStack()
    print("After reverse: \t\t", end="")
    print(llist)
