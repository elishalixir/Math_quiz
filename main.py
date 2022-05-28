import random

number = 0
questions = {}
count = 0
trial = ''
while True:
    welcome = input("Would you like to start the Math quiz? yes/no: \n").lower()
    if welcome == 'yes':
            name = input('Choose: \n1. Easy \n2. Medium  \n3. Hard \n:').lower()
            if name == '2':
                for i in range(10):
                    int_a = random.randint(0, 10)
                    int_b = random.randint(0, 10)
                    operator = ['+', '-']
                    operator_use = random.choice(operator)
                    question = str(int_a) + '' + str(operator_use) + '' + str(int_b)
                    answer = eval(question)
                    question += ': '
                    questions.update({question: str(answer)})

                for q in questions.keys():
                    user_answer = input(q)
                    if questions.get(q) == str(user_answer):
                        count += 1
                        print('Correct!')
                    else:
                        print('Incorrect!')

                print(f'You got {count} questions right.')

    # prompt = input('would you like to play again?\n: ').lower()
            elif name== '1':
                  for i in range(10):
                    int_a = random.randint(0, 5)
                    int_b = random.randint(0, 5)
                    operator = ['+']
                    operator_use = random.choice(operator)
                    question = str(int_a) + '' + str(operator_use) + '' + str(int_b)
                    answer = eval(question)
                    question += ': '
                    questions.update({question: str(answer)})

                  for q in questions.keys():
                    user_answer = input(q)
                    if questions.get(q) == str(user_answer):
                        count += 1
                        print('Correct!')
                    else:
                        print('Incorrect!')
                    print(f'You got {count} questions right.')
            elif name== '3':
                  for i in range(10):
                    int_a = random.randint(0, 10)
                    int_b = random.randint(0, 10)
                    operator = ['+', '-', '*']
                    operator_use = random.choice(operator)
                    question = str(int_a) + '' + str(operator_use) + '' + str(int_b)
                    answer = eval(question)
                    question += ': '
                    questions.update({question: str(answer)})

                  for q in questions.keys():
                    user_answer = input(q)
                    if questions.get(q) == str(user_answer):
                        count += 1
                        print('Correct!')
                    else:
                        print('Incorrect!')
                    print(f'You got {count} questions right.')

            else:
               print('Wrong selection! Read the instruction and try again. \n')

    else:
        print('Thanks, Have a good day!')
        break

#trial = input('Would you like to try again?\nyes/no?: ')


#     quest_1 = input('3 + 2: ')
#     if quest_1 == '5':
#         number += 1
#         print("Correct!")
#     else:
#         print('Incorrect')
#         print("The correct answer is 5")
#     quest_2 = input('5 + 4: ')
#     if quest_2 == '9':
#         number += 1
#         print("Correct!")
#     else:
#         print('Incorrect')
#         print("The correct answer is 9")
#     quest_3 = input('7 + 3: ')
#     if quest_3 == '10':
#         number += 1
#         print("Correct!")
#     else:
#         print('Incorrect')
#         print("The correct answer is 10")
#
# print(f'This is the end.\n You got {number} questions correct')

