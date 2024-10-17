size = input("which pizza do you want(S,M,L)? ")
bill = 0

if size=='s' or size=='S':
    print("price of the small pizza is 100 rupees.")
    bill += 100

if size=='m' or size=='M':
    print("price of the medium pizza is 200 rupees.")
    bill += 200

if size=='l' or size=='L':
    print("price of the large pizza is 300 rupees.")
    bill += 300

pepperoni = input("do you want pepperoni(y/n)?")
if pepperoni=='y' or pepperoni=='Y':
    if size == 's' or size == 'S':
        bill+=30
    else:
        bill+=50

cheese = input("do you want cheese(y/n)?")
if cheese=='y' or cheese=='Y':
    bill+=20

print(f"your final bill is {bill}")

