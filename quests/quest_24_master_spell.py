def ask_for_age():
    age = int(input("Enter your age: "))
    return age

def can_they_vote(age):
    if age >= 18:
        print(f"You are {age} years old. You CAN vote!")
    else:
        print(f"You are {age} years old. You CANNOT vote yet.")

age = ask_for_age()
can_they_vote(age)