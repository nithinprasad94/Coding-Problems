#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: remove_dups.py
#Program Description: Given an unsorted linked list, this code removes
# duplicates from the list, and returns the new list.

class LL_Node:

    val = None
    nxt = None

    def __init__(self,input_val, next_node):

        self.val = input_val
        self.nxt = next_node
    

#Assume nodes having integer values for this problem
#NOTE: O(n) time with tmp buffer, O(n) space
def remove_dups(head_LL):

    #Simple case 0 or 1 element linked list
    if head_LL == None or head_LL.nxt == None:
        return head_LL
    
    unique_vals = {}

    #Preliminary check
    if head_LL.val == head_LL.nxt.val:
        tmp = head_LL.nxt.val #Tmp node reference
        head_LL.nxt = head_LL.nxt.nxt #Node bypass
        tmp = None #In Python, this node will be freed automatically

    unique_vals[head_LL.val] = 1

    curr = head_LL
    lead = head_LL.nxt
    
    while lead != None:

        #print("Dict: ", unique_vals)
        #print("Processing lead.val: ", lead.val)
        if lead.val in unique_vals.keys():
            #print(">>>>>Popping: ", lead.val)
            #Pop node
            tmp = lead
            lead = lead.nxt
            curr.nxt = lead
            tmp = None
        else:
            unique_vals[lead.val] = 1

            curr = lead
            lead = lead.nxt

    #since a pointer to the list was passed in, modifying the LL here
    # modifies it in the calling function
    #return head_LL

#W/O temp buffer: O(n^2) time without tmp buffer, O(1) space
def remove_dups_no_buff(head_LL):

    #Simple case 0 or 1 element linked list
    if head_LL == None or head_LL.nxt == None:
        return head_LL
    
    #unique_vals = {}

    #Preliminary check
    if head_LL.val == head_LL.nxt.val:
        tmp = head_LL.nxt.val #Tmp node reference
        head_LL.nxt = head_LL.nxt.nxt #Node bypass
        tmp = None #In Python, this node will be freed automatically

    #unique_vals[head_LL.val] = 1

    lead = head_LL #Runner starts from head_LL.nxt
    
    while lead != None:

        #print("Dict: ", unique_vals)
        #print("Processing lead.val: ", lead.val)
        trailer = lead
        runner = lead.nxt
        
        while (runner != None):

            if runner.val == lead.val:
                tmp = runner
                trailer.nxt = runner.nxt
                runner = runner.nxt
                tmp = None

            else:
                runner = runner.nxt
                trailer = trailer.nxt

        lead = lead.nxt
                
            

    #return head_LL

    
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

            new_node = LL_Node(inp_list[i],None) #create a new object
            curr.nxt = new_node #Grow LL by 1 node
            curr = new_node #create new node

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
        
def remove_dups_test(func):

    print("Testing function: ", func.__name__)
    head = create_LL(None)
    print_LL(head)
    func(head)
    print_LL(head)

    head = create_LL([])
    print_LL(head)
    func(head)
    print_LL(head)
    
    head = create_LL([3])
    print_LL(head)
    func(head)
    print_LL(head)
    
    head = create_LL([1,1,1,3,4,2,2,4,8,7,5,5,5])
    print_LL(head)
    func(head)
    print_LL(head)
    
    head = create_LL([1,2,3,4,2,5,3,6,7,3,4,8])
    print_LL(head)
    func(head)
    print_LL(head)
    

if __name__ == "__main__":

    remove_dups_test(remove_dups)
    remove_dups_test(remove_dups_no_buff)
