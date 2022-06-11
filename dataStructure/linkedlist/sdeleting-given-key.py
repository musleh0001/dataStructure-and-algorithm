"""
    Deleting a node at given key
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode_iter(self, key):
        tmp = self.head

        # if head node itself holds the key to be deleted
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                tmp = None
                return

        while tmp is not None:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp == None:
            return

        prev.next = tmp.next
        tmp = None

    def printList(self):
        tmp = self.head
        while tmp:
            print(" %d" % (tmp.data))
            tmp = tmp.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)

    print("Created Linked List:")
    llist.printList()
    llist.deleteNode_iter(2)
    print("\nLinked List after deletion:")
    llist.printList()
