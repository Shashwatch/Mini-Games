import random
import Mini_Game as G

score = 0
choice = 0
Low = 0
High = 0


def main():
    print("-----------------------------------------------------------------")
    print("                       Choose difficulty:                        ")
    print("-----------------------------------------------------------------")
    print("                     Choose from the option:")
    print("                       1. Easy")
    print("                       2. Medium")
    print("                       3. Hard")
    print("-----------------------------------------------------------------\n\n")
    
    global choice
    choice = int(input("Choice: "))
    print("\n")
    game()

def game():
    global Low, High, score

    if choice == 1:
        Low = 0
        High = 20
    elif choice == 2:
        Low = 0
        High = 1000
    elif choice == 3:
        Low = 0
        High = 10000

    range_game()

def range_game():
    global score

    print("Select a 10 digit range between ", Low, " and ", High, ":")
    In_Low = int(input("Low : "))
    In_High = int(input("High : "))

    if In_High - In_Low == 9:
        random_num = randomize(Low, High)
        print("Random number:", random_num)

        if In_Low <= random_num <= In_High:
            print("\nWinner!!")
            score += 1
            print("Score = ", score)
        else:
            print("\nGame Over!!")
            print("Score = ", score)
            print("\n\n")
            reset()
    else:
        print("Select correct Range !!")
        range_game()

def randomize(Low, High):
    return random.randint(Low, High)

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

if __name__ == "__main__":
    main()