import random

cnt = 0
print("Hello! What is your name?")
name = input()
number = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

while cnt < 6:
    print('Take a guess')
    guess = input()
    guess = int(guess)
    cnt += 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high")    

    if guess == number:
        break

if guess == number:
    cnt = str(cnt)
    print("Good job" + name + " ! You guessed my number in " + cnt + " guesses!")  

if guess != number:
    number = str(number)          
    print("Nope. Number i was thinking was " + number)