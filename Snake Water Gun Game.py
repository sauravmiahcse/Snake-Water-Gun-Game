import random

comp_point = 0
user_point = 0

n = int(input("How Many Times You Want To Play This Game:"))

for i in range (n):
    lst = ["s", "w", "g"]
    comp = random.choice(lst)

    print("Choose Snake (s), Water (w), Gun(g): ")
    user = input()

    if comp == "s" and user == "w":
        print("Computer Choose Snake (s)\n"
        "You Loose!")
        comp_point += 1

    elif comp == "s" and user == "g":
        print("Computer Choose Snake (s)\n"
        "You Win!")
        user_point += 1

    elif comp == "s" and user == "s":
        print("Computer Choose Snake (s)\n"
        "Same!")

    elif comp == "w" and user == "g":
        print("Computer Choose Water (w)\n"
        "You Loose!")
        comp_point += 1

    elif comp == "w" and user == "s":
        print("Computer Choose Water (w)\n"
        "You Win!")
        user_point += 1

    elif comp == "w" and user == "w":
        print("Computer Choose Water (w)\n"
        "Same!")

    elif comp == "g" and user == "s":
        print("Computer Choose Gun (g)\n"
        "You Loose!")
        comp_point += 1

    elif comp == "g" and user == "w":
        print("Computer Choose Gun (g)\n"
        "You Win!")
        user_point += 1

    elif comp == "g" and user == "g":
        print("Computer Choose Gun (g)\n"
        "Same!")

    else:
        print("Wrong Choice!")


if comp_point > user_point:
    print("Computer:", comp_point, "You:", user_point,
    "\nOops! You Loose The Game!")
elif comp_point < user_point:
    print("Computer:", comp_point, "You:", user_point,
    "\nCongratulations! You Win The Game!")

else:
    print("Computer:", comp_point, "You:", user_point,
    "\nGame Draw!")

