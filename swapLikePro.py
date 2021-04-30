'''
One way to swap variable is by using a temporary variable.
The better way to do it in python is as follows:
'''
salary = 85000
exp=3
price = 34

salary, exp = exp, salary
print(salary)