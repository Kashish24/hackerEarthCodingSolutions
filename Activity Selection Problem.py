# Link to the Problem:- https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 9 , 9 , 7]

f = [a for a,b in sorted(zip(f,s))]
s = [b for a,b in sorted(zip(f,s))]

print(*s)
print(*f)
print(f'{s[0]}--> {f[0]}')
finish = f[0]
for i in range(1,len(s)):
    if s[i] > finish:
        print(f'{s[i]} --> {f[i]}')
        finish = f[i];
