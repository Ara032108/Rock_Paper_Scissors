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

game = [rock, paper, scissors]
import random

computer = random.choice(game)
player = random.randint(0,2)
player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : ")
def rps(player, computer):
    if player == '0':
      print(rock) 
    elif player == '1':
      print(paper)
    else:
      print(scissors)

    print("Computer Choose:",computer)
    if player == '0':
      if computer == rock:
        print("Its a tie")
      elif computer == paper:
        print("You Lose")
      else:
        print("You Win")
    elif player == '1':
      if computer == rock:
        print("You Win")
      elif computer == paper:
        print("Its a tie")
      else:
        print("You lose")
    else:
      if computer == rock:
        print("You lose")
      elif computer == paper:
        print("You win")
      else:
        print("Its a tie")
  
rps(player, computer)