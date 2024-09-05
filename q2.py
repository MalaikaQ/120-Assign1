
num_oper = int(input("Hi, how many operations do you want MagiCal to perform?\n"))
for i in range(num_oper):
        operator = input("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")
        if operator == "1":
            first_num = int(input("Enter the first number in the interval of [0,100]:\n"))
            second_num = int(input("Enter the second number in the interval of [0,100]:\n"))
            if 0 <= first_num <= 100 and 0 <= second_num <= 100:
                print(str(first_num), "+", str(second_num), "=", int(first_num) + int(second_num))
            else:
                print("Magic calculator can not perform your operation!")
        if operator == "2":
            first_num = int(input("Enter the first number in the interval of [0,100]:\n"))
            second_num = int(input("Enter the second number in the interval of [0,100]:\n"))
            if 0 <= first_num <= 100 and 0 <= second_num <= 100:
                print(str(first_num), "-", str(second_num), "=", int(first_num) - int(second_num))
            else:
                print("Magic calculator can not perform your operation!")
        if operator == "3":
            first_num = int(input("Enter the first number in the interval of [0,100]:\n"))
            second_num = int(input("Enter the second number in the interval of [0,100]:\n"))
            if 0 <= first_num <= 100 and 0 <= second_num <= 100:
                print(str(first_num), "*", str(second_num), "=", int(first_num) * int(second_num))
            else:
                print("Magic calculator can not perform your operation!")
        if operator == "4":
            first_num = int(input("Enter the first number in the interval of [0,100]:\n"))
            second_num = int(input("Enter the second number in the interval of [0,100]:\n"))
            if second_num == 0:
                print("The denominator cannot be 0.")
            if 0 <= first_num <= 100 and 0 < second_num <= 100:
                print(str(first_num), "/", str(second_num), "=", int(first_num) / int(second_num))
            if first_num < 0 or first_num > 100:
                print("Magic calculator can not perform your operation!")
            if second_num < 0 or second_num > 100:
                print("Magic calculator can not perform your operation!")
        if operator > "4" or operator < "0":
            print("Invalid input!")