# A program on __int__=" <main function>"
import file2

print("just a statement")
def add():
	a=[1,2,3,4]
	total=sum(a)
	print(" The addition of numbers:  ", total)

#if MainFunc.__name__ == "__main__"	
if __name__ == "__main__":
	print(" it is a main program")
	print(" value of __name__ is:", __name__)
	add()
	file2.statements()
else:
	print("How is this statement getting printed")
	

	


#if file2.__name__ == "__main__"