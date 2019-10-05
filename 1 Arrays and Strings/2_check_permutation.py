#Author: Nithin Prasad
#Date Created: 26/09/2019
#Program Name: check_permutation.py
#Program Description: (CTCI 1.2) Given 2 strings, write a method to decide
# if one string is a permutation of the other.

#NOTE: solution is case sensitive; spaces matter!!!!
#NOTE: algorithm runs in O(n) time and O(n) space
#NOTE: alternative solution: sort the strings (n*(log n) time worst case) and
# compare each char (log n time) => O(n*logn) time, O(1) space!


def check_permutation(str1,str2):

    #Basic check: diff length strings are not permutations
    if len(str1) != len(str2):
        return False

    #Collect str1&str2 into a dictionary
    letters_dict = {}

    for i in range(len(str1)):

        char1 = str1[i]
        char2 = str2[i]

        if char1 in letters_dict.keys():
            letters_dict[char1] += 1
        else:
            letters_dict[char1] = 1

        if char2 in letters_dict.keys():
            letters_dict[char2] += -1
        else:
            letters_dict[char2] = -1

    #Check if all the keys have value 0
    for key in letters_dict.keys():
        if letters_dict[key] != 0:
            return False

    return True    

def check_permutation_harness(function):

    print("Running tests on function: ", function.__name__)
    print(function("","")) #True - empty strings permute
    print(function("","name")) #False
    print(function("name1","name 1")) #False - diff length
    print(function("name1","1eamn")) #True
    print(function("nameeth","thenane")) #False


if __name__ == "__main__":

    check_permutation_harness(check_permutation)
