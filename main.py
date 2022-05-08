import random

user_wins = 0
computer_wins = 0

opcje = ["kamien", "papier", "nozyce"]

while True:
    user_input = input("Napisz Kamien/Papier/Nozyce lub Q aby wyjść: ").lower()
    if user_input == "q":
        break


    if user_input not in opcje:
        continue

    random_number = random.randint(0,2)
    # kamien: 0, papier: 1, nozyce: 2
    computer_pick = opcje[random_number]
    print("Twoj stary wybrał", computer_pick + ".")

    if user_input == "kamien" and computer_pick == "nozyce":
        print("Ojebales starego!")
        user_wins += 1

    elif user_input == "papier" and computer_pick == "kamien":
        print("Ojebales starego!")
        user_wins += 1

    elif user_input == "nozyce" and computer_pick == "papier":
        print("Ojebales starego!")
        user_wins += 1

    else:
        print("Przejebałeś ze starym!")
        computer_wins += 1

print("Wygrałeś", user_wins, "razy.")
print("Stary wygrał", computer_wins, "razy.")
print("Naura!")
