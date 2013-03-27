def is_palindrome_v2(s):
	''' (str) -> bool
	True if palindrome

	>>> is_palindrome_v2('noon')
	True
	>>> is_palindrome_v2('racecar')
	True
	>>> is_palindrome_v2('dented')
	False
	'''
	#number of chars in s
	n=len(s)
	#compare 1st half of s to reverse of 2nd half
	#omits the mid char of odd length
	return s[:n//2] == reverse(s[n-n//2:])

def reverse(s):
	''' (str) -> str
	return reverse
	'''
	rev=''
	for ch in s:
		rev+=ch

	return rev