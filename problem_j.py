import sys 

lines = []
for line in sys.stdin:
    lines += [line]

cur_dir = int(lines[0])
real_dir = int(lines[1])

dist = (real_dir - cur_dir)%360
if dist < 180:
    print(dist)
else:
    print(dist-360)
