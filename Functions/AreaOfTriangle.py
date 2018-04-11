print("Program to fin Area of Triangle\n\n")
print("Area of Triangle")
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
Perimeter=(a+b+c)/2
AreaOfTriangle=math.sqrt(Perimeter*(Perimeter-a)*(Perimeter-b)*(Perimeter-c))
print("Area of the triangle is: ",round(AreaOfTriangle,2))
