string_for_reverse = input()

stack_string = []

for letter in string_for_reverse:
    stack_string.append(letter)

reversed_string = ""

while stack_string:
    reversed_string += stack_string.pop()
print(reversed_string)



