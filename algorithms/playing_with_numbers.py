from functools import reduce
n = int(input())
N = [int(x) for x in str(input()).split()]
q = int(input())
Q = [int(x) for x in str(input()).split()]


for query in Q:
    # add query to entire list
    N = [ x + query for x in N ]
    # add up absolute values
    print(reduce(lambda x,y: abs(x) + abs(y), N ))



