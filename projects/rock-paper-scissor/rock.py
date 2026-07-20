"""
Project: Rock paper
"""

import random

item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both choose same = Match Tie!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer Win !!!") 
    else:
         print("Rock smashes Scissor, You Win !!!") 

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer Win !!!") 
    else:
         print("Paper covers Rock, Computer Win !!!") 


elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper, You Win !!!") 
    else:
         print("Rock smashes Scissor, Computer Win !!!") 



