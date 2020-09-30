"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if (x%2==1):
        return True
    else:
        return False


def is_palindrome(word):
    string = word
    for i in range (0, (int (len(string)/2))):
        if string[i] != string[(len(string)-i-1)]:
            return False
    return True
    

            
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    odd = []
    for i in range (0, len(numlist)):
        if (numlist[i]%2 == 1 ):
            odd.append(numlist[i])
    return odd
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    text.lower()
    wordcount = dict()
    words = text.split()
    for word in words:
        if word in wordcount:
            wordcount[word] +=1
        else:
            wordcount[word] = 1
    return wordcount
    
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """

print (is_odd(190))
print (is_palindrome("abdhadba"))
list = [2,3,5,6,8,9,11,12]
print (only_odds(list))
a = "AHUhIIWm"
print (a.lower());
print (count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?"))