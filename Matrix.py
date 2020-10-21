import copy

def mat_def():
    name = str(input("Name of the matrix: "))
    m1 = int(input("Enter total number of rows in the matrix: "))
    n1 = int(input("Enter total number of columns in the matrix: "))

    New = [[0 for col in range(n1)]for row in range(m1)]

    print("Enter all elements one after other.")
    for i in range(m1):
        for j in range(n1):
            New[i][j] = int(input(name + str(i+1) + str(j+1)))
    return (name, New)

def mat_print(A):
    for i in range(m1):
        for j in range(n1):
            print(Mat[p][i][j], end = " ")
        print()
    print()

def add(A, B):
    name = str(input("Name of the new matrix is: "))
    m1 = len(A)
    n1 = len(A[1])
    m2 = len(B)
    n2 = len(B[1])

    if(m1 == m2 and n1 == n2):
        Out = [[0 for col in range(n1)]for row in range(m1)]
        for i in range(m2):
            for j in range(n2):
                Out[i][j] = A[i][j] + B[i][j]
        return (name, Out)
            
    else:
        print("Addition is not Defined")
        return (None, None)

def mul(A, B):
    name = str(input("Name of the new matrix is: "))
    m1 = len(A)
    n1 = len(A[1])
    m2 = len(B)
    n2 = len(B[1])

    if(m2 == n1):
        product = [[0 for row in range(n2)]for col in range(m1)]
        for i in range(m1):
            for j in range(n2):
                prod[i][j]=0
                for k in range(m2):
                    prod[i][j]+=(A[i][k])*(B[k][j])
        return (name, prod)
            
    else:
        print("Multiplication is not Defined.")
        return (None, None)

def tnp(A):
    name = str(input("Name of the new matrix is: "))
    m1 = len(A)
    n1 = len(A[1])
    
    comp = [[0 for col in range(m1)]for row in range(n1)]
    for i in range(n1):
        for j in range(m1):
            comp[i][j] = A[j][i]
    return (name, comp)

def det(A):
    p = len(A)
    determinant = 0
    if p == 1:
        determinant = int(A[0][0])
            
    if p != 1:
        determinant = 0
        adj = list()

        # Expanding along Row 1
        
        for i in range(p):
            lst = A
            B = copy.deepcopy(A)
            x = B.pop(0)
            
            for j in range(p-1):
                x = B[j].pop(i)
                            
            adj.append(det(B))
                    
        for i in range(p):
            determinant += (A[0][i] * adj[i] * ((-1) ** (i)))
    
    return determinant
