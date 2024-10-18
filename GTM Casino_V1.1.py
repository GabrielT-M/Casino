# The GTM Casino
# Made By Gabriel Tachie Menson
# Made In Visual Studio Code
# Started: 2024 - October - 18
# Finished: 

# Import the random plugin
import random

# The user is welcomed to the game
print("Welcome to the GTM Casino")
print(" ")

# The player has a balance that they can use gamble
player_balence = 100000
player_balence = str(player_balence)
print("Your balence is " + player_balence + ".")
player_balence = int(player_balence)

# The player learns how to play the game
print("If your balence gets to under 5 dollars you die")
print(" ")

# The user needs to choose the game to play
print("The avalible games are lottery, and to quit input quit.")
print("The prices of the games are:")
print("Lottery: 5 Credits")
print("Roulette: 10 Credits ")
game = input("Choose a game to play: ")

#Lottery
while True:
    lottery_win = 100000000
    if game == "Lottery":

        # The number is the highest number your can choose or the super big number in the 1 in (super big number) chance of winning.
        chance_int = int(14000000)
        chance_str = str(chance_int)

        # The user inputs the number they hope will win.
        userinput_int = int(input("Choose your number it can be from 1 to " + chance_str + (". ")))
        userinput_str = str(userinput_int)
        print(" ")

        # The program chooses the winning number.
        win_int = int(random.randint(1,chance_int))
        win_str = str(win_int)

        # If the user guess the correct number (They won't) This happens.
        if userinput_int == win_int:
            print("You win! You guessed the correct number was " + win_str + "!")
            print("You won 100,000,000 credits.")
            player_balence = player_balence + lottery_win
            break

        # The user guesses the wrong number the are shown that they lost and what the right number is.
        if userinput_int != win_int:
            print("You lost. The winning number was " + win_str + ".")
            break


# Roulette
while True:
    rou





# 