import random
nums=random.randint(0,9)
#print(nums)
for i in range(0,3):
 print('Total chance :' +str(3-i))
 usernum=int(input('Guess any number between 0 to 9: '))
 if(usernum>=0 and usernum<=9):
    if(nums==usernum):
       print('Cool!!! You guessed it correctly!!')
       break
    elif(nums>=usernum):
       print('Oops your guess is minimum than actual number')
    elif(nums<=usernum):
       print('Oops your guess is maximum than actual number')
    else:
       print('Invaild content')
 else:
  print('Its out of range')
  break
print('Thanks for guess your buddy!!')
