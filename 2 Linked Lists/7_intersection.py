#Author: Nithin Prasad
#Date Created: 04/10/2019
#Program Name: intersection.py
#Programm Description: Given 2 Singly Linked Lists, determines if the 2
# lists intersect!

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

def print_LL(head, addr=False):

    if (head == None):
        print("<Empty Linked List>")
        return

    curr = head
    str_LL = ""
    while curr != None:
        if (addr):
            str_LL += str(curr)
        else:
            str_LL += str(curr.val)
        if curr.nxt != None:
            str_LL += " -> "        
        curr = curr.nxt

    print(str_LL)
    return

#NOTE: algorithm can be implemented in O(A+B) time and O(n) space!
#NOTE: Intersection of 2 Linked Lists defined as having the same node
# memory-wise not value-wise) from some point in both lists till the end of
# each list. Ie. they share all nodes after some point k in each list!
#NOTE: next time, do an iterative solution which would only req. O(1) space!
def intersection(head_1, head_2):

    #Can't 1 or more empty lists!
    if head_1 == None or head_2 == None:
        return None

    count_1 = 0
    count_2 = 0

    curr_1 = head_1
    curr_2 = head_2

    #Obtain counter difference between the 2 lists (ie. diff in # of elems
    # in each list)
    while not(curr_1 == None and curr_2 == None):

        if curr_1 != None:
            curr_1 = curr_1.nxt
        else:
            count_1 += 1

        if curr_2 != None:
            curr_2 = curr_2.nxt
        else:
            count_2 += 1

    #print("Count 1: ",count_1,"Count 2:",count_2)

    #Make a recursive call to get the intersecting node!
    depth = 0 #Tester variable
    (dummy_bool, intersecting_node) = intersection_helper(head_1, head_2, count_1, count_2,depth)
    return intersecting_node

def intersection_helper(curr_1, curr_2, count_1, count_2,depth):
    depth += 1

    #print("Depth: ", depth)
    #if curr_1 != None and curr_2 != None:
    #    print("L1 Node:",curr_1,"L1 Val:", curr_1.val)
    #    print("L2 Node:",curr_2,"L2 Val:", curr_2.val)
    #else:
    #    print("L1 Node:",curr_1,"L2 Node:",curr_2)
    
    #If we reach terminating node ...
    if curr_1.nxt == None and curr_2.nxt == None:

        #Return!
        if curr_1 == curr_2:
            return (True, curr_1) #Return node identity
        else:
            return (False, None) #Return None (node doesn't matter)

    #Otherwise...

    #First check if existing nodes are comparable
    if count_1 != 0:
        count_1 -= 1 #forward processing, move to 'equalize nodes'
        curr_1_next = curr_1 #Hold node
        curr_2_next = curr_2.nxt #Advance noce
    elif count_2 != 0:
        count_2 -= 1 #forward processing, move to 'equalize nodes'
        curr_1_next = curr_1.nxt #Advance node
        curr_2_next = curr_2 #Hold node
    else:
        curr_1_next = curr_1.nxt
        curr_2_next = curr_2.nxt
       
    (ret_val, ret_node) = intersection_helper(curr_1_next,curr_2_next,count_1,count_2,depth)
    #print("Depth: ",depth)
    #print("Ret_val:",ret_val,"Ret_node:",ret_node)
    
    if ret_val == False:        
        return (False, ret_node)
    else:
        if curr_1 == curr_2:
            return (True, curr_1)
        else:
            return (False, ret_node)

def intersection_test(func): 

    print("Testing function: ", func.__name__)

    print("\n-----------------------------------------------")
    list_int = []
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = LL_Node(4,None)
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return None
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,2,3]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = LL_Node(4,LL1.nxt)
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return 2
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,5]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = LL_Node(4,LL1.nxt)
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return 5
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,2,3]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = LL_Node(4,LL1)
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return 1
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,2,3,4]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = create_LL([5,3,4])
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return None
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,2,3,8,7,5]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = LL_Node(4,LL_Node(3,LL1.nxt.nxt.nxt))
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return 8
    print((func(LL1,LL2)))

    print("\n-----------------------------------------------")
    list_int = [1,2,3]
    LL1 = create_LL(list_int)
    print_LL(LL1)
    print_LL(LL1,True)
    LL2 = create_LL([1,2,3])
    print_LL(LL2)
    print_LL(LL2,True)
    if (func(LL1,LL2)) != None:
        print((func(LL1,LL2)).val) #Should return None
    print((func(LL1,LL2)))
    
    return

if __name__ == "__main__":

    intersection_test(intersection)
