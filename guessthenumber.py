import random
random_number=random.randint(1,10)
guess=0
while(guess!=random_number):
    guess=int(input(f"enter the random number between 1 and 10:"))
    if(guess<random_number):
        print("Sorry Guess Again Too Low.")
    elif(guess>random_number):
         print("Sorry Guess Again Too high.")
print("yay,congrats you have guessed the number correctly!!")