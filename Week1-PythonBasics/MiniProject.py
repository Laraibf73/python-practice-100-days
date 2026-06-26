'''
Rock Paper Scissors Game

Features:

User vs Computer
Score tracking
 
***Rules:
        Rock beats Scissors
        Scissors beats Paper
        Paper beats Rock
'''

import random

selection = {
    "rock": "r",
    "paper": "p",
    "scissor": "s"
}
computer=random.choice(list(selection.values()))
user_score=0
comp_score=0

tries=3
i=0
print("=============================")
print(" Rock Paper Scissors Game")
print("=============================")

while i<3:
    user=input("Enter r for a rock. p for a paper, s for a scissor ")
    if (user=='r' and computer=='s') or(user=='p' and computer=='r') or (user=='s' and computer=='p'):
       # print("user score",user,"->",computer)
        user_score+=1
        i+=1
    elif(computer=='s'and user=='p' ) or(computer=='p'and user=='r') or (user=='s' and computer=='r'):
       # print("user score",user,"->",computer)
        comp_score+=1
        i+=1
    else:
        #print("user score",user,"->",computer)
        i+=1
    print("--------------------------------------")
    print("User Scores = ",user_score)
    print("Computer Scores = ",comp_score)
    print("--------------------------------------")


if(user_score>comp_score):
    print("\t\tUser Won! \n Score: ",user_score)
elif (user_score<comp_score):
    print("\t\tComputer Won. You better Try next time! \n Score: ",comp_score)
else:
    print("\t\tD R A W !!")

