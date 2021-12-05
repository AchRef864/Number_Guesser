from random import randint

CPU_X = randint(1,1000)
Your_x = 0

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

def CPU_Guess(x):
    feedback = ""
    low = 1
    high = 1000
    while feedback != "C" :
        if low != high :
            guess = randint(low ,high)
        else :
            guess = low
        feedback = input(f"Is The Number {guess} Too High Or Too Low ?   :   ")
        if feedback == "H" or feedback == "h":
            high = guess - 1
        elif feedback == "L" or feedback == "l":
            low = guess + 1
        elif feedback == "C" or feedback == "c":
            break
    print(f"I Knew It {guess} It's Obvious")
    x = guess

i = 1

while True:
        Answer = int(input("Press 1 If You Wanna Guess Press 0 To Let CPU Guess (888 To Quit): "))
        if Answer in [0,1,888]:
            if(Answer == 0):
                print("Think Of A Number Cause I Am About To Read Your Mind : ")
                print("Too High(H) Too Low(L) Correct(C)")
                CPU_Guess(Your_x)
            elif(Answer == 1):
                print("Guess My Number : ")
                print("You Will Have Some Hints ")
                USER_Guess(CPU_X,i)
            else:
                print("GoodBye")
                break
        else:
            print('That is not a valid answer .... ')


