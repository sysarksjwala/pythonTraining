print("A program to Add Key-Value Pair to Dictionary")
print()
print("Key-Value Pair")
key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)