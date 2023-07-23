#%% Find words from letters provided

# Definitions

import enchant

d = enchant.Dict("es_ES")

def check_word(word):
    return d.check(word)

#%%

# Get words

# Check every conbination of letters and see if it is a word
letters = "paiern"
desired_length = len(letters)

# Get all combinations of letters
from itertools import permutations

words = []
for i in range(2, len(letters)+1):
    for p in permutations(letters, i):
        word = "".join(p)
        if check_word(word):
            words.append(word)

# Remove duplicates
words = list(set(words))

# Sort by length
words.sort(key=len, reverse=True)

# Remove words that have a length different from desired_length
words = [word for word in words if len(word) == desired_length]
 
# Print words
for word in words:
    print(word)




# %%
