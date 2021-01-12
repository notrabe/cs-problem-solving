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

def csSumOfPositive(input_arr):
    return sum(x for x in input_arr if x > 0)

print(csSumOfPositive([1, 2, 3, -4, 5, -3, 7, 8, 9, 6, 4, -7]))