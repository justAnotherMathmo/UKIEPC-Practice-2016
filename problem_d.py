import sys

data = []
money = 100
shares = 0

for line in sys.stdin:
    data.append(int(line))
prices = data[1:]

if len(prices) == 1:
    money = 100
else:
    if prices[0] < prices[1] and prices[0] <= 100:
        shares = int(money/prices[0])
        money -= shares*prices[0]
        
    for i in range(1,len(prices)-1):
        if prices[i-1] < prices[i] and prices[i] > prices[i+1]:
            money += prices[i]*shares
            shares = 0
        elif prices[i-1] > prices[i] and prices[i] < prices[i+1] and prices[i] <= money:
            shares = int(money/prices[i])
            money -= shares*prices[i]

    money += shares*prices[-1]


print(money)
    
    
