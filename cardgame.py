# Implements a cards shuffler and dealer.

# import random module to use the shuffle method (randomly shuffle elements in list)
import random

# Write a declaration for the Card class.
# this class creates a card
class Card:

    # init sets values when creating one specific object of type Card
    def __init__(self, suit, value):  # suit and value parameters have to be declared when creating the class
        self.suit = str(suit)
        self.value = str(value)

    # method
    def description(self):
        '''
        returns a string that properly describes the object.
        e.g. 'Ace of Spades'
        '''

        # provide an easily readable description of the Card object
        return (f"{self.value} of {self.suit} ")

# declare the class
class Deck:

    # set intializer (default values):
    # each object (deck) starts with these attributes
    def __init__(self):
        self._suits = ['Hearts','Diamonds','Clubs','Spades']
        self._values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        # set empty list to generate all 52 Cards and add them to a list called _cards
        self._cards = []

        # loop through lists of suits and values and add each combination to a card
        for suit in self._suits:
            for value in self._values:
                # # calls on the Card class to create a cars with these particular suits and values
                card = Card(suit,value)
                # append card (string), to list of cards to create a deck
                self._cards.append(card)

    # method
    def description(self):
        return f"{len(self._cards)} cards in the deck"

    # method
    def shuffle(self):
        '''
        Call random.shuffle with the cards attribute as a parameter.
        It shuffles the deck.
        '''
        return random.shuffle(self._cards)

    # method
    def deal(self):
        '''
        method deal that removes the top card from the cards list and return it.
        To remove means that after calling deal, the number of cards in cards will have decreased by 1
        '''
        return self._cards.pop()

if __name__ == "__main__":
    '''
    Anything that’s inside this if will only be executed if we run the
    file directly from the command line using python cardgame.py.
    '''
    # basic:
    # var1 = Card('Spades', 'Ace')
    # print(var1.description())

    # create one instance of a Deck and print it.
    deck = Deck()
    print(deck.description())

    # shuffle cards in the Deck
    deck.shuffle()
    print(deck.description())

    card = deck.deal()
    print(card.description())
    print(deck.description())
