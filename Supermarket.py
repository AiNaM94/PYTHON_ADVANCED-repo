from collections import deque

deque_magazine = deque()
person_entry = input()

while person_entry != "End":
    if person_entry != "Paid":
        deque_magazine.append(person_entry)
    else:
        for customer in range (len(deque_magazine)):
            print(deque_magazine.popleft())

    person_entry = input()
print(f"{len(deque_magazine)} people remaining.")








