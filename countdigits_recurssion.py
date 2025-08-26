def countdigits(n):
	if n==0: return 0
	else:  return 1+ countdigits(n//10)
n=int(input('enter a number = '))
print('count of a number = ' ,countdigits(n))
`