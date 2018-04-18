#print("A program for Average of two numbers")
print()
print("Average") 
#initializing variable 
X=int(input("Enter the number of elements to be inserted: "))
#initializing an array
a=[]
# for loop for range 
for i in range(0,X):
   num=int(input("Enter element: "))
   a.append(num)
avg=sum(a)/X
print("Average of elements in the list",round(avg,2))