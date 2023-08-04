import Shuffle_Ball as S
import TicTacToe as T
import Number_Range as C


def main():
    print("-----------------------------------------------------------------")
    print("                              Game                               ")
    print("-----------------------------------------------------------------")
    print("                     Choose from the option:")
    print("                       1. Tic-Tac_Toe")
    print("                       2. Shuffle Ball")
    print("                       3. Number Range")
    print("-----------------------------------------------------------------\n\n")
    enter()


def choice(inputs):
    if inputs == 1:
        T.main()
    elif inputs == 2:   
        S.main()
    elif inputs == 3:   
        C.main()


def enter():
    try:
        inputs = int(input("Enter your choice : "))
        choice(inputs)
    except:
        print("Try Again")

if __name__ == "__main__":
    main()