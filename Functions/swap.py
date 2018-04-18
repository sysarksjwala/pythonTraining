print ("A program for swapping of two numbers")
num1 = input("Enter first number :")
num2 = input("Enter second number :")
x = type(num1)

def swap(num1,num2):
	if num1 != x  :
		number1=int(num1)
		number2=int(num2) 
		print("swapping of two numbers:")
		swap = number1
		number1 = number2
		number2 = swap
		print(" First Number after swapping:", number1)
		print(" Second Number after swapping:", number2)
	else:
		exit()
		
