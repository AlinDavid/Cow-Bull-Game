import random


def compare_numbers(number, user_guess):
    cowbull = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


if __name__ == "__main__":
    playing = True
    number = str(random.randint(0, 9999))
    print(number)
    guesses = 0

    while playing:
        user_guess = input("What number do you think it is?: (Type exit if you want to quit)")
        if user_guess.casefold() == "exit":
            break
        cowbullcount = compare_numbers(number, user_guess)
        guesses += 1

        print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1] == 4:
            playing = False
            print("You won the game after " + str(guesses) + " tries " + "! The number was "+str(number))
            break
        else:
            print("Your guess isn't quite right, try again.")
