import time
import random


def print_pause(statement):
    print(statement)
    time.sleep(2)


def intro():
    print_pause("In a realm known as Glenoruso, the Shielded Expanse, "
                "a warrior is determined to find the last dragon.")
    print_pause("In order to rescue Dragonite..")
    print_pause("You must find three rare elements.")
    print_pause("1. Rare Plant")
    print_pause("2. Rare Animal")
    print_pause("3. Rare Sword")


def rescue_dragonite(items, plant, animal):
    print_pause("Which rare element you want to find?")
    element = input("(1 or 2 or 3)\n").lower()
    if element == '1':
        rare_plant(items, plant, animal)
    elif element == '2':
        rare_animal(items, plant, animal)
    elif element == '3':
        rare_sword(items, plant, animal)
    else:
        print_pause("It's an unwanted element")
        rescue_dragonite(items, plant, animal)


def rare_plant(items, plant, animal):
    if plant in items:
        print_pause("You have successfully found the rare plant.")
        check_elements(items, plant, animal)
    else:
        print_pause("Finding the rare plant journey has begun\n")
        print_pause("When winter daylight was diminished")
        print_pause("and nights were long,")
        print_pause("there are variety of plants in your surroundings,")
        print_pause("suddenly a " + plant + " has catched your eyes.\n")
        print_pause("Will you pick it? (Yes or No)")
        valid_input('plant', items, plant, animal)


def rare_animal(items, plant, animal):
    if animal in items:
        print_pause("You have successfully found the rare animal.")
        check_elements(items, plant, animal)
    else:
        print_pause("Finding the rare animal journey has begun\n")
        print_pause("When walking on a dark road,")
        print_pause("terrible sounds come from anonymous sources.")
        print_pause("You notice that you only have two choices:\n")
        print_pause("1. Following the sound.")
        print_pause("2. Continue walking on your path.\n")
        print_pause("What will you choose? (1 or 2)")
        valid_input('animal', items, plant, animal)


def valid_input(element, items, plant, animal):
    if element == 'plant':
        while True:
            pick_plant = input().lower()
            if pick_plant == 'yes':
                print_pause("Yay! It turns out to be a key")
                print_pause("for when finding the rare sword,")
                print_pause("an old man will help you through it.")
                items.append(plant)
                check_elements(items, plant, animal)
                break
            elif pick_plant == 'no':
                print_pause("Wise choice, it could be a poisonous plant.")
                check_elements(items, plant, animal)
                break
            else:
                print_pause("Will you pick it? (Yes or No)")
    elif element == 'animal':
        while True:
            choice = input().lower()
            if choice == '1':
                print_pause("You chose to follow the sound..")
                print_pause("It was a trap from dragonite guards!")
                print_pause("You have been caught immediately!")
                check_elements(items, plant, animal)
                break
            elif choice == '2':
                print_pause("You continued walking in the peaceful way..")
                print_pause("out of nowhere a " + animal + " has appeard")
                print_pause("and is walking by your side!")
                items.append(animal)
                check_elements(items, plant, animal)
                break
            else:
                print_pause("What will you choose? (1 or 2)")


def rare_sword(items, plant, animal):
    if 'Rare Sword' in items:
        print_pause("You have successfully found the rare sword.")
        check_elements(items, plant, animal)
    else:
        print_pause("Finding the rare sword journey has begun\n")
        if plant in items:
            print_pause("An old man approached you and said:")
            print_pause("You have a powerful key in your hand!")
            print_pause("On your right is a small cave with a treasure chest.")
            print_pause("Open it and you will find the rare sword you need.\n")
            print_pause("You thank this old man for his valuable advice")
            print_pause("and take a step towards your goal.")
            print_pause("After entering the cave,")
            print_pause("your eyes noticed the chest behind the stone,")
            print_pause("you opened it and found the sword there!")
            items.append('Rare Sword')
            check_elements(items, plant, animal)
        else:
            print_pause("Leading to nowhere,")
            print_pause("this road has no use")
            print_pause("for everyone who seeks a destination..")
            print_pause("The forest, you realized,")
            print_pause("was home to many wild creatures.")
            print_pause("When you saw this shadowy figure")
            print_pause("which appeard to be a bear!")
            print_pause("you ran towards the cave to hide from it.")
            print_pause("After entering the cave..")
            print_pause("your eyes noticed the chest behind the stone,")
            print_pause("you opened it and found the sword there!\n")
            items.append('Rare Sword')
            check_elements(items, plant, animal)


def check_elements(items, plant, animal):
    if plant in items and animal in items and 'Rare Sword' in items:
        print_pause("\nThe three required elements has been found")
        print_pause("& the last living dragon Dragonite has been rescued!")
        play_again()
    elif len(items) == 2:
        print_pause("Two elements down, one to go!")
        rescue_dragonite(items, plant, animal)
    elif len(items) == 1:
        print_pause("One element down, two to go!")
        rescue_dragonite(items, plant, animal)
    elif len(items) == 0:
        print_pause("Three elements need to be found!")
        rescue_dragonite(items, plant, animal)


def play_game():
    items = []
    plants = ["Violet Plant", "Bacopa", "Bloody Cranesbill", "Lilac"]
    animals = ["Snow Leopard", "Sailugem Bear", "Red Panda", "Elephant Shrew"]
    plant = random.choice(plants)
    animal = random.choice(animals)
    intro()
    rescue_dragonite(items, plant, animal)


def play_again():
    print_pause("GAME OVER.\nDo you want to play again?")
    while True:
        play_again = input("(Yes to continue playing or No to exit): ").lower()
        if play_again == "no":
            print_pause("Thank you for playing. See you next time :)")
            break
        elif play_again == "yes":
            play_game()


play_game()
