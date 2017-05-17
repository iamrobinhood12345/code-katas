"""This function takes a unicode string (text)
as input and returns whether the string is properly closed
parenthetically."""

from doubly_linked_list import Doubly_Linked_List

def proper_parenthetics(text):
	"""Returns a 1 if the string is parenthetically open.
	Returns a 0 if the string is parenthetically balanced.
	Returns a -1 if the string is parenthetically broken."""
	parenthetics = Doubly_Linked_List()
	text = text[::-1]
	for char in text:
		if char == '(' or char == ')':
			parenthetics.push(char)
	while True:
		try:
			a = parenthetics.pop()
			if a != '(':
				return -1
			else:
				try:
					parenthetics.remove(')')
				except:
					return 1
		except:
			return 0
