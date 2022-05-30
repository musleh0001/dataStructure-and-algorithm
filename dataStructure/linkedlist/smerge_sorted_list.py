"""
    Single Linked list: Merge two sorted list.
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

    def mergeLists_dummy(self, head1, head2):
        dummyNode = Node(0)

        tail = dummyNode

        while True:
            if head1 is None:
                tail.next = head2
                break
            if head2 is None:
                tail.next = head1
                break

            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        return dummyNode.next

    def mergeLists_rec(self, head1, head2):
        tmp = None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data <= head2.data:
            tmp = head1
            tmp.next = self.mergeLists_rec(head1.next, head2)
        else:
            tmp = head2
            tmp.next = self.mergeLists_rec(head1, head2.next)
        return tmp

    def __len__(self):
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


if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.push(25)
    llist1.push(15)
    llist1.push(10)
    llist1.push(5)

    llist2.push(30)
    llist2.push(20)
    llist2.push(3)
    llist2.push(2)
    
    print("Before Merge: ")
    print(f"List 1: {llist1}\nLength: {len(llist1)}\n")
    print(f"List 2: {llist2}\nLength: {len(llist2)}\n")

    print("After Merge: ")
    llist3 = LinkedList()
    llist3.head = llist3.mergeLists_rec(llist1.head, llist2.head)
    print(f"List 1: {llist3}\nLength: {len(llist3)}\n")
