from scipy.stats import f_oneway

A = [78,85,90,82,88]
B = [70,72,68,75,69]
C = [88,90,92,85,89]

res = f_oneway(A, B, C)
print(res)