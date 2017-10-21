# The function in this quiz, median, returns the median value of an input list. Unfortunately it only works with lists that have an odd number of elements. Modify the function so that when median is given a list with an even number of elements, it returns the mean of the two central elements. The provided test cases demonstrate the expected behavior.

def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    number_of_elements_type = len(numbers)

    if number_of_elements_type % 2 == 0:
    	middle_index = int(len(numbers)/2)
    	middle_before_index = middle_index -1
    	median_of_even_numbers = (numbers[middle_index] + numbers[middle_before_index])/2
    	return median_of_even_numbers
    else:
    	middle_index = int(len(numbers)/2)
    	return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

test4 = median([1,2,3,4,5,6,7,8])
print("expected result : 4.5, actual result: {}".format(test4))