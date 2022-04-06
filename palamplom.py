import random
user_score=0
computer_score1=0
computer_score2=0

options=["ro","posht"]


for i in range(5):
    computer_choice1=random.choice(options)
    computer_choice2=random.choice(options)
    print("select")
    user_choice=input()

    if computer_choice1==computer_choice2 and user_choice!=computer_choice1:
        user_score+=1
    elif computer_choice1==user_choice and computer_choice2!=computer_choice1:
        computer_score2+=1
    elif computer_choice2==user_choice and computer_choice1!=computer_choice2:
        computer_score1+=1

print("user score",user_score)
print("computer1 score",computer_score1)
print("computer2 score",computer_score2)
if user_score>computer_score1 and user_score>computer_score2:
    print("user win")

elif computer_score1>user_score and computer_score1>computer_score2:
    print("computer1 win")
    
elif computer_score2>user_score and computer_score2>computer_score1:
    print("computer2 win")    
else:
    print("no winner")