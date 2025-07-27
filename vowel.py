# membership operator = in ,not in.
# identity operator = is , is not.


def main():
	letter=input('enter a letter=')
	if letter in 'aeiouAEIOU': print('vowel')
	else: 			   print('not a vowel')
if __name__=='__main__':
	main()