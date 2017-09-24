# In this quiz, implement a function called which_prize() that notifies a competitor of the prize they have won in a game, depending on the number of points they've scored.

# Points	Prize
# 0 - 50	wooden rabbit
# 51 - 150	No prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
# The input to which_prize() will be the number of points (an integer). The function which_prize() should return the text "Congratulations! You have won a [prize name]!" with the prize name included if they have won a prize and the text "Oh dear, no prize this time." if there is no prize. As always, test your function to check whether it's performing correctly.

def which_prize(points):
	if 0<=points<=50:
		prize = "wooden rabbit"
		return "Congratulations! You have won a {prize}!".format(prize=prize)
	elif 51<=points<=150:
		prize = "no prize"
		return "Oh dear, no prize this time."
	elif 151<=points<=180:
		prize = "wafer-thin mint"
		return "Congratulations! You have won a {prize}!".format(prize=prize)
	elif 181<=points<=200:
		prize = "penguin"
		return "Congratulations! You have won a {prize}!".format(prize=prize)
	else:
		return "Oh dear, no prize this time."

print(which_prize(12))

