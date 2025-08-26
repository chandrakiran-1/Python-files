def chandu(n):
	if n>1: chandu(n-1)
	print('chandu',end=' ')
chandu(990)