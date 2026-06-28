direction = input("What direction do you want to go: ") 
if direction == "left": 
      action = input("Do you want to swim or wait: ")
      if action =="swim":
            print("You found treasure!")
      else:
             print("Nothing happened!")
else:
    print("You fell in a pit!")