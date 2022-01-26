import random
print("Number Guessing Game(1-9)")
number = random.randint(1,9)
chance = 0
print("Guess a number(1-9)")
while chance < 5:
   guess = int(input("Enter the answer:"))

   if(guess == number):
        print("Congrats! You Won!!!")
        break

   elif(guess < number):
        print("The guess is too low than the number: ", str(guess))

   elif(guess > number):
        print("The guess is higher than the number: ", str(guess))    
   
   chance +=1

if not chance < 5:
        print("You Lose!! The answer was", str(number))
