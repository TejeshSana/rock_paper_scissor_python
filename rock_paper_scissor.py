import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper ='''
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_images=[rock,paper,scissor]

user_choice=int(input("ENTER YOUR CHOICE 😇 Type 0 for Rock,1 for Paper,2 for Scissor : "))

if user_choice>=3 or user_choice<0:
    print("ERROR!!! ⚠️  You choose a wrong number ")

else:
  print(game_images[user_choice])

  computer_choice=random.randint(0,2)
  print("Computer choice is : ")
  print(game_images[computer_choice])

  if user_choice==0 and computer_choice==2:  
    print("You win!!! 😊")
  elif computer_choice==0 and user_choice==2:  
    print("Computer wins!!! 😵")
  elif computer_choice > user_choice:  
    print("Computer wins!!! 😵")
  elif user_choice>computer_choice:  
    print("You win!!!  😊")
  elif computer_choice==user_choice:
    print("It's a tie!!!  😶 ")





