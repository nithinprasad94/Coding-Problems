#Author: Nithin Prasad
#Date Created: 25/09/2019
#Program Name: is_unique.py
#Program Description: (CTCI 1.1) Program to check if (i) string has all
# unique chars, and (ii) do above w/o additional data structs

#Structs allowed
#Note: Algorithm in O(n) time and O(c)=O(1) space
def is_unique(str_in):

    #Assume: using 128 character ASCII
    if len(str_in) > 128:
        return False

    #Setup a dictionary to hold letter-frequency pairs
    char_dict = {}

    #For Loop: tabulate letter frequencies
    for elem in str_in:

        if elem in char_dict.keys():
            return False
        else:
            char_dict[elem] = 1

    return True

#No structs allowed - assume we can only use SCALAR data types
#NOTE: Algorithm uses O(n^2) time and O(1) space.
#NOTE: if allowed to mod original string, sort string and compare neighbouring chars for equality
# -> would yield O(n*logn) time, O(1) space (ONLY IF we are sorting in place).
def is_unique_no_structs(str_in):

    for i in range(len(str_in)):

        for j in range(i+1,len(str_in)):

            if (str_in[i] == str_in[j]) and (i != j):

                return False
    return True

#Test Harness for all is_unique functions in this file
def is_unique_common_harness(func):

    print("Testing for function: ", func.__name__)
    print(func("")) #True
    print(func("aA")) #True -> case is unique! (Assumption)
    print(func("utopia")) #True
    print(func("granger")) #False
    print(func("/storm.")) #True
    print("")

if __name__ == "__main__":

    #With Structs
    is_unique_common_harness(is_unique)
    
    #No structs
    is_unique_common_harness(is_unique_no_structs)
