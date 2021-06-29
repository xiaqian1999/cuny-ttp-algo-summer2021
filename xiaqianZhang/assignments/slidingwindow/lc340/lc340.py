# Problem Statement #

# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

'''
Input: A string, target integer with k unique integers
Output: number that is the longest substring in the given string with k unique character

Edge case: if k is 0, return empty string, since there will be no such substring
initliaze with a startIndex, that we want to constantly looping and update throughout the string
intialize with dictionary that contains the count of each unique characters as key-value pair -> unique charater : count
intialize with the longestSize = 0

loop through each index in the given string with for loop:
  initliaze with a current index's character -> currentChar = str[each]
  check if the current index's character is in the dictionary:
   if not in the dictionary -> initialize the value as 0
   if its in the dictionary -> increment the value by 1
  while the length of the dictionary is greater than target k:
    initialize the first index value in the dictionary
    decrement the count of the unique character
    check if the value of the count is equal to 0:
    if so, we delete the entire key value
  
  outside of the while loop, we increment the startIndex value
update the longestSize as max(longestSize, currentIndex - startIndex + 1)
return longestSize
'''

def longest_substring_with_k_distinct(str, k):
  startIndex = 0
  uniqueCount = {}
  longestSize = 0

  for each in range(len(str)):
    currentChar = str[each]
    if currentChar not in uniqueCount:
      uniqueCount[currentChar] = 0
    uniqueCount[currentChar] += 1
    
    while len(uniqueCount) > k:
      uniqueChar = str[startIndex]
      uniqueCount[uniqueChar] -= 1
      if uniqueCount[uniqueChar] == 0:
        del uniqueCount[uniqueChar]
      
      startIndex +=1
    longestSize = max(longestSize, each - startIndex + 1)
    
  return longestSize

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  # "araa" length of 4
  # araa -> raa -> aac -> ac -> ci
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  # "aa" length of 2
  # a -> r -> aa -> c -> i
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
  # "cbbeb" "bbebi" length of 5
  # cbbeb -> bbebi -> bebi -> ebi -> bi -> i


main()



# Solution
# -----
  # window_start = 0
  # max_length = 0
  # char_frequency = {}

  # # in the following loop we'll try to extend the range [window_start, window_end]
  # for window_end in range(len(str1)):
  #   right_char = str1[window_end]
  #   if right_char not in char_frequency:
  #     char_frequency[right_char] = 0
  #   char_frequency[right_char] += 1

  #   # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
  #   while len(char_frequency) > k:
  #     left_char = str1[window_start]
  #     char_frequency[left_char] -= 1
  #     if char_frequency[left_char] == 0:
  #       del char_frequency[left_char]
  #     window_start += 1  # shrink the window
  #   # remember the maximum length so far
  #   max_length = max(max_length, window_end-window_start + 1)
  # return max_length
