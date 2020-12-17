import time
import random


villan = ["dragon", "gorgon", "pirate", "troll", "monster"]
enemy = random.choice(villan)


def print_pause(message):
    print(message)
    time.sleep(2)


# Description part for the player
def inrto():
    global enemy
    enemy = random.choice(villan)
    global weapon
    weapon = []
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                "and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty"
                "(but not every effective) dagger.\n")


# when player knock at the door without weapon
def knock_the_door():
    print_pause("You approch the door of the house.\n")
    print_pause("You are about to knock when the door opens"
                f" and out steps a {enemy}.\n")
    print_pause(f"Eep! This is the {enemy}'s house!\n")
    print_pause(f"The {enemy} attacks you!\n")


# when you peer into cave 1st time
def cave():
    print_pause("Yo peer coutiously into the cave.\n")
    print_pause("It turns out to be a very small cave.\n")
    print_pause("Your eye catches a glint of metal behind a rock.\n")
    print_pause("You have found the megical sword of the Ogoroth!\n")
    print_pause("You discard your silly old dagger"
                " and takes the sword with you.\n")
    print_pause("You walk back to the field.\n")
    weapon.append("sword")


# situation at cave for player when player got the weapon or not
def empty_cave():
    if 'sword' not in weapon:
        cave()
    else:
        print_pause("You peer cuatiously into the cave.\n")
        print_pause("You've been here, and gotten all the good stuff."
                    "It's just an empty cave now.\n")


# situation at enemy house when player has weapon or not
def house_siuation():
    if 'sword' in weapon:
        knock_the_door()

    else:
        knock_the_door()
        print_pause("You feel bit under-pressured for this,"
                    "what only having a tiny dagger.\n")


# situation when player has to choose if player wants to fight or not?
def fight():
    fight_choice = input("What would you like to do?"
                         "(1) Fight or (2) Run away ?\n")
    if fight_choice == '1':
        if 'sword' in weapon:
            print_pause(f"As the {enemy} moves to attack,"
                        f"you unsheath your new sword.\n")
            print_pause(f"The sword of the Ogoroth shines brightly in your"
                        "hand as you brace yourself for the attack.\n")
            print_pause(f"But the {enemy} takes a one look at"
                        "your new shiny toy and runs away!\n")
            print_pause(f"You have rid the town of {enemy}."
                        "You are victorius!\n")

        else:
            print_pause("You do your best...\n")
            print_pause(f"but your dagger is no match for {enemy}.\n")
            print_pause("You have been defeated!")

    elif fight_choice == '2':
        print_pause("You run back to the field. Luckily,"
                    " you don't seem to have been followed.\n")
        game()

    else:
        print_pause("Enter valid input.\n")
        fight()


# If player wants to play again or not??
def play_game_again():
    play_again = input("Would you like to play again??"
                       "Say yes or no?\n") .lower()
    if "yes" in play_again:
        print_pause("Excellent!! Restarting the game ...")
        inrto()
        game()

    elif "no" in play_again:
        print_pause("Thank you for playing. See you next time!!\n")

    else:
        print_pause("Enter valid input\n")
        play_game_again()


# Here playes gets to choose what they wants to do for the game?
def game():
    # weapon = []
    game_choice = input("Enter 1 to knock on the door of the house.\n"
                        "Enter 2 to peer into the cave.\n"
                        "What would you like to do?\n"
                        "(Please enter 1 or 2?)\n")
    if game_choice == "1":
        house_siuation()
        fight()
        play_game_again()

    elif game_choice == "2":
        empty_cave()
        game()
    else:
        print_pause("Enter valid input.\n")
        game()


def adventure_game():
    inrto()
    game()


adventure_game()