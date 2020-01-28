#!/usr/bin/env python3
import sys, random #imports

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #prints greeting
colors = ['red','orange','yellow','green','blue','violet','purple'] #a list that has a few names of colors
play_again = '' #a variable with an empty as its assignment
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #a while loop that keeps on running as long as the player wants to by only ending if they say no or n
    match_color = random.choice(colors) #so it makes this a random color from one within the list
    count = 0 # a counter variable
    color = '' #empty string variable
    while (color != match_color): # a while loop that will continually run for as long as the guess and the random color are not the same
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #asks what the color is and then this is where it makes your guess lower case adn without spaces
        count += 1 #adds 1 to the counter
        if (color == match_color): #will print correct if you get it right
            print('Correct!')
        else: #will print and rerun the while loop all while disp,aying the counter
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count)) #after you complete the game it will print the numebr of times it took to guess it

    if (count < best_count): # if you took less guesses than previously it will say the print statement
        print('This was your best guess so far!')
        best_count = count # redefines best_count as count effectivly making it your new highscore

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #this will allow you to keep playing as long as you dont put in n or no

print('Thanks for playing!') #after the program is done will print this