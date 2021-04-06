# Link to Problem:- https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

import heapq

def minCost(arr,n):
    heapq.heapify(arr);
    res = 0;
    while(len(arr) > 1):
        first = heapq.heappop(arr);
        second = heapq.heappop(arr);
        res += first+second
        heapq.heappush(arr, first+second);
        
    return res;

if __name__ == '__main__':
    n = int(input());
    arr = list(map(int, input().split()))
    print("Total Cost:- " + str(minCost(arr,n)));
