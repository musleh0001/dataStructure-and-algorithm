class StackNode:
    def __init__(self, data = 0, next = None) -> None:
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

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"{stack.pop()} popped from stack")
    print(f"Top element is {stack.peek()}")
