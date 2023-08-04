from random import shuffle
import Mini_Game as G

count = 0
ball = ['|_|','|O|','|_|']

def main():
    print(*ball)
    enter(count)

def enter(count):
    n = int(input("enter choice : "))
    if n == 1 or n == 2 or n == 3 :
        inputs(n)
    else:
        enter(count)

def inputs(n):
    global ball,count

    shuffle(ball)
    if (ball[n-1] == '|O|'):
        print(*ball)
        print("Winner")
        count = count + 1
        print("score = ",count)
        shuffle(ball)
        enter(count)
    else:
        print(*ball)
        print("Game Over")
        print("score = ",count)
        print("\n")
        reset

def reset():
    print("-----------------------------------------------------------------")
    print("                            Reset:                               ")
    print("-----------------------------------------------------------------")
    print("                     Choose from the option:")
    print("                       1. Play Again")
    print("                       2. Start Menu")
    print("-----------------------------------------------------------------\n")
    Choose_reset = int(input("Your choice : "))
    if Choose_reset == 1:
        main()
    elif Choose_reset == 2:
        G.main()

if __name__ == '__main__':
    main()