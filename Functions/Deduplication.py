print( " program to delete duplicates from lists")

x = [1,2,2.5,3.6,2,1,3]
print(" Actual List is:", x)

def deldup1(x):
	y = []
	for i in x:
		if(i not in y):
			y.append(i)
	return y
	
def deldup2(x):
	return list(set(x))

x = [1,2,2.5,3.6,2,1,3]	
print(deldup1(x))	
print(deldup2(x))


