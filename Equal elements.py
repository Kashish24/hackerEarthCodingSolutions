Link to Problem:- https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/equal-elements-2-db70c1ae/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
for t in range(int(input())):
    evenCount= 0
    oddCount= 0
    n = int(input()) ; arr = list(map(int, input(). split()))
    for i in arr:
        if i%2 ==0:
            evenCount +=1;
        else:
            oddCount +=1;
    print(min(evenCount,oddCount))
