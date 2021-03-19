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

# 3 random password
# import random
# passlen = int(input("enter the length of password:"))
# s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-="
# p = ''.join(random.sample(s, passlen))
# print(p)

# 4 cut the email
# email = input("what is your email address?:").strip()
# user_name = email[:email.index("@")]
# domain_name = email[email.index("@")+1:]
# res = f"Your uesername is '{user_name}' and your domain name is '{domain_name}'"
# print(res)

# 5 email auto send
# import smtplib
# from email.message import EmailMessage
#
# email = EmailMessage()
# email['from'] = 'xyz name'  # Person who is sending
# email['to'] = 'xyz id'  # Whom we are is sending
# email['subject'] = 'xyz subject'  # Subject of email
# email.set_content("Xyz content of email")  # content of email
# with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
#     smtp.ehlo()
# smtp.starttls()
# smtp.login("Email_id", "Password")
# smtp.send_message(email)
# print("email send")

# 6 read the PDF
# import pyttsx3, pyPDF2
# pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))
# speaker = pyttsx3.init()
# for page_num in range(pdfReader.numPages):
#     text = pdfReader.getPage(page_num).extractText()
#     speaker.say(text)
#     speaker.runAndwait()
# speaker.stop()

# 7