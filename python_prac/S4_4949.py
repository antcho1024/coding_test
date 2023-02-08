import sys

while True:
    str = sys.stdin.readline().rstrip()
    if str == '.': break
    i = 0
    stack = []
    result = "yes"

    for s in str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                result = "no"
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                result = "no"
                break
            stack.pop()
    if stack: result = "no"
    print(result)
