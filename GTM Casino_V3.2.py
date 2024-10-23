# GTM Casino
# Made By Gabriel Tachie Menson
# Made In Visual Studio Code
# Started: 2024 - October - 18
# Finished: 

# Import the random plugin.
import random

# Prices Of Diffrent Actions
lottery_cost = 100
slots_cost = 500

# The balance of the player. 
player_balance = 10000

# The user is welcomed to the game
print("Welcome to the GTM Casino")
print(" ")

# The player learns how to play the game
print("If your balance gets to under 5 dollars you die")
print(" ")

while True:
    # The user chooses a action to do.
    print("The avalible games are lottery and slots.")
    print("To quit enter 'quit'.")
    print("To check or balance enter 'balance'.")
    print("The prices of the games are:")
    lottery_cost = str(lottery_cost)
    slots_cost = str(slots_cost)
    print("Lottery: " + lottery_cost + " Credits.")
    print("Slots: " + slots_cost +   " Credits. ")
    lottery_cost = int(lottery_cost)
    slots_cost = int(slots_cost)
    action = str.lower(input("Choose an action to do: "))
    print(" ")

    # Quit.
    if action == "quit":
        print("Good job.")
        print("You aren't a gambling addict.")
        break

    # Balance.
    player_balance = str(player_balance)
    print("Your balance is " + player_balance +".")
    player_balance = int(player_balance)
    print(" ")

    # Lottery.
    if action == "lottery":
        while True:

            # The user pays for the action.
            player_balance = player_balance - lottery_cost

            # This is how much money you will win if you win.
            lottery_prize = 100000000

            # The number is the highest number your can choose or the super big number in the 1 in (super big number) chance of winning.
            lottery_chance = int(14000000)
            lottery_chance = str(lottery_chance)

            # The user inputs the number they hope will win.
            lottery_input = int(input("Choose your number it can be from 1 to " + lottery_chance + (". ")))
            lottery_input = str(lottery_input)
            lottery_chance = int(lottery_chance) 
            print(" ")

            # The program chooses the winning number.
            lottery_win = int(random.randint(1,lottery_chance))
            lottery_win = str(lottery_win)

            # If the user guess the correct number (They won't) This happens.
            if lottery_input == lottery_win:
                print("You win! You guessed the correct number was " + lottery_win + "!")
                print("You won 100,000,000 credits.")
                print(" ")
                player_balance = player_balance + lottery_prize

                break

            # The user guesses the wrong number the are shown that they lost and what the right number is.
            if lottery_input != lottery_win:
                print("You lost. The winning number was " + lottery_win + ".")
                print(" ")

                break

    # Slots.
    if action == "slots": 

        # The user is billed for the price of the game
        player_balance = player_balance - slots_cost

        # How much money you'll win if you get each of the jack pots.
        slots_prize_111 = int(1000)
        slots_prize_222 = int(2000)
        slots_prize_333 = int(3000)
        slots_prize_444 = int(4000)
        slots_prize_555 = int(5000)
        slots_prize_777 = int(7000)
        slots_prize_888 = int(8000)
        slots_prize_999 = int(9000)

        # The program chooses each digit of the random number.
        Slots_digit_1 = str(random.randint(1,9))
        Slots_digit_2 = str(random.randint(1,9))
        Slots_digit_3 = str(random.randint(1,9))
        
        # The program combines the 3 digits to get the final number.
        slots_result = int(Slots_digit_1 + Slots_digit_2 + Slots_digit_3)

        # What happens if you spin 111.
        if slots_result == 111:
            player_balance = player_balance + slots_prize_111
            slots_prize_111 = str(slots_prize_111)
            print("You won! You spun the number 111 and won " + slots_prize_111 + " credits.")
            print(" ")
            
        else:

            # What happens if you spin 222.
            if slots_result == 222:
                player_balance = player_balance + slots_prize_222
                slots_prize_222 = str(slots_prize_222)
                print("You won! You spun the number 111 and won " + slots_prize_222 + " credits.")
                print(" ")

            else:

                # What happens if you spin 333.
                if slots_result == 333:
                    player_balance = player_balance + slots_prize_333
                    slots_prize_333 = str(slots_prize_333)
                    print("You won! You spun the number 333 and won " + slots_prize_333 + " credits.")
                    print(" ")

                else:

                    # What happens if you spin 444.
                    if slots_result == 444:
                        player_balance = player_balance + slots_prize_444
                        slots_prize_444 = str(slots_prize_444)
                        print("You won! You spun the number 444 and won " + slots_prize_444 + " credits.")
                        print(" ")

                    else:

                        # What happens if you spin 555.
                        if slots_result == 555:
                            player_balance = player_balance + slots_prize_555
                            slots_prize_555 = str(slots_prize_555)
                            print("You won! You spun the number 555 and won " + slots_prize_555 + " credits.")
                            print(" ")

                        else:

                            # What happens if you spin 777.
                            if slots_result == 777:
                                player_balance = player_balance + slots_prize_777
                                slots_prize_777 = str(slots_prize_777)
                                print("You won! You spun the number 777 and won " + slots_prize_777 + " credits.")
                                print(" ")

                            else:
        
                                # What happens if you spin 888.
                                if slots_result == 888:
                                    player_balance = player_balance + slots_prize_888
                                    slots_prize_888 = str(slots_prize_888)
                                    print("You won! You spun the number 888 and won " + slots_prize_888 + " credits.")
                                    print(" ")

                                else:

                                    # What happens if you spin 999.
                                    if slots_result == 999:
                                        player_balance = player_balance + slots_prize_999
                                        slots_prize_999 = str(slots_prize_999)
                                        print("You won! You spun the number 999 and won " + slots_prize_999 + " credits.")
                                        print(" ")

                                    else:

                                        # What happens if don't spin jackpots.
                                        slots_result = str(slots_result)
                                        print("You loose! You spun " + slots_result + ".")
                                        print(" ")
                                        