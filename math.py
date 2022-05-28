

name = input('What is your name?\n:').lower()
while name != 'kayla':
    print('You are not kayla')
    break
else:
    question = int(input('5 + 5 = '))
    if question == 10:
        print('You got it Champ!')
    else:
        print('incorrect answer')