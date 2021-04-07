#Link to the problem:- https://www.geeksforgeeks.org/fractional-knapsack-problem/

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50


unitValue = [];

for i in range(len(wt)):
    unitValue.append(int(val[i]/wt[i]));

wt1 = [y for (x,y) in sorted(zip(unitValue, wt), key=lambda pair: pair[0], reverse=True)]
unitValue = [x for (x,y) in sorted(zip(unitValue, wt), key=lambda pair: pair[0], reverse=True)]
print(*unitValue)
print(*wt1)

profit =0;
i=0
while(capacity > 0):
    if(capacity >= wt1[i]):
        profit += unitValue[i]*wt1[i];
        capacity -= wt1[i]
        i +=1;
    else:
        profit += unitValue[i]*capacity;
        capacity =0;
        break;
        
print(f'Maximum Profit : {profit}');
