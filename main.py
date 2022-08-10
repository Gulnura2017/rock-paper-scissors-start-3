rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇
my_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_chose = random.randint(0, 2) 
game_list = [rock, paper, scissors]
print(game_list[my_chose])
print("Computer chose:") 
print(game_list[computer_chose])
if my_chose >= 3 or my_chose < 0:
  print("You chose the wrong number, you loose")
 
if my_chose == 0:
  if computer_chose ==0:
    print("Fair")
  elif computer_chose == 1:
    print("You loose")
  elif computer_chose == 2:
    print("Congratulations! You winn!")
if my_chose == 1:
  if computer_chose ==0:
    print("Congratulations! You winn!")
  elif computer_chose == 1:
    print("Fair")
  elif computer_chose == 2:
    print("You loose")
if my_chose == 2:
  if computer_chose ==0:
    print("You loose")
  elif computer_chose == 1:
    print("Congratulations! You winn!")
  elif computer_chose == 2:
    print("Fair")

    



    




