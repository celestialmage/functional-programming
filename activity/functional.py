from functools import reduce

# Wave 1
# Write a function that takes in a list of words and returns the shortest
# one. (assume no ties)

# def shortest_word(words):
#     min_length = min(words, key=lambda x: len(x))
#     return min_length

def shortest_word(words):
    min_length = reduce(lambda x, y: x if len(x) < len(y) else y, words)
    return min_length

# SUPER CHALLENGE: use functools.reduce
# Only try this after completing the rest of the activity
# You will need to research the use of the functools.reduce function
# def shortest_word(words):
#     from functools import reduce
#     pass    



# Wave 2
# Write a function that takes in a list of numbers and returns a new list
# containing only the ones that are even, in the same order.
# Hint: remember to convert back to a list!

def even_nums(nums):
    even_only = filter(lambda x: x % 2 == 0, nums)
    return list(even_only)

# Wave 3
# Write a function that takes in a list of numbers and returns a new list
# containing the squares of those numbers (the numbers raised to the second power)
# Hint: remember to convert back to a list!

def squares(nums):
    squared = map(lambda x: x ** 2, nums)
    return list(squared)

# Wave 4
# Write a function that accepts a word, a function, and the name of that 
# function. It should return a string that reports:
# "The result of applying FUNCTION_NAME to WORD is RESULT"

def report(word, function, function_name):
    return f"The result of applying {function_name} to {word} is {function(word)}"

# Wave 5
# Write a function that takes a list of passwords and returns a list of only 
# those passwords that have at least one non-alphabetic character in them. 
# The returned list should be sorted by in order of increasing length.

def sorted_valid_passwords(passwords):
    result = filter(lambda x: x.isalpha() == False, sorted(passwords, key=lambda x: len(x)))
    return list(result)

