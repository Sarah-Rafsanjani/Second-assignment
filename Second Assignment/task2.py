import random

print("Dice 🎲")
while True:
    command = input("type R to roll the dice and E to exit: ")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    if command == "e" or command == "E":
        break
    else:
        if command == "r" or command == "R":
            print(dice1)
            if dice1 == 6:
                print("six gets a double roll:")
                print(dice2)
        elif command != "r":
            print("error")