from collections import deque

watter_reserve = int(input())
pouring_watter = input()
queue_drinkers = deque()

while pouring_watter != "Start":
    queue_drinkers.append(pouring_watter)
    pouring_watter = input()

litters = input()
while litters != "End":
    if "refill" not in litters:
        if watter_reserve >= int(litters):
            watter_reserve -= int(litters)
            print(f"{queue_drinkers.popleft()} got water")
        else:
            print(f"{queue_drinkers.popleft()} must wait")

    else:
        cuter = litters.split(" ")
        litters = cuter[1]
        watter_reserve += int(litters)
    litters = input()
print(f"{watter_reserve} liters left")




