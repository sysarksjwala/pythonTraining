print("Program for Absolute function")
n=input("enter number:")
x=type(n)
#print('type of n is: ', type(n))
def absolute(n) :
	switcher = {
		1:
		if type(int(n))!= x:
			print("Absolute value of integer is:",abs(int(n)))
		  else:
			print("wrong input")
		2:
			if type(float(n))!= x:
				print("Absolute value of float is:",abs(float(n)))
			else:
				print("rong input")
	}
	print switcher.get("Absolute value:", n)