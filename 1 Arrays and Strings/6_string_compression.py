#Author: Nithin Prasad
#Date Created: 28/09/2019
#Program Name: string_compression.py
#Program Description: this program compresses a string of adjacent repeated
# characters and returns a (i) compressed string ONLY IF the length of the
# compressed is smaller than the original, (ii) OR returns the original
# otherwise.

#NOTE: easy solution is string concatenation (but this is inefficient)
# because the algorithm requires sigma(0 to n-1) [n] which is O(n^2)
# character additions by the nth iteration. Thus, we try a better method!
#NOTE: Algorithm of complexity O(n) time and O(n) space.
def string_compression_improved(str_in):

    str_list = []

    j = 0 #tracks index of first occurence of previous character (in seq.)
    count = 0
    
    for i in range(len(str_in)):
        new_char = str_in[i]
        old_char = str_in[j]

        if old_char == new_char:
            count += 1
            
        else:
            #str_new += (prev_char + str(count))
            str_list.append(old_char) #O(1) amortized
            str_list.append(str(count)) 

            j = i
            count = 1 

        #NOTE: could do this outside of loop, but "feels" less
        # elegant and more hacky!
        #If last character in string
        if i == (len(str_in) - 1):
            str_list.append(old_char)
            str_list.append(str(count))
    
    if len(str_in) <= len(str_list):
        #If new is no shorter than old, just keep the old
        return str_in
    else:
        #Return the new string if it's shorter!
        str_new = "".join(str_list) #O(n) to copy list of chars to string
        return str_new

def string_compression(str_in):

    str_new = ""
    
    prev_char = None #tracks previous character marked for repetition
    count = 0
    
    for i in range(len(str_in)):
        new_char = str_in[i]

        if prev_char == new_char:
            count += 1
            
        else:
            #Don't append for first char!
            if prev_char != None:
                str_new += (prev_char + str(count))

            prev_char = new_char
            count = 1 #1 since new character registered in this iteration

        #NOTE: could do this outside of loop, but "feels" less
        # elegant and more hacky!
        #If last character in string
        if i == (len(str_in) - 1):
            str_new += (prev_char + str(count))
    
    if len(str_in) <= len(str_new):
        #If new is no shorter than old, just keep the old
        return str_in
    else:
        #Return the new string if it's shorter!
        return str_new

def string_compression_harness(func):

    print("Testing function: ", func.__name__)
    print(func("")) #1) "" -> base case: treated as same length
    print(func("a")) #)2 "a" -> "a1" would be longer
    print(func("aa")) #)3 "aa" -> "a2" would be same length
    print(func("aaa")) #)4 "a3" -> *orig* would be longer
    print(func("aaabbaaacccc")) #5 "a3b2a3c4" -> *orig* would be longer
    print(func("aaabbc")) #6) "aaabbc" -> "a3b2c1" would be same length

if __name__ == "__main__":

    string_compression_harness(string_compression)

    string_compression_harness(string_compression_improved)
