'''
This method saves most lines of code and places them in a single line.
Using this method, we can iterate over a list while checking any condition in parallel using a single line
'''

li = [i**3 for i in range(1,15) if i%2==0]
print(li)