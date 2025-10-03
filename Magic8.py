import random
ques = input('Question :  ')
rand_num= random.randint(1,9)
if rand_num == 1:
  print('Magic 8 Ball : Yes - definitely.')
elif rand_num == 2:
  print('Magic 8 Ball : It is decidedly so.')
elif rand_num == 3:
  print('Magic 8 Ball : Without a doubt.')
elif rand_num == 4:
  print('Magic 8 Ball : Reply hazy, try again.')
elif rand_num == 5:
  print('Magic 8 Ball : Ask again later.')
elif rand_num == 6:
  print('Magic 8 Ball : Better not tell you now.')
elif rand_num == 7:
  print('Magic 8 Ball : My sources say no.')
elif rand_num == 8:
  print('Magic 8 Ball : Very doubtful.')
elif rand_num == 9:
  print('Magic 8 Ball : Outlook not so good.')
