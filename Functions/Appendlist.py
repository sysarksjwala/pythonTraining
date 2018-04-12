print("program to append list using function") 
mylist = [10,20,30]
print ("Values outside the function: ", mylist)

def list( mylist ):
   mylist.append([1,2,3,4]);
   print ("Values inside the list: ", mylist)
  
list( mylist )
print ("Values outside the function: ", mylist)
  

