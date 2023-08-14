print(
    """
████████████████████████████████████████████████
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ████████████████████████████████████    ██
██                ██        ██                ██
████████████████████  ████  ████████████████████
██    ██▓▓▓▓▓▓▓▓▓▓██  ▓▓▓▓  ██▓▓▓▓▓▓▓▓▓▓██    ██
██    ██████████████        ██████████████    ██
██                  ████████                  ██
██                                            ██
████████████████████████████████████████████████
"""
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
direction = input("Would you like to go left or right?\n").lower()

if direction == "left":
    swim = input(
        "You go to the left and come to a dock. There is an island out in the middle of the lake. Type 'Wait' to wait, or 'Swim' to swim across.\n"
    )
    if swim == "wait":
        door = input(
            "You notice there is a house with 3 doors. One red, one yellow, and one blue. Which do you choose?\n"
        )
        if door == "red":
            print("You enter a room full of fire and die. Game over.")
        elif door == "yellow":
            print("You find a pot of gold! You win!")
        else:
            print(
                "A wizard greets you, to tell you that you've lost. He vaporizes you with his electricity spell. Game over."
            )
    elif swim == "swim":
        print("You try to swim across, but you drown and die. Game over.")
else:
    print("You go to the right and are eaten by a dragon. Game over.")
