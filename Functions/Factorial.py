print("Program for Factorial of Given numbers")
x = int(input("Enter number:"))
fact = 1
if x == 0:
	print(" The factorial of 0 is always 1 ")

elif x > 0:
	for i in range(1,x+1):
		fact=fact * i
	print("The factorial of",x,"is",fact)
		
else:
	print(" No factorial for negative numbers")
	

#def factorial():
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
		

