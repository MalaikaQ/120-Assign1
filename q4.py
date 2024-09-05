h = int(input("What is the height of the pyramid?\n"))
if h < 0:
    exit()
if h > 9 or h < 2:
        print("PyNum cannot help you!")
        exit()
for i in range(1, h + 1):
    for j in range(1, (h + 1) - i):
        print(" ", end = " ")
    for j in range(1, i):
        print(j, end = " ")
    for j in range(i, 0, -1):
        print(j, end = " ")
    print("")

        
