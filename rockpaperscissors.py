import random
list1 = ["Rock", "Paper", "Scissors"]
rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Player Choice Area
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
if player_choice >= 0 and player_choice <= 2:
    player_list_choice = list1[int(player_choice)]
    print(f"Player chose: {player_list_choice}.")
else:
    quit(print("IMPROPER INPUT")) 
if player_choice == 0:
    print(rock1)
elif player_choice == 1:
    print(paper1)
elif player_choice == 2:
    print(scissors1)

#Computer Choice Area
computer_choice = random.randint(0, 2)
computer_list_choice = list1[computer_choice]
print(f"Computer chose: {computer_list_choice}.")
if computer_choice == 0:
    print(rock1)
elif computer_choice == 1:
    print(paper1)
elif computer_choice == 2:
    print(scissors1)
#Game Results Area
if player_choice == 0 and computer_choice == 1:
    print("You lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 0 and computer_choice == 0:
    print("Tie game!")
if player_choice == 1 and computer_choice == 1:
    print("Tie game!")
elif player_choice == 1 and computer_choice == 2:
    print("You lose!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
if player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 2 and computer_choice == 2:
    print("Tie game!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")

