initial_balance = float(input("enter your initial balance: "))

transaction_type = input("enter transaction type (withdrawal, deposit, balance inquiry): ").lower()

if transaction_type == 'withdrawal':
    amount = float(input("enter the amount to withraw: "))
    if amount > initial_balance:
        print("insufficient balance...")

    else:

            initial_balance -= amount
            print("withdrawal is successful! the new balance is:",initial_balance)

elif transaction_type == 'deposit':
    add = float(input("enter the amount to deposit: "))
    initial_balance += add
    print("successfully deposited! the new balance is: ",initial_balance)

elif transaction_type == 'balance inquiry':
    print("the balance is: ",initial_balance)

else:
    print("invalid transaction type....")
