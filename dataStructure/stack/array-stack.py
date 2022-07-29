from sys import maxsize

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

if __name__ == "__main__":
    stack = createStack()
    push(stack, str(10))
    push(stack, str(30))
    push(stack, str(80))
    print(pop(stack) + " popped from stack")
