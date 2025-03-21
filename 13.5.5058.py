BRACKETS = {"(": ")", "[": "]", "{": "}"}

def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        elif BRACKETS.get(stack.pop()) != bracket:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    sequence = input().strip()
    print("yes" if check(sequence) else "no")
