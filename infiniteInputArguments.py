'''
This trick is handy when we dont know the input argument's function length. 
We can use the * sign with the variable name that takes input as a list
'''

def fun1(*a):
    res = 1
    for ele in a :
        res*=ele
    return res
ans = fun1(5,6,7,6,8,5,4)
print(ans)