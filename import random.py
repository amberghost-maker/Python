import random
class FuritQuiz:
    def __init__ (self):
        self.furits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'bananna' : 'yellow'}
    def quiz(self):
         while (True):
             furit, colour = random.choice(list(self.furits.items()))
             print("What is the colour of{}".format(furit))
             user_answer = input()
             if (user_answer.lower() == colour):
                 print('correct answer')
             else:
              print('wrong answer')
             option = int(input('enter 0, if u want to play again otherwise press 1'))
             if (option):
                break
print('welcome to the fruit Quiz')
fq = FuritQuiz()
fq.quiz()