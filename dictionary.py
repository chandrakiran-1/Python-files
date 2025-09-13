s={'rama':45,'raja':30,'sita':43}
M=max(s.values())
for i, j in s.items():
    if j==M:
        print(i, ":",j)