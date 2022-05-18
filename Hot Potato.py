from collections import deque
participants = deque(input().split(" "))
last_participant = ""
num = int(input())


while participants:
    for n in range(num-1):
        participant =  participants.popleft()
        participants.append(participant)

    last_participant = participants.popleft()
    print(f"Removed {last_participant}")
    if len(participants) == 1 :
        break

print(f"Last is {participants[0]}")





