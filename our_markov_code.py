"""Generate Markov text from text files."""

import os
import sys
from random import choice
import twitter

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    read_file = open(file_path).read()

    # file_path.close()

    return read_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    """

    chains = {}

    text_string = text_string.split()
    text_string.append(None)

    # for loop to go through text and group into tuples
    for i in range(len(text_string)-2):

        following_word = text_string[i + 2]
        chain_tuple = (text_string[i], text_string[i + 1])

    # conditional statement to check for chain_tuple in keys of dictionary
        # if new entry, it'll add a list containing a following word
        if chain_tuple not in chains.keys():
            chains[chain_tuple] = [following_word]
        # if not new entry, append the following word to the value
        else:
            chains[chain_tuple].append(following_word)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # random_key pulls a tuple from the .keys() in dictionary chains and converts to list. .keys() DOES NOT GENERATE A LIST. it generates an ITERABLE.
    random_key = choice(list(chains.keys()))
    # next_word randomly chooses from the values (which is list) associated with random_key
    next_word = choice(chains[random_key])

    # initializing counter variable for length of words list
    total_char = len(words)

    # while loop to make sure text won't exceed character limit  
    while total_char < 250:

        len_words = sum(len(i) for i in words)
        spaces = len(words) - 1
        total_char = len_words + spaces
 
        
        # conditional statement to make sure random_key has a next_word available.
        if next_word is not None:
            # redefine random_key to be the next sequential tuple
            random_key = (random_key[1], next_word)
            words.append(next_word)
            # redefine next_word to be from the values associated with new tuple
            next_word = choice(chains[random_key])

        # once we hit none, comes out of while loop
        else:
            words.pop()
            break
            # if total_char < 280:
            #     break
            # else:
            #     words.pop()

    print("character length is {}".format(total_char))
    return " ".join(words)

def tweet(chains):
    """Create a tweet and send it to the Internet."""

    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.

    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    status = api.PostUpdate(chains)

    print(status.text)


# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
# filenames = sys.argv[1:]

# # Open the files and turn them into one long string
# text = open_and_read_file(filenames)

# # Get a Markov chain
# chains = make_chains(text)

# Your task is to write a new function tweet, that will take chains as input
# tweet(chains)


def execute_functions(file_name):
    input_path = file_name

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)
    
    # Get a Markov chain
    chains = make_chains(input_text)
    
    # Produce random text
    random_text = make_text(chains)

    tweet(random_text)

execute_functions('lyrics.txt')





