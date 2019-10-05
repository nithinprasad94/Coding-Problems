#Author: Nithin Prasad
#Date Created: 29/09/2019
#Program Name: zero_matrix.py
#Program Description: Given an MxN matrix, this program returns the given
# matrix with rows and columns containing a 0 (initially) set to 0.

#Note: solution is of O(n^2) in time and O(n) in space. We use the matrix
# itself as data storage to reduce spatial storage to O(1).
def zero_matrix(matrix_in):

    m = len(matrix_in)
    if m == 0:
        return matrix_in
    n = len(matrix_in[0])

    #Special flags to check if first row or col have zeros
    row_has_zeros = False
    col_has_zeros = False

    #Check for 0 col..
    for i in range(m):
        if matrix_in[i][0] == 0:
            col_has_zeros = True

    #Check for 0 row..
    for j in range(n):
        if matrix_in[0][j] == 0:
            row_has_zeros = True

    #Iterate through matrix elements (1,1)->(m,n) and set 0s in headers
    for i in range(1,m):
        for j in range(1,n):
            if matrix_in[i][j] == 0:
                #If an element is 0, we want to zero that row's header
                # and that column's header to 0. 
                matrix_in[i][0] = None #row header set to None
                matrix_in[0][j] = None #col header set to None
                
    #Now only populate rows with zeroes and ignore the None valued elements
    for i in range(1,m):
        if matrix_in[i][0] == 0:
            for j in range(n):
                matrix_in[i][j] = 0

    #Now only populate columns with zeroes
    for j in range(1,n):
            if matrix_in[0][j] == 0:
                for i in range(m):
                    matrix_in[i][j] = 0

    if row_has_zeros:
        for j in range(n):
            matrix_in[0][j] = 0
    if col_has_zeros:
        for i in range(m):
            matrix_in[i][0] = 0
                    
    return matrix_in

def zero_matrix_test(func):

    print("Testing function: ", func.__name__)
    matrix = []
    print_matrix(func(matrix))
    matrix = [[0]]
    print_matrix(func(matrix))
    matrix = [[1]]
    print_matrix(func(matrix))
    matrix = [[1,2]]
    print_matrix(func(matrix))
    matrix = [[3],[0]]
    print_matrix(func(matrix))
    matrix = [[1,2,0],[3,4,5],[6,7,8],[0,9,10]]
    print_matrix(func(matrix))

def print_matrix(matrix_in):
    print("---------------------")
    m = len(matrix_in)
    if m > 0:
        n = len(matrix_in[0])

        for i in range(m):
            vec = ""
            for j in range(n):
                vec += ("%3s" % matrix_in[i][j]) + " "
            print(vec)
    else:
        print("")

if __name__ == "__main__":

    zero_matrix_test(zero_matrix)
