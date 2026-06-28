def forest():
    print("You entered a dark forest.")
    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        print("You found a treasure! You win!")
    elif choice == "right":
        print("A dragon appears. Game over!")
    else:
        print("Invalid choice.")

print("Welcome to the Adventure Game!")
forest()