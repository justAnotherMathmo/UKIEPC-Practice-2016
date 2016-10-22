import sys

data = []
money = 100
shares = 0

for line in sys.stdin:
    data.append(int(line))
prices = data[1:]

turningpoints = [0]

if len(prices) == 1:
    money = 100
else:
    if prices[0] < prices[1]:
        shares = int(money/prices[0])
        money -= shares*prices[0]
        
    for i in range(1,len(prices)-1):
        if prices[turningpoints[i-1]] < prices[i] and prices[i] > prices[i+1]:
            money += prices[i]*shares
            shares = 0
            turningpoints.append(i)
        elif prices[turningpoints[i-1]] > prices[i] and prices[i] < prices[i+1]:
            shares = int(money/prices[i])
            if shares > 100000:
                shares = 100000
            money -= shares*prices[i]
            turningpoints.append(i)
        else:
            turningpoints.append(turningpoints[-1])
        
    money += shares*prices[-1]
    
print(int(money))
