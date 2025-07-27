def reverse(n):
	r=0
	while n>0:
		r=r*10+n%10
		n=n//10
	return r	
n=int(input('enter a number to reverse='))
print('the reverse num of =', reverse(n))