tries = 3
guess = 0

while guess != 6 and tries > 0:
  guess = int(input("guess the number : "))
  tries = tries - 1
  if guess != 6:
      print(f'you have left {tries} chances')
  elif guess !=6 and tries == 0:
      print(f'No chances are left.')
  else:
      print('you got it!')
