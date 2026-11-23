import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
print()

while lower_bound >= upper_bound:
    print("Invalid input, please try again")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    print()

secret_number = random.randint(lower_bound,upper_bound)
print()

num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

while num_guess < lower_bound or num_guess > upper_bound:
    print("Invalid entry, please try again")
    print()
    num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

while secret_number != num_guess:
    if num_guess > secret_number:
        print("Nope, too high!")
        num_guess = int(input("Guess another number: "))
        print()

        while num_guess < lower_bound or num_guess > upper_bound:
            print("Invalid entry, please try again")
            num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            print()

    else:
        print("Nope, too low!")
        num_guess = int(input("Guess another number: "))
        print()
        while num_guess < lower_bound or num_guess > upper_bound:
            print("Invalid entry, please try again")
            num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            print()
print("You got it!")
print("Want to play again?")
answer = input()
print()

while answer.lower() == "yes":
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    print()

    while lower_bound >= upper_bound:
        print("Invalid input, please try again")
        print()
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        print()

    secret_number = random.randint(lower_bound, upper_bound)
    print()

    num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

    while num_guess < lower_bound or num_guess > upper_bound:
        print("Invalid entry, please try again")
        print()
        num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

    while secret_number != num_guess:
        if num_guess > secret_number:
            print("Nope, too high!")
            num_guess = int(input("Guess another number: "))
            print()

            while num_guess < lower_bound or num_guess > upper_bound:
                print("Invalid entry, please try again")
                num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
                print()

        else:
            print("Nope, too low!")
            num_guess = int(input("Guess another number: "))
            print()
            while num_guess < lower_bound or num_guess > upper_bound:
                print("Invalid entry, please try again")
                num_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
                print()
    print("You got it!")
    print("Want to play again?")
    answer = input()
    print()

print("Goodbye!")
