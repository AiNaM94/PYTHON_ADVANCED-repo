
quantity_of_food = int(input())
orders = [int(numbers) for numbers in input().split(" ")]
copy_order = orders.copy()
copy_order.sort()
x = len(orders) -1
print(copy_order[x])
for i in range(x+1):
    finishing_orders = int(orders[0])
    if finishing_orders <= quantity_of_food:
        quantity_of_food -= finishing_orders
        orders.pop(0)
if len(orders) == 0:
    print("Orders complete")
else:
    print("Orders left:", end=" ")
    for ord in orders:
        print(f"{ord}", end=" ")


















