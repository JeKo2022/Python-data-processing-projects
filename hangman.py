
# Assignment: Hangman

# random is used to get pick a random word of correct length from lexicon
import random

class Lexicon:
    '''
    Objects of class Lexicon are used to retrieve words for the game from a dictionary.
    The Lexicon class is based on the file dictionary.txt
    '''

    def __init__(self, word_length):

        '''
        Function reads file, creates list with possible words, also does two assertions.
        '''

        assert word_length > 0 and word_length < 46, "Invalid word length for Lexicon"

        # initialize an empty list to note the possible length of words in the lexicon
        # used for assertion that the wordlength that is given to the Lexicon actually exists in the dictionary
        self._list_leng_words = []

        # initialize word_length for use in different functions
        self._word_length = word_length

        # initialize list for words with word_length
        self._possible_words = []

        # function assumes this filename
        filename = 'dictionary.txt'

        with open(filename, 'r') as f:
            # loop through every word
            for word in f:
                # the file dictionary txt has one word on each line: adjust word_length to discard "\n"
                word = word[:-1]
                # place words with correct length in list of possible lengths
                if len(word) == self._word_length:
                    self._possible_words.append(word)

                # fill list_leng_words with the possible lengths of words in the lexicon for assertion wordlength below
                if len(word) not in self._list_leng_words:
                    self._list_leng_words.append(len(word))

            # assertion that checks whether the wordlength that is given to the Lexicon actually exists in the dictionary.
            assert word_length in self._list_leng_words, "Word with this length not in Lexicon"

        return None



    def get_word(self):
        '''
        Function gets a word from the list of possible words. Returns a string.
        '''

        random_word = random.choice(self._possible_words)

        return random_word

class Hangman:
    '''
    Function plays hangman game based on Lexicon class.

    '''

    def __init__(self, word, number_guesses):

        # initialize word, number of guesses
        self._word = word
        self._number_guesses = number_guesses

        # set guesses left to number of guesses to keep track of the nr. of guesses left
        self._guesses_left = number_guesses

        # set empty list to keep track of letters guessed correctly
        self._letters_guessed_correctly = []
        self._list_of_guesses = []

    def is_running(self):
        '''
        This function keeps track of wether there are any guesses left and if game has not been won.
        Returns true or false - keep going or game over / game won
        '''

        # call on function self.won to see whether game has been won and self._guess_left is at least 1.
        if self._guesses_left > 0 and self.won() == False:
            return True
        else:
            return False

    def won(self):
        '''
        This function considers whether game has been won.
        Returns true or false - game won or not (yet) won.
        '''

        if len(self._letters_guessed_correctly) == len(self._word):
            return True
        else:
            return False


    def guesses_left(self):
        '''
        This function keeps track of wether there are any guesses left and if game has not been won.
        Returns true or false - keep going or game over / game won
        '''

        if self._guesses_left > 0 and self.won() == False:
             return self._guesses_left
        else:
            return False


    def is_valid_guess(self, letter):
        '''
        This function considers whether the user input is a a string.
        If it is not a string, the function returns false so that another guess must be made.
        '''

        if letter.isalpha() and letter not in self._list_of_guesses:
            return True
        else:
            return False


    def current_pattern(self):
        '''
        This function compares the list of letters that the user has guessed correctly to the word that needs to be guessed.
        It then enables a pattern to be printed of current guesses.
        '''
        # create empty list to put the letters that have and have not been guessed in
        pattern = []

        # loop through  letters in the word (to be guessed) and add as letter if guessed, add as "_" if not guessed
        for letter in self._word:
            if letter in self._letters_guessed_correctly:
                pattern.append(letter)
            else:
                pattern.append("_")

        # join strings in list for readibility
        pattern = ''.join(pattern)

        return pattern


    def guess(self, letter):

        # assert correct parameters for guess
        assert self.is_valid_guess(letter) == True, "invalid guess"
        assert len(letter) == 1, "any input other than a single letter is invalid"

        # adjust number of guesses left
        self._guesses_left = self._guesses_left - 1

        # get list of letters in the word
        list_of_letters = []
        list_of_letters = list(self._word)

        # set correctness to False in order to change if the guess is correct
        correctness = False

        # see if guessed letter is in letters of word
        for letter_word in list_of_letters:
            if letter_word == letter:
                correctness = True
                self._letters_guessed_correctly.append(letter)

        # add letter guess to list of guessed for use in assertion validity guess
        self._list_of_guesses.append(letter)

        if correctness == True:
            return True
        else:
            return False


if __name__ == '__main__':

    print("WELCOME TO HANGMAN ツ")

    # prompt and re-prompt for word length
    word_length = int(input("What length of word would you like to play with?\n"))
    while word_length > 44:
        word_length = int(input("No words are longer than 44 letters!\n"))

    # load words
    lexicon = Lexicon(word_length)

    # prompt and re-prompt for number of guesses
    number_guesses = int(input("How many guesses are allowed?\n"))
    while number_guesses <= 0:
        number_guesses = int(input("Negative or zero guesses make no sense.\n"))

    # run an infinite number of games
    while True:

        # game set-up
        print(f"I have a word in my mind of {word_length} letters.")
        word = lexicon.get_word()
        print(word) # remove when done
        game = Hangman(word, number_guesses)


        # # allow guessing and provide guesses to the game
        while game.is_running():
            # prompt and re-prompt for single letter
            letter = input(f"Guess a letter ({game.guesses_left()} left): ")
            if len(letter) != 1 or not game.is_valid_guess(letter):
                # reprompt the user for a valid guess
                print("invalid guess")
                continue # terminates the inner loop so goed back to while

            # provide feedback
            if game.guess(letter):
                print("It's in the word! :))")
            else:
                print("That's not in the word :(")

            print(game.current_pattern())

        # after game ends, present the conclusion
        if game.won():
            print("Whoa, you won!!! Let's play again.")
        else:
            print(f"Sad, you lost ¯\_(ツ)_/¯. This was your word: {word}")
