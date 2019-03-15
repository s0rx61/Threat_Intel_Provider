
#Title: entropy
#calculates entropy based on distance between adjacent characters in a given string


def entropy(str):
	sum = 0
	prev = str[0]
	for i in range(0,len(str)-1):		
		sum = sum+abs(ord(str[i])-ord(str[i+1]))
	return sum/len(str)