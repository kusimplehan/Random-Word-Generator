import random
type_style = input("single or multi : ")
if type_style=="single":
    n = input("Type a lettle : ")
    while (type_style != "stop"):
        print(n,"\n")
        y = input()
        if y==n:
            print(True)
        else:
            print(False)

elif type_style=="multi":

    i = input("Enter 'start' to begin: \n")
    while(i != "stop" ):
        a = "abcdefghijklmnopqrstuvwxyz"
        b = random.choice(a)
        print(b,"\n")
        i = input()
        if i==b:
            print(True)
        elif(i=="stop"):
            break
        else:
            print(False)