#Author: Nithin Prasad
#Date Created: 04/10/2019
#Program Name: intersection.py
#Programm Description: Given a circular linked list, this program returns
# the node at the beginning of the loop!

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

def print_LL(head, addr=False,bounds=10000):

    if (head == None):
        print("<Empty Linked List>")
        return

    curr = head
    str_LL = ""
    count = 0
    
    while curr != None and count < bounds:
        if (addr):
            str_LL += str(curr)
        else:
            str_LL += str(curr.val)
        if curr.nxt != None:
            str_LL += " -> "        
        curr = curr.nxt
        count += 1

    if (count >= bounds):
        print("MAY HAVE CYCLIC LINKED LIST!")

    print(str_LL)
    return

#NOTE: Time complexity O(n), Space complexity O(n) via a Hash Table
def loop_detection(head_in):

    if head_in == None:
        return None
    if head_in.nxt == None:
        return None

    #Otherwise, a loop may exist! Iterate through the LL to find the
    # 'start' of the loop!

    dict_nodes = {}

    #print("Hello?")
    #return
    curr = head_in
    
    #print("Pree loop")
    while curr != None:
        #print("In loop!")

        if curr in dict_nodes:
            return curr
        else:
            dict_nodes[curr] = 1
            
        curr = curr.nxt

    #Only gets here if list of finite length and has no loops!
    return None

#NOTE: Time complexity O(n)
def loop_detection_opt(head_in):

    #1) Do runner method at rate 1,2 till collision occurs. In a list of
    # size k (non-loop) and L (size of loop), collision occurs at L-k = K.
    incr_1 = 1
    incr_2 = 2

    ptr_1 = head_in
    ptr_2 = head_in

    while (ptr_1 != ptr_2):

        incr_1_tmp = incr_1
        incr_2_tmp = incr_2

        #Increment by increment amounts
        while incr_1_tmp != 0:
            ptr_1 = ptr_1.nxt
            incr_1_tmp -= 1
        while incr_2_tmp != 0:
            ptr_2 = ptr_2.nxt
            incr_2_tmp -= 1
       
    #2) Set p2 to LLHead and move pointers at rate 1,1 till collision
    # occurs again! At this time, p1 moves k nodes to start of loop, and p2
    # moves K + m*L = k nodes to start of loop! Return this node!
    ptr_2 = head_in

    while (ptr_1 != ptr_2):

        incr_1_tmp = incr_1
        incr_2_tmp = incr_2

        #Increment by increment amounts
        while incr_1_tmp != 0:
            ptr_1 = ptr_1.nxt
            incr_1_tmp -= 1
        while incr_2_tmp != 0:
            ptr_2 = ptr_2.nxt
            incr_2_tmp -= 1

    return ptr_1    

def loop_detection_test(func):

    print("Testing function: ", func.__name__)

    print("\n---------------------------------------------------")
    vals = [1]
    LL = create_LL(vals)
    LL.nxt = LL #create a loop to first node itself!
    print_LL(LL,False,10)
    node = (loop_detection(LL)) #prints 1 (first node)
    if node != None:
        print(node.val)
    print(node)

    print("\n---------------------------------------------------")
    vals = [1,3,4,6,8]
    LL = create_LL(vals)
    (LL.nxt.nxt.nxt.nxt).nxt = LL.nxt.nxt
    print_LL(LL,False,10)
    node = (loop_detection(LL)) #prints 4 (3rd node)
    if node != None:
        print(node.val)
    print(node)

    print("\n---------------------------------------------------")
    vals = [1,3,9,8,1,2]
    LL = create_LL(vals)
    (LL.nxt.nxt.nxt.nxt.nxt).nxt = LL.nxt.nxt.nxt 
    print_LL(LL,False,10)
    node = (loop_detection(LL)) #prints 8 (4th Node)
    if node != None:
        print(node.val)
    print(node)
    
if __name__ == "__main__":

    loop_detection_test(loop_detection)
    loop_detection_test(loop_detection_opt)
