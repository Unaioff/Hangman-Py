import random
import os

HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

words = [
    "Apple", "Banana", "Cherry", "Dragon", "Elephant", "Falcon", "Giraffe", "Horizon", "Island", "Jungle",
    "Kingdom", "Lantern", "Mountain", "Neptune", "Ocean", "Pyramid", "Quasar", "Rainbow", "Satellite", "Thunder",
    "Unicorn", "Volcano", "Wizard", "Xylophone", "Yacht", "Zebra", "Almond", "Bicycle", "Circus", "Dolphin",
    "Emerald", "Forest", "Galaxy", "Harbor", "Igloo", "Jaguar", "Knight", "Library", "Meteor", "Necklace",
    "Octopus", "Penguin", "Quicksand", "Rocket", "Sunset", "Treasure", "Universe", "Victory", "Waterfall", "Xenon",
    "Yellow", "Zipper", "Acorn", "Balloon", "Castle", "Desert", "Engine", "Feather", "Garden", "Helicopter",
    "Iceberg", "Jellyfish", "Kite", "Lighthouse", "Mermaid", "Notebook", "Oasis", "Parrot", "Quartz", "River",
    "Starfish", "Telescope", "Umbrella", "Vortex", "Whale", "Xenophobia", "Yawn", "Zephyr", "Anchor", "Bridge",
    "Compass", "Dinosaur", "Echo", "Firefly", "Glacier", "Hurricane", "Insect", "Jewel", "Kangaroo", "Lizard",
    "Magnet", "Narwhal", "Olive", "Peacock", "Quill", "Robot", "Seahorse", "Tornado", "Universe", "Volcano"
]

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Title():
    Clear()
    print("                                                           +---+  ")
    print("        _    _                   __  __                    |   |  ")
    print("       | |  | |                 |  \/  |                       |  ")
    print("       | |__| | __ _ _ __   __ _| \  / | __ _ _ __             |  ")
    print("       |  __  |/ _` | '_ \ / _` | |\/| |/ _` | '_ \            |  ")
    print("       | |  | | (_| | | | | (_| | |  | | (_| | | | |           |  ")
    print("       |_|  |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|           |  ")
    print("                            __/ |                        =========")
    print("                           |___/                                  ")
    print(
    """
    1) You Vs Friend
    2) You Vs Machine
    3) Exit
    """)

    mode = input(">> ")
    global word
    if mode == "1":
        Clear()
        word = input("Enter the word to guess: ")
        Start()
    elif mode == "2":
        word = random.choice(words)
        Start()
    elif mode == "3": exit()
    else: Title()

def Start():
    global word_to_guess, guessed_letters, Playing, Error
    word_to_guess = list(word.lower())
    guessed_letters = []
    Error = 0
    Playing = True
    
    while Playing:
        Clear()
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(HANGMANPICS[Error])
        print("")
        print(f"=======[ {display_word} ]=======")
        print("")
        answer = input(">> ").lower()
        if len(answer) != 1 or not answer.isalpha():
            print("Please enter a valid letter...")
            continue
        
        if answer in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(answer)

        if answer in word_to_guess:
            if all(letter in guessed_letters for letter in word_to_guess):
                input(f"Congratulations! You've guessed the word: {word}")
                Playing = False
                Title()
        else:
            Error += 1 
            if Error == 7:
                GameOver()

def GameOver():
    Clear()
    print("                                                                             ")
    print("        ██████╗  █████╗ ███╗   ███╗███████╗ ██████╗ ██╗   ██╗███████╗██████╗ ")
    print("       ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print("       ██║  ███╗███████║██╔████╔██║█████╗  ██║   ██║██║   ██║█████╗  ██████╔╝")
    print("       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print("       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print("        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
    print("                                                                             ")
    print(f"The word was: {word}")
    input("  Press any key to continue...                                  ")
    Title()

Title()

