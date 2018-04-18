print(" Generation of random numbers:")
from random import randint
n= int(input("Total random numbers to be generated:"))	
def random() :
	r1= int(input("Minimum value of Random range:"))
	r2= int(input("Maximum value of Random range:"))
	for i in range (0,n):
		print(randint(r1,r2))
print(random())
	
	

