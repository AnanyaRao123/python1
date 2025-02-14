import random
choices = ["rock","paper","scissor"]
user_choice = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissor)\n"))
computer_choice = random.randint(0,3)
if(user_choice>=0 and user_choice<3):
    print("User choice = ",choices[user_choice],"\nComputer choice = ",choices[computer_choice])
if(user_choice==0 and computer_choice==2):
    print("You win")
elif(computer_choice==0 and user_choice--2):
    print("You lose")
elif(user_choice>computer_choice):
    print("You win")
elif(computer_choice>user_choice):
    print("You lose")
elif(user_choice==computer_choice):
    print("It's a draw")
else:
    print("You have typed wrong number!..")