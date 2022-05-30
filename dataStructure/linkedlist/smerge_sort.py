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

    def __len__(self):
        count = 0
        tmp = self.__head
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def __str__(self):
        li = ""
        tmp = self.__head
        while tmp:
            li += str(tmp.data) + " "
            tmp = tmp.next
        return li

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.__head
        self.__head = new_node

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.getMiddle(head)
        nexttomiddle = middle.next

        middle.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if head == None:
            return head
        
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortedMerge(self, left, right):
        result = None

        if left == None:
            return right
        if right == None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(15)
    llist.push(10)
    llist.push(5)
    llist.push(20)
    llist.push(3)
    llist.push(2)

    print("Before sort:")
    print(f"List:\t{llist}\nLength:\t{len(llist)}")

    print("\nAfter sort:")
    llist.head = llist.mergeSort(llist.head)
    print(f"List:\t{llist}\nLength:\t{len(llist)}")
