def ispalindrome(n):
	r=0
	temp=n
	while temp>0:
		r=r*10+temp%10
		temp=temp//10
	return n==r
n=int(input('enter a number= '))
if ispalindrome(n): print(' num is palindrome')
else:		    print(' num not a palindrome')
