
n = input("How many numbers do you want to check?\n")
count = 0
for i in range(int(n)):
    number = int(input("Enter a positive integer:\n"))
    j = 2
    if number > 1:
        while j < number:
            if number % j == 0:
                break
            j = j + 1
        else:
            Prime = True
            if Prime == True:
                count += 1
            print(number, "is a prime number.")
    while number < 0:
        print("PrimeFinder ignores negative numbers!")
        number = int(input("Enter a positive integer:\n"))
        j = 2
        if number > 1:
            while j < number:
                if number % j == 0:
                    break
                j = j + 1
            else:
                Prime = True
                if Prime == True:
                    count += 1
                print(number, "is a prime number.")
print("Total prime numbers:", count)

                    

                    
