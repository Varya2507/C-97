import random


gold= random.randint(1,9)
silver= 0

print("guess a random number from 1 to 9")
while silver<5:
    good= int( input("Enter the number you thought of"))
    if good==gold:
        print("Congratulations! You won!")
        break
    elif good<gold:
        print("Your guess was too low. Guess a number higher", good)
    else:
        print("Your guess was too high. Guess a number lower", good)
    silver+=1


if not silver<5:
    print("Sorry buddy! You have lost, the number is ", gold)    