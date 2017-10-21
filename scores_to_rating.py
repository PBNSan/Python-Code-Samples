# Imagine that you work for a consumer ratings website. Users submit reviews and scores for products they use, and you show the results so that consumers can make informed choices.
# Throughout this section we will write a function that takes as input five scores and aggregates them to output a single rating.

# Steps Outlined:

# Take each of the raw scores and convert each of them to a numerical type.
# Input: score as string/float/int. Output: score as float or int.
# Choose the middle 3 values from the set of 5 scores.
# Input: 5 scores as float or int. Output: 3 scores (same type).
# Take the average of three scores.
# Input: 3 scores as float or int. Output: 1 average score (float).
# Choose the correct word rating for the average score.
# Input: average score as float. Output: Rating as a string.



def convert_to_numeric(score):
	"""
	This function will take the Input score which could be any type (String/INT/FLOAT) and convert it to either int or float

	"""
	#Alternative Solution

	#Approach 1
	# try:
	# 	return int(score)
	# except ValueError:
	# 	return float(score)
	
	#Approach 2
	# return float(score) if '.' in score or 'e' in score.lower() else int(score)

	#Approach 3
	converted_score = float(score)
	return converted_score




def sum_of_middle_three(score1,score2,score3,score4,score5):
	"""
	This function takes in the 5 input scores identifies the middle three scores and calculates the sum of them

	score1/score2/score3/score4/score/5 : type int or float

	"""
	sum_of_all_five_scores = score1+score2+score3+score4+score5
	min_of_scores = min(score1,score2,score3,score4,score5)
	max_of_scores = max(score1,score2,score3,score4,score5)
	sum = sum_of_all_five_scores - (min_of_scores + max_of_scores)

	return sum

def score_to_rating_string(average_score):
	"""
	This function takes the average score from the input and maps the average score obtained to the written rating.

	# Average Score	Rating
	# 0 <= score < 1	Terrible
	# 1 <= score < 2	Bad
	# 2 <= score < 3	OK
	# 3 <= score < 4	Good
	# 4 <= score <= 5	Excellent

	average_score : type float
	"""

	if average_score < 1:
		rating = "Terrible"
	elif average_score < 2:
		rating = "Bad"
	elif average_score < 3:
		rating = "OK"
	elif average_score < 4:
		rating = "Good"
	else:
		rating = "Excellent"

	return rating

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating



scores_to_rating(1,2,3,4,5)