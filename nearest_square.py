# Implement the nearest_square function. The function takes an integer argument limit, and returns the largest square number that is less than limit. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
# There's more than one way to write this code, but I suggest you use a while loop!

def nearest_square(limit):

	"""
	This function takes a limit, finds a square value closest to the limit and returns the square value.
	"""
	#Approach 1
	# i = 1
	# bef_limit = 1
	# aft_limit = 1

	# while  aft_limit < limit:
	# 	bef_limit = i * i
	# 	i += 1
	# 	aft_limit = i * i

	# return print(bef_limit)

	#Approach 2
	answer = 0
	while (answer + 1) ** 2 < limit:
		answer += 1
	return print(answer **2)

nearest_square(40)

