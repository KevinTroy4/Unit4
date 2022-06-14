'''
The user will enter a maximum and minimum numeric value.
The computer selects a random number in the range provided by the user.
The user attempts to guess the number selected by the computer.
After each guess an appropriate output is displayed and the user is prompted to try again.
The game continues until the user guesses the correct number. The computer then displays the number of attempts to obtain the correct answer.
Make sure that your output statements and input prompts are clear, and that your game is fun to play.
You must follow all style conventions and use internal documentation to make your program easy to understand.
'''
#name of the author Kevin
#name of the program: Guessing game.py
#date of creation: 6:13:22'
#purpose of program: the purpose of this program is to input 2 numbers and have the computer 
#chose one in between, you then have to guess the number the computer chose.

import random
bob=int(input("input a number"))
foo=int(input("input a number larger than first number number"))

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between your numbers:')
car = random.randint(bob, foo)

while number_of_guesses < 10000000:
    guess = int(input())
    number_of_guesses += 1
    if guess < car:
        print('Your guess is too low')
    if guess > car:
        print('Your guess is too high')
    if guess == car:
        break
if guess == car:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(car))
#print("thank you for using the random number generator")
