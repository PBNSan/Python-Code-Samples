# Write a function, tag_count, that takes as its argument a list of strings. It should return a count of how many of those strings are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and end with a right angle bracket ">".

# You can assume that the list of string that will be given as input will not contain empty strings.

#TODO: Define the tag_count function

list1 = ['<greeting>', 'Hello World!', '</greeting>','</sim>','<preet>']

def tag_count(list1):
	"""
	This function takes an input list and checks each string in the list, if the string starts and ends with < and > it is a tag, finally output the count of tags

	"""
	count = 0
	for element in list1:
		# element_length = len(element)
		# if element[0] == "<" and element[element_length-1] == ">":
		if element[0] == "<" and element[-1] == ">":
			count += 1
	return count

# Test for the tag_count function:
count = tag_count(list1)
print("Expected result: 4, Actual result: {}".format(count))
