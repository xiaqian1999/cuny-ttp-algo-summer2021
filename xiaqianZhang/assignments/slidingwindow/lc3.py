# Problem Statement #
# Given a string s, find the length of the longest substring without repeating characters.

'''
Input: A string
Output: length of longest substring that contains unique characters

initialize with a startIndex = 0
initialize dictionary that contains the each unique characters and the count of each
initialize with the longestLength = 0

loop through each index in the string:
    initliaze with the current index's value 
    check if the current index's value character is in the dictionary:
        if it's not in the dictionary ->  initliaze as the value of the count as 0
        if it is in the dictionary -> we need to update the length
            initialize the character's value in the string
            then decrement the value count of the current character in the dictionary
            if the count is 0 -> delete the entire value
            increment the startIndex
        update the longestLength

'''


def longestSubstring(str):
    startIndex = 0
    uniqueCount = {}
    longestLength = 0

    for each in range(len(str)):
        currentChar = str[each]
        if currentChar not in uniqueCount:
            uniqueCount[currentChar] = 0
        else:
            uniqueChar = str[startIndex]
            uniqueCount[uniqueChar] -= 1
            if uniqueCount[uniqueChar] == 0:
                del uniqueCount[uniqueChar]
            startIndex+=1
        longestLength = max(longestLength, each - startIndex + 1)

    return longestLength

def main():
    print("The length of the longest substring without repeating characters: " + str(longestSubstring("abcabcbb")))
    # abc -> 3
    print("The length of the longest substring without repeating characters: " + str(longestSubstring("bbbbb")))
    # b -> 1
    print("The length of the longest substring without repeating characters: " + str(longestSubstring("pwwkew")))
    # wke -> 3

main()