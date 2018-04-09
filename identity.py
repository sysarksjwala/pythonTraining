print("A program to print identity matrix")
print()
print("Identity matrix") 
#initializing
X=int(input("Enter a number: "))
# i,j variable to construct matrix
for i in range(0,X):
    for j in range(0,X):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()