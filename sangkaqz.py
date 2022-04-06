import random
user_score=0
computer_score=0
options=["rock","paper","scissor"]

for i in range(5):

    computer_choice=random.choice(options)
    print("select")
    user_choice=input()

    if user_choice=="paper" and computer_choice=="rock":
        user_score+=1
    elif user_choice=="paper" and computer_choice=="scissor":
        computer_score+=1
    elif user_choice=="paper" and computer_choice=="paper":
        user_score=user_score
        computer_score=computer_score

    elif user_choice=="rock" and computer_score=="paper":
        computer_score+=1
    elif user_choice=="rock" and computer_score=="scissor":
        user_score+=1         
    elif user_choice=="rock" and computer_score=="rock":
        user_score=user_score
        computer_score=computer_score

    elif user_choice=="scissor" and computer_choice=="rock":
        computer_score+=1
    elif user_choice=="scissor" and computer_choice=="paper":
        user_score+=1
    elif user_choice=="scissor" and computer_choice=="scissor":
        user_score=user_score
        computer_score=computer_score

print("user score",user_score)
print("computer score",computer_score)
if user_score>computer_score:
    print("user win")
elif computer_score>user_score:
    print("computer win")
else:
    print("no winner")        