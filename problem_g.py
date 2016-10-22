import sys

rank = 25
stars = 0
winstreak = 0
rankstars = {25:2, 24:2,23:2,22:2,21:2,20:3,19:3,18:3,17:3,16:3,
             15:4,14:4,13:4,12:4,11:4,10:5,9:5,8:5,7:5,6:5,5:5,4:5,3:5,2:5,1:5}

for line in sys.stdin:
    winloss = line

for match in winloss:
    if rank > 0:
        if match == "W":
            stars += 1
            winstreak += 1
            if winstreak >= 3 and rank > 5:
                stars += 1
            if stars > rankstars[rank]:
                stars -= rankstars[rank]
                rank -= 1
                
        
        if match == "L":
            winstreak = 0
            if rank < 21:
                stars -= 1
                if stars < 0 and rank < 20:
                    rank += 1
                    stars = rankstars[rank] - 1
                if stars < 0 and rank == 20:
                    stars = 0

if rank > 0:
    print(rank)
else:
    print('Legend')
    
                
            
