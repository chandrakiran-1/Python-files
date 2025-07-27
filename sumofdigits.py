def sumofdigits(n):
	sum=0
	temp=n
	while n>0:
		sum+=temp%10
		temp//=10
n=int(input('enter a number='))
print('sumofdigits=', sumofdigits(n))