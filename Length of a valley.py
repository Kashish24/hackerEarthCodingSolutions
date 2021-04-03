Link to Problem:- https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/hill-150045b2/

# Brute Force Approach.
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for t in range(int(input())):
    n = int(input()) ; arr = list(map(int, input().split()))
    l = 0;
    r = 0;
    res = []
    for i in range(len(arr)):
        l = i+1;
        r = i+1;
        for j in range(i-1,-1,-1):
            if arr[j] > arr[j+1]:
                l -=1;
            else:
                break;
        for j in range(i+1,len(arr)):
            if arr[j] > arr[j-1]:
                r +=1;
            else:
                break;
        res.append(r-l+1);
    print(*res)
    
    
# Better RunTime Complexity using Stack;

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def r_area(arr,n):
    stack = [];
    r_index = [0]*n;
    index=0;

    while(index<n):
        if(len(stack)==0 or arr[stack[-1]]< arr[index]):
            stack.append(index);
            index +=1;
        else:
            while(len(stack)):
                elem = stack.pop();
                r_index[elem] = index;
    
    while(len(stack)):
        elem = stack.pop();
        r_index[elem] = index;
    
    return r_index;

def l_area(arr,n):
    stack = [];
    l_index = [0]*n;
    index=0;

    while(index<n):
        if(len(stack)==0 or arr[stack[-1]]< arr[index]):
            stack.append(index);
            index +=1;
        else:
            while(len(stack)):
                elem = stack.pop();
                l_index[elem] = index;
    
    while(len(stack)):
        elem = stack.pop();
        l_index[elem] = index;
    
    return l_index;

for t in range(int(input())):
    n = int(input()) ; arr = list(map(int, input().split()))
    l_index = [0]*n;
    r_index = [0]*n;
    res = [0]*n;
    l_index = l_area(arr[::-1],n);
    l_index = l_index[::-1];
    l_index = [(n-i+1) for i in l_index];
    r_index = r_area(arr,n);
    for i in range(n):
        res[i] = r_index[i] - l_index[i] +1;
        
    print(*res)
