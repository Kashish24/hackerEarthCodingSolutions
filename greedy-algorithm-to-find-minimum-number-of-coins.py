# Link to the problem:- https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

deno = [1, 2, 5, 10, 20, 50,
            100, 500, 1000]
i = len(deno) - 1;
V = 93;

res = [];
while(i>=0):
    if(V >= deno[i]):
        while(V >= deno[i]):
            res.append(deno[i]);
            V -= deno[i]
    i -=1;
        
print(f'Toatl denominations will be {len(res)} : ' , sep = " ")

print(*res)
