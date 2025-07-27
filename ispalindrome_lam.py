ispalindrome =lambda x: x==x[::-1]
words=[ 'oyo','pop','kayak','madam','ganesh','chandu']
print(list(filter(ispalindrome,words)))
