def countofdigits(n):
	if n==0 : return 0
	else: return 1+countofdigits(n//10)
n=int(input('enter a number='))
print('countdigits=', countofdigits(n))