'''
If you want to check what object repeats the most, we can use the following line of code
This approach uses the max function with the key attribute to find the most repeated element
'''
li = [1,5,8,6,5,9,6,6,4,6,5,4,5,"a","a","b","b","a","a","a"]

print(max(set(li), key=li.count))
