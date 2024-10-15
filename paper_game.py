import random
user_choice = input("your choice will be(rock,paper,scissor)")
print("your choice is: ")
print(user_choice)
print()


choice = ['rock','paper','scissor']
computer_choice = random.choice(choice)
print("computer choice is: ")
print(computer_choice)

print()
print()
if computer_choice == user_choice:
    print("the game is draw.....")
elif computer_choice == 'paper' and user_choice == 'rock':
    print("you are the winner...")
elif computer_choice == 'scissor' and user_choice == 'rock':
    print("you are the winner...")
elif computer_choice == 'rock' and user_choice == 'paper':
    print("you are the winner...")
elif computer_choice == 'scissor' and user_choice == 'paper':
    print("computer is the winner...")
elif computer_choice == 'rock' and user_choice == 'scissor':
    print("computer is the winner...")
elif computer_choice == 'paper' and user_choice == 'scissor':
    print("you are the winner...")
