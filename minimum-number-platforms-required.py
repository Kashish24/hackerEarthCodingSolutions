# Link to the problem:- https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort();
dep.sort();
i=1;
j=0;
res=1;
while(i<len(arr) and j<len(dep)):
    if(arr[i] <= dep[j]):
        res +=1;
        i +=1;
    elif(arr[i] > dep[j]):
        res -=1;
        j +=1;
    
    if(platformNeeded < res):
        platformNeeded = res;
print("Platform Needed :",platformNeeded)
