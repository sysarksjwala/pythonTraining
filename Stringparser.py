print("A program to find no of digits and letters in a string")
print()
print("Digits and Letters in string") 
#initializing string,count1 and count2 variables
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)