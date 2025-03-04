number = int(input("Enter your number: "))

if number <= 3:
    print("It must be higher than 3!")
else:
    if number % 2 == 0: 
        print("The even numbers from 2 to", number, "are:")
        for i in range(2, number + 1, 2):
            print(i)
    else:  
        print("The odd numbers from 1 to", number, "are:")
        for i in range(1, number + 1, 2):
            print(i)