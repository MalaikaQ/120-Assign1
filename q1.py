talk = input("Hi, this is Pchatbot, can I talk to you?\n")
if talk == "N" or talk == "n":
        print("Okay! Talk to you soon!")
if talk == "Y" or talk == "y":
    name = input("What is your name?\n")
    print("Nice to meet you, " + name + ".")
    hru = input("How are you doing today?\n")
    if hru == "Bad" or hru == "Not Okay" or hru == "I'm not feeling good":
        print("Have some time to yourself to recharge!")
        age = int(input("How old are you?\n"))
        print("Still taking the bus!")
    elif hru == "Good" or hru == "I'm great" or hru == "I'm good" or hru == "Fine":
        print("I'm glad you're feeling well, " + name + ".")
        age = int(input("How old are you?\n"))
        if age > 18:
            print("You are ready to drive.")
        if age <= 18:
            print("Still taking the bus!")
    else:
        print("I see!")
        age = int(input("How old are you?\n"))
        print("Still taking the bus!")
        
    
    