total = 0

print("➕ Addition Problem")

while True:
    number = input("put numbers to calculate their addition. Type \"exit\" to give out the result: ")
    if number != "exit":
        total += int(number)
    elif number == "exit":
        print("This is your final result:", total)