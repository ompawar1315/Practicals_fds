net_amount = 0
s = input("enter the operation and then amount")
for values in range(1):
    values = s.split(" ")
    operation = values[-1]
    amount = int(values[0])
    if operation=="D":
        net_amount=net_amount+amount
    elif operation=="W":
        if(net_amount>=0 and net_amount>amount):
            net_amount=net_amount-amount
        else:
            print("insufficent")
    else:
        pass
print(net_amount)
