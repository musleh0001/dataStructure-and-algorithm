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

    def isPalindrome_stack(self):
        stack = []
        tmp = self.__head

        while tmp:
            stack.append(tmp.data)
            tmp = tmp.next

        tmp = self.__head
        while tmp:
            poped = stack.pop()
            print(f"Current: {tmp.data}\tPopped: {poped}")
            if poped != tmp.data:
                return False
            tmp = tmp.next
        return True

    def isPalindrome_reverse_list(self, head):
        slow_ptr = fast_ptr = prev_of_slow_ptr = head
        midNode = None
        res = True

        if head and head.next:
            while fast_ptr and fast_ptr.next:
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next

            if fast_ptr:
                # when list is odd length
                midNode = slow_ptr
                slow_ptr = slow_ptr.next

            second_half = slow_ptr
            prev_of_slow_ptr.next = None

            # reverse
            second_half = self.reverse(second_half)

            # compare
            res = self.compareLists(head, second_half)

            if midNode:
                prev_of_slow_ptr.next = midNode
                midNode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res

    def reverse(self, second_half):
        current = second_half
        prev = next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        second_half = prev
        return second_half

    def compareLists(self, head1, head2):
        tmp1, tmp2 = head1, head2

        while tmp1 and tmp2:
            if tmp1.data != tmp2.data:
                return False
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        if not tmp1 and not tmp2:
            return True
        return False


if __name__ == "__main__":
    llist = LinkedList()
    llist.push("R")
    llist.push("A")
    llist.push("D")
    llist.push("A")
    llist.push("R")

    print(f"Length of Single Linked List: ", len(llist))
    print(f"Single Linked List: {llist}")

    print("isPalindrom: ", llist.isPalindrome_reverse_list(llist.head))
