

stack = []
num = int(input())

for _ in range(num):
    console = input().split()
    command = console[0]
    test = stack.copy()
    test.sort()
    if command == "1":
        x = int(console[1])
        stack.append(x)
    elif command == "2" and len(stack) > 0:
        stack.pop()
    elif command == "3" and len(stack) > 0:
        print(test[(len(test))-1])
    elif command == "4" and len(stack) > 0:
        print(test[0])
for i in range(len(stack)):
    if len(stack) == 1:
        print(stack.pop(), end="")
    else:
        print(f"{stack.pop()}", end=", ")




