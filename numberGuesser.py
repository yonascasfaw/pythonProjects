import random

randValue = random.randint(0, 10)
print("Hello my friend,")
guess = int(input(" please enter a number between 0 and 10: "))
while guess != randValue:
    if guess > randValue:
        guess = int(input("guess lower"))
    else:
        guess = int(input("guess higher"))
print("hooray! you got it.")