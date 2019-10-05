#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: partition.py
#Program Description: given a linked list and a value x, mod the list
# such that all numbers < x appear before all numbers >= x. Partion,
# val need not exactly come inbetween left and right partitions

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

#NOTE: A good alternative: create a new list, and add the elements less
# than x to the tail, and numbers >= x to the head! (Doesn't preserve
# order but that doesn't matter; not specified!)
#NOTE: solution runs in O(n) time.
def partition(head_LL, x):

    #Handle list lengths 0 and 1
    if head_LL == None:
        return None
    if head_LL.nxt == None:
        return head_LL

    #Set a lower and upper starter
    lower_head = None
    lower_curr = None
    upper_head = None
    upper_curr = None

    curr = head_LL

    while curr != None:
        #print("LOOOPING")

        #Pop curr node from linked list and hold it in tmp node
        tmp = curr
        curr = curr.nxt
        tmp.nxt = None #Break this node off the chain!

        if tmp.val < x:
            #print("if")
            #Handle cases where lower is still None OR it has node(s) pres.
            if lower_head == None:
                #print("if->if")
                lower_head = tmp
                lower_curr = tmp
            else:
                #print("if->else")
                lower_curr.nxt = tmp
                lower_curr = lower_curr.nxt #iterate to tmp
        else:
            #print("else")
            #Handle cases where upper is still None OR it has node(s) pres.
            if upper_head == None:
                #print("else->if")
                upper_head = tmp
                upper_curr = tmp
            else:
                #print("else->else")
                upper_curr.nxt = tmp
                upper_curr = upper_curr.nxt #iterate to tmp
                
        #print("Upper Head: ")
        #print_LL(upper_head)
        #print("Lower Head: ")
        #print_LL(lower_head)

    #Handle merges of the 2 partitions
    if lower_head == None:
        head_LL = upper_head
    elif upper_head == None:
        head_LL = lower_head
    else:
        #print("in else ..")
        #print("printing lower head ...")
        #print_LL(lower_head)
        #print("printing upper head ...")
        #print_LL(upper_head)
        lower_curr.nxt = upper_head
        #print("printing lower head ...")
        #print_LL(lower_head)
        #print("printing upper head ...")
        #print_LL(upper_head)
        head_LL = lower_head
        #print("printing entire linked list!")
        #print_LL(head_LL)
        #print("head.val: ", str(head_LL.val))
        #print("head.nxt.val: ", str(head_LL.nxt.val))

    return head_LL
    

def partition_test(func):

    print("Testing function: ", func.__name__)

    print("\n========================")
    head = create_LL(None)
    print_LL(head)
    x = 3
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #None

    print("\n========================")
    head = create_LL([1])
    print_LL(head)
    x = 3
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #[1] (unchanged)

    print("\n========================")
    head = create_LL([4,1])
    print_LL(head)
    x = 3
    head = func(head,x)
    print("x = ",x)
    print_LL(head)#[1,4] 

    print("\n========================")
    head = create_LL([3,4,1,7,5])
    print_LL(head)
    x = 3
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #eg. [1,3,4,7,5]

    print("\n========================")
    head = create_LL([1,2,3,4,5])
    print_LL(head)
    x = 3
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #[1,2,3,4,5] (unchanged?)

    print("\n========================")
    head = create_LL([1,2,3,4,5])
    print_LL(head)
    x = 6
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #[1,2,3,4,5] (unchanged?)

    print("\n========================")
    head = create_LL([1,2,3,4,5])
    print_LL(head)
    x = 0
    head = func(head,x)
    print("x = ",x) 
    print_LL(head) #[1,2,3,4,5] (unchanged?)

    print("\n========================")
    head = create_LL([3,4,6,1,8,9,10,8,8,7,3,5])
    print_LL(head)
    x = 8
    head = func(head,x)
    print("x = ",x)
    print_LL(head) #[3,4,6,2,7,3,5,8,9,10,8,8] 

if __name__ == "__main__":

    partition_test(partition)
