print("Program to evaluate enumarate function")
print()
Books = {'Managemnt system': 1, 'Database': 8, 'Python': 10}
for i,j in enumerate(Books):
  print(j,i)
  Bcount = print(j)

for Bcount in enumerate(Books):
  print(Bcount)

print('\n')
for count, item in enumerate(Books):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(Books, 100):
  print(count, item)