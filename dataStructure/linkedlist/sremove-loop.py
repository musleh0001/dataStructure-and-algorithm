"""
    Single Linked List: Detect and Remove Loop
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
    def head(self, new_head):
       self.__head = new_head
       return self.__head

    def __len__(self):
       tmp = self.__head
       count = 0

       while tmp:
           count += 1
           tmp = tmp.next

       return count

    def __str__(self):
       output = ""
       tmp = self.__head

       while tmp:
           output += str(tmp.data) + " "
           tmp = tmp.next
       return output

    def push(self, new_data):
       new_node = Node(new_data)
       new_node.next = self.__head
       self.__head = new_node

    def detectAndRemoveLoop(self):
        if self.__head is None:
            return

        if self.__head.next is None:
            return

        slow_p = fast_p = self.__head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            # if slow_p and fast_p meet at some point then there is a loop
            if slow_p == fast_p:
                slow_p = self.__head
                while slow_p.next != fast_p.next:
                    slow_p = slow_p.next
                    fast_p = fast_p.next

                fast_p.next = None

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(12)
    llist.push(32)
    llist.push(27)
    llist.push(19)
    llist.push(4)

    # create a loop
    llist.head.next.next.next.next.next = llist.head.next.next

    loop = llist.detectAndRemoveLoop()

    print(f"Linked List: {llist}")

