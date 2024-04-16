import random
i = input("Enter 'start' to begin: \n")
while(i != "stop" ):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = random.choice(a)
    print(b)
    i = input()
    if i==b:
        print(True)
    elif(i=="stop"):
        break
    else:
        print(False)