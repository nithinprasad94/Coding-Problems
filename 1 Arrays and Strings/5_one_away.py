#Author: Nithin Prasad
#Date Created: 28/09/2019
#Program Name: one_away.py
#Program Description: Given 2 strings, this program checks if they are one away (by
# insert, remove or delete)

#Note: spaces and non-alphabetic characters count, case does not!
#Note: algorithm is of complexity O(n) in time, O(1) in space
def one_away(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    len_diff = abs(len(str1)-len(str2))
    len_max = max(len(str1),len(str2))
    
    if len_diff > 1:
        #Fails if more than 1 away by remove or delete
        return False

    #Iterate through both strings by 1 char at a time. If unequality is reached
    # at a given index, advance the longest string's index by 1.
    #NOTE: here we handle inserts and removes identically (or agnostically)
    str_long = None
    str_short = None
    
    if len(str1) >= len(str2):
        str_long = str1
        str_short = str2
    else:
        str_long = str2
        str_short = str1
        
    i = 0 #points through str_L
    j = 0 #points through str_S
    mirrored = True #See if strings are a mirrored to any given iteration/index of loop

    #print("-------------------------------")
    #print("<"+str_long+">")
    #print("<"+str_short+">")

    #NOTE: length 0 strings     
    while i < len(str_long) and j < len(str_short):

        char_long = str_long[i]
        char_short = str_short[j]

        if char_long != char_short:
            #characters seem different ...

            if mirrored:
                mirrored = False

                if len_diff == 0:
                    #Increment for replacement
                    i += 1
                    j += 1

                else:
                    #Increment for inserted string ONLY so that the next iteration,
                    # we remember to check the new character in the long string with
                    # the old one in the short string.
                    i += 1
                   
            else:
                # 1 character was already different prior
                return False

        else:
            #characters are the same!
            i += 1
            j += 1
        
    return True

def one_away_harness(func):
    
    print("Testing for function: ",func.__name__)
    print(func("","")) #True - base case
    print(func(" ","")) #True - base case 
    print(func("a","")) #True - base case
    print(func("a","b")) #True
    print(func("a","ab")) #True
    print(func("ba","a")) #True
    print(func("abca","aca")) #True
    print(func("asdfasdf","asdfas")) #False
    print(func("asadaf","asabgf")) #False
    print(func("abdca","abua")) #False - 0 insert and mod, side by side

if __name__ == "__main__":

    one_away_harness(one_away)
