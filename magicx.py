def sum(n):
	sum=0
	while  n>0:
		sum=sum+n%10
		temp=temp//10
	return sum
def r(n):
	r=0
	while r>0:
		r=r*10+n%10
		n=n//10
	return r
def magic(n):
	if sum(n)*r(n): print('magic nummber = ')
	else:		  print('not a magic number =')	
		
	
	