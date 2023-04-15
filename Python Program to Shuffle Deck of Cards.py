# Python program to shuffle a deck of card

#import module
import itertools, random

# make the deck of cards
deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))

#Shuffle the deck
random.shuffle(deck)

#draw five cards
print("You got: ")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])