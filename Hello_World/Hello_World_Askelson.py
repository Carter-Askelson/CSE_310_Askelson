import sys

def main():
    while True:
        print()
        answer = input("Would you like to print 'Hello World!'? (y/n):")
        answer = answer.lower()
        print()
        if answer == "y" or answer == "yes":
            print("Hello World!")
            print()
            restart()
        elif answer == "n" or answer == "no":
            print("Script terminating. Goodbye.")
            sys.exit()
        else:
            print("Invalid Input.")

def restart():
    while True:
        restart = input("Would you like to run the program again? (y/n): ")
        restart = restart.lower()
        print()
        if restart == "y" or restart == "yes":
            main()
        elif restart == "n" or restart == "no":
            print("Script terminating. Goodbye.")
            sys.exit()
        else:
            print("Invalid Input.")

main()