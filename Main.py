import random
from Matrix import *
from Instructions import *

def toMat(tuple_2):
    if (tuple_2[0] == None):
        return
    elif (tuple_2[0] in Mat):
        tuple_2 = (str(input("This name " + tuple_2[0] + " is already used, use another name: ")), tuple_2[1])
    Mat[tuple_2[0]] = tuple_2[1]

# All Matrices are stored under "Mat"
Mat = {}

# Instructions for the USER
inst()

# Waiting for input
y = input()

while(y != "Q"):
    if(y == "I"):
        inst()
        
    elif(y == "N"):
        toMat(mat_def())

    elif(y == "P"):
        A = str(input("Enter Name of the matrix to be printed: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        else:
            print("\n" + "Matrix " + A + " is")
            mat_print(Mat[A])

    elif(y == "O"):
        A = str(input("Enter Name of the matrix to print order: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        else:
            print(str(len(Mat[A])) + "X" + str(len(Mat[A][0])))
        
    elif(y == "A"):
        A = str(input("Enter Name of the first matrix: "))
        B = str(input("Enter Name of the second matrix: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        elif (B not in Mat):
            print("Matrix " + B + " is not yet defined")
        else:
            toMat(add(Mat[A], Mat[B]))
        
    elif(y == "M"):
        A = str(input("Enter Name of the first matrix: "))
        B = str(input("Enter Name of the second matrix: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        elif (B not in Mat):
            print("Matrix " + B + " is not yet defined")
        else:
            toMat(mul(Mat[A], Mat[B]))

    elif(y == "T"):
        A = str(input("Enter Name of the matrix to transpose: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        else:
            toMat(tnp(Mat[A]))

    elif(y == "D"):
        A = str(input("Enter Name of the matrix to calculate determinant: "))
        if (A not in Mat):
            print("Matrix " + A + " is not yet defined")
        else:
            Out = det(Mat[A])
            if Out != None :
                print(Out)
        
    else:
        print("Please enter a valid input.")
        inst()
        
    y = (input("\nEnter a letter: ")).upper()

quit()
