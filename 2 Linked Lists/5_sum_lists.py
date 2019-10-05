#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: sum_lists.py
#Program Description: given 2 linked lists, where each node represents a
# digit of a number, solve the sum of both linked lists, if the lists are
# ordered (i) units position as head, and (ii) units position as tail

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

#NOTE: This is considered "reverse order"
def sum_lists_reverse(head1, head2):

    list1_digits = []
    list2_digits = []
    val1 = 0
    val2 = 0

    if head1 == None:
        val1 = 0

    if head2 == None:
        val2 = 0

    curr1 = head1
    curr2 = head2
    
    #Iterate through the linked lists
    while (curr1 != None) or (curr2 != None):
        if (curr1 != None):
            list1_digits.append(curr1.val)
            curr1 = curr1.nxt
        if (curr2 != None):
            list2_digits.append(curr2.val)
            curr2 = curr2.nxt

    #print("List 1 digits: ",list1_digits)
    #print("List 2 digits: ",list2_digits)

    #Generate sums
    for i in range(len(list1_digits)):
        val1 += list1_digits[i]*(10**i)
    
    for i in range(len(list2_digits)):
        val2 += list2_digits[i]*(10**i)

    #print(str(val1), str(val2))

    sum_lists = val1 + val2
    list_sum = list(str(sum_lists))
    #print(list_sum)

    new_head = LL_Node(list_sum[-1],None)
    curr = new_head
    
    for i in range(len(list_sum)-2,-1,-1):
        elem = list_sum[i]
        new_node = LL_Node(int(elem),None)
        curr.nxt = new_node
        curr = new_node

    return new_head        

#NOTE: Code is O(n) in time and O(n) in space
#Optimized version (recursion)
def sum_lists_reverse_opt(head1, head2):

    carry = 0
    head_out = LL_Node(0,None) #Dummy node created at the start
    curr_out = head_out
    
    #Invoke recursive call
    recursive_reverse_add(head1, head2, carry, head_out, curr_out)

    head_out = head_out.nxt
    
    return head_out

#Recursive addition on each set of digits ...
def recursive_reverse_add(curr_A, curr_B, carry, head_O, curr_O):
##    print("IN Recursive call ....!!!!")
##    print("Type(curr_A): ",type(curr_A))
##    print("Type(curr_B): ",type(curr_B))

    #Return if both heads are None!
    if curr_A == None and curr_B == None:

        #Make a new output node if the carry is nonzero ...
        if carry != 0:
            new_node = LL_Node(int(carry),None)
            curr_O.nxt = new_node                    

        #return head_O
        return

    val_A = 0 #Default value if head is None
    val_B = 0

    if curr_A != None:
        val_A = curr_A.val
    if curr_B != None:
        val_B = curr_B.val

    #Compute the sum
    sum_digits = carry + val_A + val_B

    #Advance input list pointers
    if curr_A != None:
        curr_A = curr_A.nxt
    if curr_B != None:
        curr_B = curr_B.nxt

    new_carry = 0
    if sum_digits >= 10:
        new_carry = 1
        
    #Assign new node and advance output node, if it isn't the first in the list
    new_node = LL_Node(int(sum_digits%10),None)

    curr_O.nxt = new_node
    curr_O = curr_O.nxt

    #print_LL(head_O)

    #Recursive call
    recursive_reverse_add(curr_A, curr_B, new_carry, head_O, curr_O)
    
    #print_LL(head_O)
    return head_O

#NOTE: Alg. is O(n) in time, and O(n) in space.
#Optimized version (recursion)
def sum_lists_forward(head1, head2):

    head_out = None
    curr_out = None

    skip1 = 0
    skip2 = 0

    #If lists are not equal lengths, we need to move that list's skip counter
    # by 1 per length deficience of 1.

    curr1 = head1
    curr2 = head2
    
    while (not(curr1 == None and curr2 == None)):

        if curr1 == None:
            skip1 += 1
        else:
            curr1 = curr1.nxt
        if curr2 == None:
            skip2 += 1
        else:
            curr2 = curr2.nxt
            

    print("Skip1: ",skip1,"Skip2:",skip2)
    
    #Invoke recursive call
    (head_out,carry) = recursive_forward_add(head1, head2, skip1, skip2)

    if carry != 0:
        new_node = LL_Node(carry,head_out)
        head_out = new_node
    
    return head_out

#Recursive function for forward add
def recursive_forward_add(curr_A, curr_B, skip_A, skip_B):

    #Return when we're at the end of both lists ...
    if curr_A == None and curr_B == None:
        return (None,0)

    dig_A = 0
    dig_B = 0

    #Process skips and values of adding digits
    if skip_A > 0:
        skip_A -= 1
    else:
        dig_A = curr_A.val
        curr_A = curr_A.nxt

    if skip_B > 0:
        skip_B -= 1
    else:
        dig_B = curr_B.val
        curr_B = curr_B.nxt

    #Recursively call function on smaller digits and get carry_out and
    # head_out
    (head_sum, carry_in) = recursive_forward_add(curr_A, curr_B, skip_A, skip_B)

    digit_sum = carry_in + dig_A + dig_B

    carry_out = int(digit_sum/10)

    #Create new output node, place place it into head_sum at the start!
    new_node = LL_Node(int(digit_sum%10), head_sum)
    head_sum = new_node

    return (head_sum, carry_out)
    
def sum_lists_test_forw(func):

    print("Testing function: ", func.__name__)

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL(None)
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List>

    print("\n========================")
    head1 = create_LL([])
    head2 = create_LL([])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL([2,1])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #2 -> 1 ie. 21

    print("\n========================")
    head1 = create_LL([3,8,0,1])
    head2 = create_LL([4,3,2])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #4 -> 2 -> 3 -> 3 ie. 4233

    print("\n========================")
    head1 = create_LL([3,8,0,1])
    head2 = create_LL([6,4,3,2])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #1 -> 0 -> 2 -> 3 -> 3 ie. 10233

def sum_lists_test(func):

    print("Testing function: ", func.__name__)

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL(None)
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List>

    print("\n========================")
    head1 = create_LL([])
    head2 = create_LL([])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL([1,2])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #1 -> 2 ie. 21

    print("\n========================")
    head1 = create_LL([1,0,8,3])
    head2 = create_LL([2,3,4])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #3 -> 3 -> 2 -> 4 ie. 4233

    print("\n========================")
    head1 = create_LL([1,0,8,3])
    head2 = create_LL([2,3,4,6])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #3 -> 3 -> 2 -> 0 -> 1 ie. 10233


def sum_lists_test(func):

    print("Testing function: ", func.__name__)

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL(None)
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List>

    print("\n========================")
    head1 = create_LL([])
    head2 = create_LL([])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #<Empty Linked List

    print("\n========================")
    head1 = create_LL(None)
    head2 = create_LL([1,2])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #1 -> 2 ie. 21

    print("\n========================")
    head1 = create_LL([1,0,8,3])
    head2 = create_LL([2,3,4])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #3 -> 3 -> 2 -> 4 ie. 4233

    print("\n========================")
    head1 = create_LL([1,0,8,3])
    head2 = create_LL([2,3,4,6])
    print_LL(head1)
    print_LL(head2)
    print_LL(func(head1,head2)) #3 -> 3 -> 2 -> 0 -> 1 ie. 10233
    
if __name__ == "__main__":

    sum_lists_test(sum_lists_reverse)
    sum_lists_test(sum_lists_reverse_opt)
    #sum_lists_test_forw(sum_lists_forward)




    
