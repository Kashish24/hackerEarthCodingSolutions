# Link to the Problem:- https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/
# Brute Force Approach developed by me yet with the help of adjacenecy list auxiliary space, Gives best Run time Complexity.

from itertools import chain
#b = [2, 1, 8, 3];
#a = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8];

a = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5 ];
b = [2, 1, 8, 3, 4];

maxA = max(a);

auxSpace = [0] * (maxA+1);

for i in range(len(b)):
    if(b[i]<=maxA):
        auxSpace[b[i]] = i+1;


other = []
print(* auxSpace)
maxB = max(auxSpace);


#z=[[]] * (maxB+1)
z = [[] for _ in range (maxB+1)]

for i in a:
    if(auxSpace[i] !=0):
        z[auxSpace[i]].append(i)
    else:
        other.append(i)

other.sort()
flattenList = list(chain.from_iterable(z))
ans = flattenList + other
print(ans)
