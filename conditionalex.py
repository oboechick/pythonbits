left_hallway = "The user went left."
right_hallway = "The user went right."

print('Do you go left or right?')
user_input = input()

def leftRightFunction(user_input):
    if user_input == "left":
        print(left_hallway)
    elif user_input == "right":
        print(right_hallway)
    else:
        print("Please type 'left' or 'right'")



leftRightFunction(user_input)