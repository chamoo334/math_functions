# TODO: make GUI and send to Landon
import random

MAX = 9999
MIN = 0
score = 0
attempts = 0

def explain(num):
    quotient = str(int(num / 2))
    product = str(int(quotient) * 2)
    difference = str(num - int(product))

    guess_quot = input("What is the quotient of "+str(num)+" % 2: ")

    if guess_quot == quotient:
        guess_prod = input("Correct. Now enter the product of "+quotient+" and 2: ")
    else:
        print("Incorrect - "+str(num)+" % 2 = "+quotient+".")
        guess_prod = input("What is the product of "+quotient+" and 2: ")

    if guess_prod == product:
        guess_diff = input("Correct. Now subtract "+product+" from "+str(num)+": ")
    else:
        print("Incorrect - "+str(num)+" - "+quotient+" = "+difference+".")
        guess_diff = input("Now subtract "+product+" from "+str(num)+": ")

    if guess_diff == difference and difference == "1":
        print("Correct!"+difference+" is not divisible by two, so it is odd.")
    elif guess_diff == difference and difference == "0":
        print("Correct!"+difference+"  is divisible by two, so it is even.")
    elif guess_diff != difference and difference == "1":
        print("The remainder of "+str(num)+" % 2 is "+difference+ ". This number is not divisible by two, so it is odd.")
    else:
        print("he remainder of "+str(num)+" % 2 is "+difference+ ". This number is divisible by two, so it is even.")

def guess_odd():
    value = str(random.randint(MIN,MAX))
    rmndr = int(value) % 2
    
    guess = input("Is "+value+" an odd number (y or n): ")
    if rmndr==1 and guess=="y":
        correct = True
        print("Correct! "+value+" is an odd number!")
    elif rmndr==0 and guess=="n":
        correct = True
        print("Correct! "+value+" is an even number!")
    else:
        correct = False
        if input("Would you like an explanation (y or n): ") == "y":
            explain(int(value))

    if correct:
        return 1
    return 0





while True:
    results = guess_odd()
    attempts += 1
    score += results
    play = input("Enter 1 to continue: ")
    if play != "1":
        grade = str((score/attempts)*100)
        print("You got "+grade+"% correct! See ya next time!")
        break