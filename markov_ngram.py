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

    print(chains)
    return chains

make_chains('Would you could you in a house? Would you could you with a mouse? Would you could you in a box? Would you could you with a fox? Would you like green eggs and ham? Would you like them, Sam I am?', 3)