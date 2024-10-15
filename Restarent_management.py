def order():
    # for i in range(1, len(orderitems)+1):
    i=1
    while True:
        user = input(f"Enter the {i}th item:").lower()
        list.append(user)
        print("Order added")
        i=i+1
        user2 = input("Do u want anything else:").lower()
        if user2 == "yes":
            continue
        else:
            print("Thanks for shoping")
            break
    return

list=list()
# price=list()
orderitems={
    "pizza": 40,
    "burger": 50,
    "coffee": 80,
    "salad": 70,
    "pasta": 50
}
print("wellcome to out restarent. Here's the menu:")
for key, value in orderitems.items():
     print(key,": Rs",value)

while True:
    ready=input("sir are u ready:").lower()
    if ready=="yes":
        order()
        break
    elif ready == "no":
        break
    else:
        print("ok take your time")
print(list)
total=0
for i in list:
    total+=orderitems[i];
print(total)












