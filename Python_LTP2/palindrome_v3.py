def is_palindrome_v2(s):
	''' (str) -> bool
	True if palindrome compare 1 to last 2nd to the 2nd from end

	>>> is_palindrome_v2('noon')
	True
	>>> is_palindrome_v2('racecar')
	True
	>>> is_palindrome_v2('dented')
	False
	'''
	i=0
	j=len(s)-1
 	
 	while i<j and s[i]==s[j]:
 		i+=1
 		j-=1

 	return j <= i