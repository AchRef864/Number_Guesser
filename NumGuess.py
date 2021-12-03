from random import randint

#Your_X = int(input("Set The Number For The Computer To Guess : "))
CPU_X = randint(1,1000)

def Odd(x):
    if(x == 1):
        return "Odd"
    else:
        if(x%2==0):
            return "Even"
        else:
            return "Odd"

def interval1(x):
    a = "1"
    b = "1"
    c = len(str(x))
    for i in range(c-1):
        a += "0"
    for i in range(c):
        b += "0"
    return f"[{a} .. {b}]"

def interval2(x):
    a = x - 10
    b = x + 10
    return f"[{a} .. {b}]"

def USER_Guess(x,i):
    hints = ["The Number Between 1 and 1000",f"The Number Conains Only {len(str(x))} Digits",f"the Number Chosen Is An {Odd(x)} Number",f"The Number Is In The Interval Of {interval1(x)}",f"The Number Is In The Interval Of {interval2(x)}"]
    your_guess = int(input(f"Guess The Number : "))
    if (your_guess == x):
        print(f"Congrats {your_guess} Is The Correct Answer")
    elif (your_guess > x) :
        print(f"{your_guess} Is Higher .......... ")
        if i > 0 and i <= len(hints):
            print(hints[i-1])
            print(f"You Have Only {(len(hints))-i} Hints Left")
        else:
            print("No Hints Left")
        USER_Guess(x,i+1)
    elif (your_guess < x) :
        print(f"{your_guess} Is Lower ........... ")
        if i > 0 and i <= len(hints):
            print(hints[i-1])
            print(f"You Have Only {(len(hints))-i} Hints Left")
        else:
            print("No Hints Left")
        USER_Guess(x,i+1)

i = 1
USER_Guess(CPU_X,i)