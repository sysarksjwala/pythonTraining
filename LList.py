print("A program to find Largest Number in list")
print()
print("Largest value in List")
# initializing a new list
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])