from random import choice 

def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    """

    chains = {}

    text_string = text_string.split()
    text_string.append(None)

    # for loop to go through text and group into tuples
    for i in range(len(text_string)-n):

        following_word = text_string[i + n]
        chain_keys_list = []
        
        while len(chain_keys_list) < n:
            chain_keys_list.append(text_string[i])
            i += 1

        chain_tuple = tuple(chain_keys_list)
        # chain_tuple = (text_string[i], text_string[i + 1])

    # conditional statement to check for chain_tuple in keys of dictionary
        # if new entry, it'll add a list containing a following word
        if chain_tuple not in chains.keys():
            chains[chain_tuple] = [following_word]
        # if not new entry, append the following word to the value
        else:
            chains[chain_tuple].append(following_word)

    return chains

def make_text(chains, n):
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
            # redefine random_key to be next key, first make into list so it's mutable then convert back to tuple.
            random_key_list = list(random_key[1:])
            random_key_list.append(next_word)
            random_key = tuple(random_key_list)

            # random_key (random_key[1], random_key[2], next_word)
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

chains = make_chains('Would you could you in a house? Would you could you with a mouse? Would you could you in a box? Would you could you with a fox? Would you like green eggs and ham? Would you like them, Sam I am?', 3)

print(make_text(chains, 3))
