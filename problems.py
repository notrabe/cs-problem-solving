# task 3 of 7 - Remove vowels from input string.
"""
def csRemoveTheVowels(input_str):
    vowels = ['a', 'e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']
    for x in input_str:
        if x in vowels:
            input_str = input_str.replace(x, '')
    return input_str
        
print(csRemoveTheVowels('Lambda School is Awesome!'))

"""

# task 4 of 7 - Return the shortest word from a string of words.

"""

def csShortestWord(input_str):
    stringToSplit = input_str
    splitString = stringToSplit.split()
    print(splitString)

    shortestWord = min(splitString, key=len)
    return len(shortestWord)

print(csShortestWord('Happy Day'))

"""

# task 5 of 7 - Given an array of integers, return the sum of all the positive integers in the array.

"""

def csSumOfPositive(input_arr):
    return sum(x for x in input_arr if x > 0)

print(csSumOfPositive([1, 2, 3, -4, 5, -3, 7, 8, 9, 6, 4, -7]))

"""

# task 6 of 7 - Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

def csLongestPossible(str_1, str_2):
    newString = str_1 + str_2                   #combine the two strings
    print(newString)

    return ''.join(sorted(set(newString)))      #use set() to create a set of the unique characters in the new string; sort them using sorted(); join the characters using ''.join

print(csLongestPossible('abc', 'zyx'))

# task 7 of 7 - Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5)

"""

def csAnythingButFive(start, end):
    arrayOfNumbers = []                                 # initialize empty array
    rangeList = list(range(start, end + 1))             # increase the end point of the range by 1 so it ends in the spot we want, then make a list of the numbers in that range
    print(rangeList)

    for i in rangeList:                                 # for each index in the list we just created, if the string of that index doesn't contain a 5, we add it to the empty array.
        if '5' not in str(i):
            arrayOfNumbers.append(i)
    print(arrayOfNumbers)
    return len(arrayOfNumbers)
    
print(csAnythingButFive(1, 5))

"""