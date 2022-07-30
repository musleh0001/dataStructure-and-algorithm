"""
    Title			: Balanced Brackets
    Description		: Check for Balanced Brackets in and expression using Stack
    Author			: Md Musleh Uddin Khan
    Date			: 30-07-2022
"""


def areBracketsBalanced(expr):
    for char in expr:
        stack = []

        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    expr = "{()}[]"
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
