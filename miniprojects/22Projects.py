# -*- coding: utf-8 -*-

# 1 dice
# import random
# while int(input('Press 1 to roll the dice or 0 to exit:\n')): print(random.randint(1, 6))

# 2 Game of scissors paper rock
# import random
# choices = ["Rock", "Paper", "Scissors"]
# computer = random.choice(choices)
# player = False
# cpu_score = 0
# player_score = 0
# while True:
#     player = input("Rock,Paper or Scissors ?").capitalize()
#     # 判断游戏者和电脑的选择
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#             cpu_score+=1
#         else:
#             print("You win!", player, "covers", computer)
#             player_score+=1
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "covers", player)
#             cpu_score+=1
#         else:
#             print("You win!", player, "covers", computer)
#             player_score+=1
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose!", computer, "covers", player)
#             cpu_score+=1
#         else:
#             print("You win!", player, "covers", computer)
#             player_score+=1
#     elif player =='E':
#         print('Final Scores:')
#         print(f'CPU:{cpu_score}')
#         print(f'Player:{player_score}')
#         break
#     else:
#         print("That's not a valid play.Check your spelling!")
#     computer = random.choice(choices)

