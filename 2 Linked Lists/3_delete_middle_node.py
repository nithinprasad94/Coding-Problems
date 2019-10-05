#Author: Nithin Prasad
#Date Created: 30/09/2019
#Program Name: delete_middle_node.py
#Program Description: this program allows one to delete A middle node in a
# linked list, given ONLY that deletable node!

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

#NOTE: O(1) time and space complexity!
def delete_middle_node(del_node):

    if del_node == None:
        return
    #if not the last node in the list ..... (list of length 1 OR
    # of length 2 with this as the second node)
    if del_node.nxt != None:

        del_node.val = del_node.nxt.val
        del_node.nxt = del_node.nxt.nxt        

    return

def delete_middle_node_test(func):

    print("Testing function: ", func.__name__)

    head = create_LL(None)
    print_LL(head)
    func(head)
    print_LL(head) #None

    head = create_LL([1])
    print_LL(head)
    func(head)
    print_LL(head) #[1] (unchanged)

    head = create_LL([1,2])
    print_LL(head)
    func(head.nxt)
    print_LL(head) #[1,2] (unchanged)

    head = create_LL([1,2,3,4,5])
    print_LL(head)
    func(head.nxt.nxt)
    print_LL(head) #[1,2,4,5]

    head = create_LL([1,2,3,4,5,6])
    print_LL(head)
    func(head.nxt.nxt.nxt) 
    print_LL(head) #[1,2,3,5,6]
    

if __name__ == "__main__":

    delete_middle_node_test(delete_middle_node)

    
