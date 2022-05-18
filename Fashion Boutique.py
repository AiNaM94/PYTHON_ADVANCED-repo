

box_of_clothes = [int(num) for num in input().split(" ")]
rag_capacity = int(input())
total_rag_need = 1
current_rag = 0
while box_of_clothes:
    ordering = box_of_clothes.pop()
    if current_rag + ordering <= rag_capacity:
        current_rag += ordering
    else:
        box_of_clothes.append(ordering)
        total_rag_need += 1
        current_rag = 0
print(total_rag_need)



