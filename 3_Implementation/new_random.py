import random


###########
# CLASSES #
###########
class GuessGame:
    # CONSTRUCTOR
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.attempts = 0
        self.pb = 100  # default PB
        self.actual_number = int(random.randint(lower, upper))

    # PURPOSE: Get the guess, print result, and output bool for pass/fail
    def MakeGuess(self, guess):
        guess_correct = False
        try:
            # -- Guess is not in range
            if int(guess) < self.lower or int(guess) > self.upper:
                print("Please guess a number within the given range")

            # -- Guess is correct
            elif int(guess) == self.actual_number:
                self.attempts += 1
                print("Nice! You got it!\nIt took you {} attempt/s".format(self.attempts))
                # change pb if needed
                if self.attempts < self.pb:
                    self.pb = self.attempts

                guess_correct = True

            # -- Guess is lower than actual number
            elif int(guess) < self.actual_number:
                print("Too low!")
                self.attempts += 1

            # -- Guess is higher than actual number
            elif int(guess) > self.actual_number:
                print("Too high!")
                self.attempts += 1
        except ValueError:
            print("Invalid value.")

        return guess_correct


#############
# FUNCTIONS #
#############

# PURPOSE set up a game class within user input
def setupGame():
    ShouldContinue = True
    while ShouldContinue:
        try:
            lower = int(input("Enter the lower bound... "))
            upper = int(input("Enter the upper bound... "))
            ShouldContinue = False
        except:
            print("Please print an integer.")
    Game = GuessGame(lower, upper)
    return Game


def playGame(Game):
    print("Game beginning")

    play_again = True
    while play_again:
        Game.actual_number = int(random.randint(Game.lower, Game.upper))  # Reset settings
        Game.attempts = 0  # reset attempts
        passed = False

        while not passed:
            guess = input("Pick a number between {} and {}: - ".format(Game.lower, Game.upper))
            passed = Game.MakeGuess(guess)

        Choice = input("Would you like to play again? (y/n): ")
        if Choice.lower() != 'y':
            play_again = False
    print("Goodbye!")


def get_name():
    player_name = input("Hello! What is your name? ")
    return player_name


def menuChoice(Name):
    print("""
    What would you like to do today, {}?

    >1. Play Guessing Game
    >2. Change Settings
    >3. Get PB
    >0. Exit
    """.format(Name))
    cont = True
    while cont:
        try:
            choice = int(input("(Enter 1/2/0): "))
            if 0 <= choice <= 3:
                cont = False
            else:
                print("Choose a value in range 0-2")
        except:
            print("Invalid value, try again")
    return choice


########
# MAIN #
########
if __name__ == "__main__":
    # -- DEFAULT SETTINGS AND SETUP STUFF -- #
    default_lower = 1
    default_upper = 10
    game = GuessGame(default_lower, default_upper)
    name = get_name()
    # MAIN PROGRAM
    should_continue = True
    while should_continue:
        choice = menuChoice(name)

        # >1. Play game
        if choice == 1:
            playGame(game)
        # >2. Change Settings
        elif choice == 2:
            game = setupGame()
        # >3. Get PB
        elif choice == 3:
            print("Your personal best is: " + str(game.pb))
        # >3. Exit
        else:
            print("Ok, seeya!")
            should_continue = False  # end program
