#Author: Nithin Prasad
#Date Created: 26/09/2019
#Program Name: urlify.py
#Program Description: (CTCI 1.3) Given an input string, replace all spaces
# in string with '%20'. Assume string has sufficient space at the end to
# store additional characters, and you are given true length of the string.

#NOTE: this is the Python-based solution
#NOTE: Algorithmic complexity is O(n) time, O(n) space
def urlify(str_in, true_length):

    new_str = ""

    #Iterate through list elements till index exceeds true_length
    i = 0
    
    while i < true_length:

        elem = str_in[i]
        if elem == " ":
            new_str += "%20"
        else:
            new_str += elem

        i += 1

    return new_str

#What if we want to implement the sort IN PLACE (no extra space)
def urlify_in_place(str_in, true_length):

    str_list = list(str_in) #Assume this is what was given to us ...
    
    #Iterate through list in reverse, replace all spaces by %20
    j = len(str_list) - 1 #initalize to last element in list

    i = true_length - 1 #Start @ last non-buffer character in string

    #print("string:",str_in)
    #print("True Length:", true_length)
    #print("Length of string:", len(str_list))
    #print("j init:", j)
    #print("i init:", i)
    #print("Init: ","i:",i,"j:",j,"list",str_list)

    while i >= 0 and j >= 0:

        if str_list[i] == " ":
            str_list[j-2] = "%"
            str_list[j-1] = "2"
            str_list[j] = "0"
            j -= 3
        else:
            str_list[j] = str_list[i]
            j -= 1
        #print("i:",i,"j:",j,"list",str_list)

        i -= 1

    return "".join(str_list)

def urlify_harness(func):

    print("Testing function: ", func.__name__)
    print("Output:",func("",0)) #Output: ""
    print("Output:",func("   ",1)) #Output: "%20"
    print("Output:",func(" aegis  ",6)) #Output: "%20aegis"
    print("Output:",func("aegis of zhonya    ",15)) #Output: "aegis%20of%20zhonya"
    print("Output:",func("  ae gis      ",8)) #Output: "%20%20ae%20gis%"
    print("")
    
if __name__ == "__main__":

    urlify_harness(urlify)

    urlify_harness(urlify_in_place)
    
