# Define a procedure is_palindrome, that takes as input a string, and returns a Boolean indicating if the input string is a #palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome_v1(s):
	''' (str) -> bool
	True if s is palindrome

	>>> print is_palindrome('')
	True
	>>> print is_palindrome('noon')
    True
	>>> print is_palindrome('racecar')
    True
    >>> print is_palindrome('dented')
    False
	'''
	return reverse(s)==s


def reverse(s):
	'''(str) -> str

	Return reversed s
	'''
	for char in s:
		rev += ch

	return rev
    # if s=='':
    #     return True
    # elif s[0]==s[-1]:
    #     return is_palindrome(s[1:-1])
    # else:
    #     return False
       
print is_palindrome('')
#>>> True
print is_palindrome('noon')
#>>> True
print is_palindrome('racecar')
#>>> True
>>> print is_palindrome('dented')
#>>> False