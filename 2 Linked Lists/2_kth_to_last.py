#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: kth_to_last.py
#Program Description: Given a linked list and an element k, return its
# kth last element, should one exist.

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

#NOTE: could implement a recursive solution at the cost of O(n) space.
#NOTE: current complexity is O(n) time and O(1) space.
def kth_to_last(head_LL, k):

    #Trivial if list has 0 or 1 nodes
    if head_LL == None:
        return None
    elif head_LL.nxt == None:
        if k == 0:
            return head_LL
        else:
            return None

    #For k > 1 node ...
    trail = head_LL
    lead = head_LL #Start them identically to one another
    i = 1 #if k = 1, then we only need the last node! (trail = lead)

    #Setup a distance of k between
    while i < k and lead.nxt != None:

        lead = lead.nxt
        i += 1

    #List shorter than k nodes!
    if i != k:
        return None

    #if lead.nxt is none, then lead is the last node ... trail is the
    # kth last node! Terminate!
    while lead.nxt != None:

        trail = trail.nxt
        lead = lead.nxt       
    
    return trail

def kth_to_last_test(func):

    print("Testing function: ", func.__name__)
    head = create_LL(None)
    k = 3
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, None
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out) 

    head = create_LL([1])
    k = 3
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, None
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out)

    head = create_LL([1,2])
    k = 3
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, None
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out) 

    head = create_LL([1,2,3])
    k = 3
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, None
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out)         

    head = create_LL([1,2,3,4,5,6])
    k = 3
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, 4
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out) 

    head = create_LL([1,10,100,1000,999,99,9,8,88,888])
    k = 7
    print_LL(head)
    node_out = func(head,k)
    if node_out != None: #3rd last, 4
        print(str(k) + "th last node:", node_out.val) 
    else:
        print(str(k) + "th last node:", node_out)
        
if __name__ == "__main__":

    kth_to_last_test(kth_to_last)

    



