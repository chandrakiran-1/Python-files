def productofnum(n):
	sum=1
	while n>1:
		product*=n%10
		n//=10
	return product
n=int(input('enter a number='))
print('product of the number=', productofnum(n))