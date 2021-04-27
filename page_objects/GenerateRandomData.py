import itertools
import random


# Generate random email
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

all_combos = list(itertools.combinations(letters, 7))
all_combos = [''.join(combo) for combo in all_combos]

random_email = random.sample(all_combos, 1)[0] + '@gmail.com'

# Generate random number
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

number_combo = list(itertools.combinations(numbers, 7))
number_combo = [''.join(combo) for combo in number_combo]

random_number = '032' + random.sample(number_combo, 1)[0]
