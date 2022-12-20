import random 

print ("Guess the number!")
while True:
    pc_number = random.randint(0, 20)
    user_number1 = int(input("enter a number between 0 to 20: "))

    if user_number1 == pc_number:
            print("You win!")
            print("You piched one number.\nThe number you picked is:", user_number1)
    else:
        if pc_number > user_number1:
            print("Go up!")
            user_number2 = int(input("enter another number: "))
        elif pc_number < user_number1:
            print("Go down!")
            user_number2 = int(input("enter another number: "))

        if user_number2 == pc_number:
            print("You win!")
            print("You picked two numbers.\nThe numbers you picked are:", user_number1, user_number2)
        else:
            if pc_number > user_number2:
                print("Go up!")
                user_number3 = int(input("enter another number: "))
            elif pc_number < user_number2:
                print("Go down!")
                user_number3 = int(input("enter another number: "))

            if user_number3 == pc_number:
                print("You win!")
                print("You picked three numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3)
            else:
                if pc_number > user_number3:
                    print("Go up!")
                    user_number4 = int(input("enter another number: "))
                elif pc_number < user_number3:
                    print("Go down!")
                    user_number4 = int(input("enter another number: "))

                if user_number4 == pc_number:
                    print("You win!")
                    print("You picked four numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4)
                else:
                    if pc_number > user_number4:
                        print("Go up!")
                        user_number5 = int(input("enter another number: "))
                    elif pc_number < user_number4:
                        print("Go down!")
                        user_number5 = int(input("enter another number: "))

                    if user_number5 == pc_number:
                        print("You win!")
                        print("You picked five numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5)
                    else:
                        if pc_number > user_number5:
                            print("Go up!")
                            user_number6 = int(input("enter another number: "))
                        elif pc_number < user_number5:
                            print("Go down!")
                            user_number6 = int(input("enter another number: "))

                        if user_number6 == pc_number:
                            print("You win!")
                            print("You picked six numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6)
                        else:
                            if pc_number > user_number6:
                                print("Go up!")
                                user_number7 = int(input("enter another number: "))
                            elif pc_number < user_number6:
                                print("Go down!")
                                user_number7 = int(input("enter another number: "))

                            if user_number7 == pc_number:
                                print("You win!")
                                print("You picked seven numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6, user_number7)
                            else:
                                if pc_number > user_number7:
                                    print("Go up!")
                                    user_number8 = int(input("enter another number: "))
                                elif pc_number < user_number7:
                                    print("Go down!")
                                    user_number8 = int(input("enter another number: "))

                                if user_number8 == pc_number:
                                    print("You win!")
                                    print("You picked eight numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6, user_number7, user_number8)
                                else:
                                    if pc_number > user_number8:
                                        print("Go up!")
                                        user_number9 = int(input("enter another number: "))
                                    elif pc_number < user_number8:
                                        print("Go down!")
                                        user_number9 = int(input("enter another number: "))
                                                
                                    if user_number9 == pc_number:
                                        print("You win!")
                                        print("You picked nine numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6, user_number7, user_number8, user_number9)
                                    else:
                                        if pc_number > user_number9:
                                            print("Go up!")
                                            user_number10 = int(input("enter another number: "))
                                        elif pc_number < user_number9:
                                            print("Go down!")
                                            user_number10 = int(input("enter another number: "))

                                        if user_number10 == pc_number:
                                            print("You win!")
                                            print("You picked ten numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6, user_number7, user_number8, user_number9, user_number10)
                                        else:
                                            if pc_number != user_number9:
                                                print("You lose!")
                                                print("You picked ten numbers.\nThe numbers you picked are:", user_number1, user_number2, user_number3, user_number4, user_number5, user_number6, user_number7, user_number8, user_number9, user_number10)