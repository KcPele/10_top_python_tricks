'''
We can use the same conditional list with the any method in
python to check whether anyones ccondition satisfies it.
'''


score = 200
wickets = 7
catch = 4
list_cond = [
    score < 320, 
    wickets > 8,
    catch < 3
]

if(any(list_cond)):
    print("Win")
else:
    print("Lose")