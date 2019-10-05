#Author: Nithin Prasasd
#Date Created: 28/09/2019
#Program Name: palindrome_permutation.py
#Program Description: (CTCI 1.4) Given a string, write a function to check if it is a
# permutation of a palindrome (not limited to dictionary words). 

#Note: case of letters are irrelevant AND ignore non-letters!
#Note: Function is of complexity: O(n) in time, O(1) in space
def palindrome_permutation(str_in):

    str_in = str_in.lower()
    allowable_chars = list("abcdefghijklmnopqrstuvwxyz")
    
    dict_chars = {}
    onezie = False #Set to true if an odd count of characters is found. If more than
                    # one odd count exists, the string cannot be a palindrome!
    
    #Collect counts of every character in word
    for char in str_in:
        if char in allowable_chars:
            if char in dict_chars.keys():
                dict_chars[char] += 1
            else:
                dict_chars[char] = 1
            
    #Check if more than one onezie exists!
    for char in dict_chars.keys():
        if dict_chars[char]%2 == 1:
            if onezie:
                return False
            else:
                onezie = True

    #A max of one onezie exists (one character of this set goes into the center of the
    # string, allowing all other characters, for which a pair exists to alternate
    # on either side of the string. Thus the remaining string is a palindrome!
    return True

def palindrome_permutation_harness(func):

    print(func("")) #True
    print(func("lru")) #False
    print(func("obl!&bol")) #True
    print(func("obolLOOB")) #True
    print(func("oblo clb")) #True

if __name__ == "__main__":

    palindrome_permutation_harness(palindrome_permutation)
