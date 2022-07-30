""" 
    Title           : Reverse String
    Description     : Reverse a string using stack
    Author          : Md Musleh Uddin Khan
    Date            : 30-07-2022
"""


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def size(self) -> int:
        return len(self.stack)

    def isEmpty(self) -> bool:
        if self.size() == 0:
            return True

    def push(self, item: str) -> str:
        self.stack.append(item)

    def pop(self) -> str:
        if self.isEmpty():
            return
        return self.stack.pop()


def reverse(string: str) -> str:
    n = len(string)
    stack = Stack()

    for i in range(0, n, 1):
        stack.push(string[i])

    string = ""

    for i in range(0, n, 1):
        string += stack.pop()

    return string


if __name__ == "__main__":
    string = "MdMuslehUddin"
    string = reverse(string)
    print(f"Reversed string is {string}")
