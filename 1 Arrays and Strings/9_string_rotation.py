#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: string_rotation.py
#Program Description: Given 2 input strings, this program computes if one
# string is a rotation of another using 1 call to issubstring (in Python
# we use the .find method).

#Time complexity is O(n) since .find is O(n).
def string_rotation(str1, str2):

    #diff length strings are irrotatable
    if len(str1) != len(str2):
        return False

    #Case insensitive
    str1 = str1.lower()
    str2 = str2.lower()

    str_new = str1 + str1 #duplicating str1 allows a potentially rotated
                          # version of str2 to now exist in str_new

    rotate = str_new.find(str2) #-1 if str2 not in str_new

    if rotate >= 0:
        return True
    else:
        return False

def string_rotation_test(func):

    print("Testing function: ", func.__name__)
    print(func("","")) #True
    print(func("a","")) #False
    print(func("a","b")) #False
    print(func("ab","ba")) #True
    print(func("alpha","phaal")) #True
    print(func("beta","beat")) #False
    print(func("waterbottle","erbottlewat")) #True

if __name__ == "__main__":

    string_rotation_test(string_rotation)
