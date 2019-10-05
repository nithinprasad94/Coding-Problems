#Author: Nithin Prasad
#Date Created: 29/09/2019
#Program Name: rotate_matrix.py
#Program Description: Given an NxN matrix (of image), where each pixel is
# 4 bytes, rotate the image by 90 degrees. Do it in place?!

#NOTE: Assume we rotate right.
#NOTE: simple method assumes we return a new rotated-matrix, but this
# requires O(n^2) space to be created and then stored in ...
# Thus we use a new method that operates in place requires only O(1)
# extra space max. Both algorithms require O(n^2) time!
def rotate_matrix(matrix_in):

    n = len(matrix_in)

    if n <= 1:
        print_matrix(matrix_in)
        return matrix_in

    #Generate empty n*n matrix
    new_matrix = []
    for i in range(n):
        vector = []
        for j in range(n):
            vector.append("-")
        new_matrix.append(vector)

    n_last = n-1 #End index for any element within the layer with respect
          # to the layer

    #Iterate through every layer in decreasing order (n->1 (inclusive)) ...
    # -> decrease n by 2 each time (remove 1 element from either side of
    # the center of the matrix (in each dimension).
    for i in range(n,0,-2):
        #i represents the dimension of that layer = number of elements
        # along a side of the layer. A layer is hollow!
        offset = int((n-i)/2) #Offset from edge of each matrix for the layer
        #print("n:",n,"i:",i,"offset:",offset)

        i_last = i-1 #Number of iterable indices in layer wall

        #Iterate through indices: 0 -> i-2 (inclusive) => i-1 elements total
        for j in range(0,i_last):
            #print("n:",n,"offset:",offset,"j:",j)
            #print("j:",j)
            
            #Generate right wall FROM top wall!
            new_matrix[j+offset][n_last-offset] = matrix_in[offset][j+offset]
            #Generate bottom wall FROM right wall!
            new_matrix[n_last-offset][n_last-offset-j] = matrix_in[j+offset][n_last-offset]
            #Generate left wall FROM bottom wall!
            new_matrix[n_last-offset-j][offset] = matrix_in[n_last-offset][n_last-offset-j]
            #Generate top wall FROM left wall!
            new_matrix[offset][j+offset] = matrix_in[n_last-offset-j][offset]

    return new_matrix

def rotate_matrix_inplace(matrix_in):

    n = len(matrix_in)

    if n <= 1:
        return matrix_in

    n_last = n-1 #End index for any element within the layer with respect
          # to the layer
    #print("----------------------")
    #Iterate through every layer in decreasing order (n->1 (inclusive)) ...
    # -> decrease n by 2 each time (remove 1 element from either side of
    # the center of the matrix (in each dimension).
    for i in range(n,0,-2):
        #i represents the dimension of that layer = number of elements
        # along a side of the layer. A layer is hollow!
        offset = int((n-i)/2) #Offset from edge of each matrix for the layer
        #print("n:",n,"i:",i,"offset:",offset)

        i_last = i-1 #number of iterable indices in layer wall
        
        #Iterate through indices: 0 -> i-2 (inclusive) => i-1 elements total
        for j in range(0,i_last):
            #print_matrix(matrix_in)
            #print("n:",n,"offset:",offset,"j:",j)
            #print("j:",j)

            #Save a tmp as right element ...
            tmp = int(matrix_in[j+offset][n_last-offset])
            #Generate top -> right
            matrix_in[j+offset][n_last-offset] = int(matrix_in[offset][j+offset])
            #Generate left -> top
            matrix_in[offset][j+offset] = int(matrix_in[n_last-offset-j][offset])
            #Generate bottom -> left
            matrix_in[n_last-offset-j][offset] = int(matrix_in[n_last-offset][n_last-offset-j])
            #Generate right -> bottom
            matrix_in[n_last-offset][n_last-offset-j] = tmp
    #print("YOLO")
    return matrix_in

def print_matrix(matrix_in):
    print("----------------------")
    n = len(matrix_in)

    for i in range(n):
        row = ""
        for j in range(n):
            row += ("%3s" % str(matrix_in[i][j])) + " "
        print(row)

def rotate_matrix_test(func):

    matrix = [] #1) ___ -> returns new empty matrix (base case)
    print_matrix(func(matrix))
    matrix = [[1]] #2) 1 -> unchanged matrix of 1x1
    print_matrix(func(matrix))
    matrix = [[1,2],[3,4]] #3) 3 1, 2 4
    print_matrix(func(matrix))
    matrix = [[1,2,3],[4,5,6],[7,8,9]] #4) 7 4 1, 8 5 2, 9 6 3
    print_matrix(func(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #5) 13 9 5 1...
    print_matrix(func(matrix))
    matrix = []
    for i in range(20):
        vec = []
        for j in range(20):
            vec.append((i*20+(j+1)))
        matrix.append(vec)
    print_matrix(func(matrix))
    
if __name__ == "__main__":

    #rotate_matrix_test(rotate_matrix)
    rotate_matrix_test(rotate_matrix_inplace)
