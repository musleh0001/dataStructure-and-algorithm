from sys import maxsize
from collections import deque
from queue import LifoQueue

# Implement using stack
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(f"{item} pushed to stack")


def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


# Implement using linked list
class StackNode:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print(f"{data} pushed to stack")

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        tmp = self.root
        self.root = self.root.next
        popped = tmp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data


# Implement using collections.deque
stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print("Initial stack:")
print(stack)

print(f"Popped {stack.pop()}")

# Implement using queue
stack = LifoQueue(maxsize=3)
print(stack.qsize())

stack.put("a")
stack.put("b")
stack.put("c")

print(f"Full: {stack.full()}")
print(f"Size: {stack.qsize()}")

print("Elements popped from the stack")
print(stack.get())
print(stack.get())

print(f"Empty: {stack.empty()}")


if __name__ == "__main__":
    # list
    # stack = createStack()
    # push(stack, str(10))
    # push(stack, str(30))
    # push(stack, str(80))
    # print(pop(stack) + " popped from stack")

    # linked list
    # stack = Stack()
    # stack.push(10)
    # stack.push(20)
    # stack.push(30)
    # print(f"{stack.pop()} popped from stack")
    # print(f"Top element is {stack.peek()}")

    # collection.queue
    print()
