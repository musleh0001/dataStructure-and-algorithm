class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # init next as null


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(10)
    llist.push(20)
    llist.push(30)
    llist.append(40)
    llist.insertAfter(llist.head.next, 50)

    llist.printList()
