import random
import time

print("***********************************"
      "\n"
      "  Welcome To Guessing Number Game  "
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "***********************************")

unknown = int(random.randint(1,100))

guess = 7

while ( guess >= 1):

    entry = int(input("Enter Your Try Please :"))

    if(entry < unknown):
        print("It's Being Calculating...")
        time.sleep(1)
        print("Enter a Higher Number Please")
        guess -= 1
        print("{} Guess Remained".format(guess))
    elif(unknown < entry):
        print("It's Being Calculating...")
        time.sleep(1)
        print("Enter a Less Number Please")
        guess -= 1
        print("{} Guess Remained".format(guess))
    else:
        print("You Have Won ! The Unknown Number Is = {}".format(unknown))
        break

if(guess == 0):
    print("You're Out of Guess The Number Was : " + str(unknown))























