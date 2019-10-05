#Author: Nithin Prasad
#Date Created: 03/10/2019
#Program Name: palindrome.py
#Program Description: Given an input Linked List, this program checks if
# it is a palindrome or not, and returns a boolean

class LL_Node:

    val = None
    nxt = None

    def __init__(self,input_val, next_node):

        self.val = input_val
        self.nxt = next_node

def create_LL(inp_list):

    if inp_list == None:
        return None

    len_list = len(inp_list)

    if len_list == 0:
        return None

    head = LL_Node(inp_list[0],None)
    curr = head

    if len_list > 0:
        for i in range(1,len_list):

            new_node = LL_Node(inp_list[i],None)
            curr.nxt = new_node
            curr = new_node

    return head

def print_LL(head):

    if (head == None):
        print("<Empty Linked List>")
        return

    curr = head
    str_LL = ""
    while curr != None:
        str_LL += str(curr.val)
        if curr.nxt != None:
            str_LL += " -> "        
        curr = curr.nxt

    print(str_LL)
    return

#NOTE: Algorithm is O(n) in time (despite the 2 for loops!) and
# O(n) in space!
#NOTE: REDO PROBLEM NEXT TIME WITH DIFF. APPROACH (eg. Recursion)
def palindrome(head_inp):

    #Base case: declare palindrome if input of size 0 or 1
    if head_inp == None:
        return True
    if head_inp.nxt == None:
        return True

    #All other cases
    dict_vals = {}

    curr = head_inp
    index = 0

    #Iterate through entire LL and store each node's index by key as
    # node.val into the dictionary
    while curr != None:

        if curr.val in dict_vals:
            dict_vals[curr.val].append(index)

        else:
            dict_vals[curr.val] = [index]

        curr = curr.nxt
        index += 1

    length = index #Index increments one per linked list element ...
        #Thus it counts 1 more than the index of the last LL element!
    half_mark = (length-1)/2 #Because indexing starts at 0!
    #print("Half mark: ",half_mark)

    #Iterate through every key in the dictionary (corresponding to a node
    # val) and check for mirroring around the center point! Allow up to
    # one node without a mirror (would work only if number of elements in
    # linked list is ODD

    allowable_singles = 0
    if length%2 == 1:
        allowable_singles = 1

    for key in dict_vals.keys():

        indices = dict_vals[key]

        #Check for odd-number of indices in list when singles aren't allowed
        if len(indices)%2 == 1 and allowable_singles == 0:
            #print("hereee")
            return False
        elif len(indices)%2 == 1 and allowable_singles == 1:
            allowable_singles = 0

        #print("Key: ",key,"Indices: ",indices)
        #Iterate through indices
        for i in range(len(indices)):

            list_index = indices[i]
            list_index_mirr = indices[(-1)-i] #Last ith element
            #print("List_index: ", list_index, "List_index_mirr: ",list_index_mirr)
            #print("Half_mark: ", half_mark)
            if list_index > half_mark:
                break #Exit loop if we've checked halfway through the list

            if (list_index-half_mark) != (half_mark-list_index_mirr):
                
                #print("Hereeeeeeee")
                return False

    return True

def palindrome_test(func):

    print("Testing function:",func.__name__)

    print("\n----------------------------------------")
    sample_list = []
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #True

    print("\n----------------------------------------")
    sample_list = [1]
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #True

    print("\n----------------------------------------")
    sample_list = [1,2,3,2,1]
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #True

    print("\n----------------------------------------")
    sample_list = [1,2,3,2,5]
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #False

    print("\n----------------------------------------")
    sample_list = [1,2,2,3,1]
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #False

    print("\n----------------------------------------")
    sample_list = [1,2,3,4,2,1]
    sample_LL = create_LL(sample_list)
    print_LL(sample_LL)
    print(palindrome(sample_LL)) #False
    
if __name__ == "__main__":

    palindrome_test(palindrome)



