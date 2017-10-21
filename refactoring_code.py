# def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    # results= [None, None, None, None, None]
    # if my_answers[0] == answers[0]:
    #     results[0] = True
    # elif my_answers[0] != answers[0]:
    #     results[0] = False
    # if my_answers[1] == answers[1]:
    #     results[1] = True
    # elif my_answers[1] != answers[0]:
    #     results[1] = False
    # if my_answers[2] == answers[2]:
    #     results[2] = True
    # elif my_answers[2] != answers[2]:
    #     results[2] = False
    # if my_answers[3] == answers[3]:
    #     results[3] = True
    # elif my_answers[3] != answers[3]:
    #     results[3] = False
    # if my_answers[4] == answers[4]:
    #     results[4] = True
    # elif my_answers[4] != answers[4]:
    #     results[4] = False
    # count_correct = 0
    # count_incorrect = 0
    # for result in results:
    #     if result == True:
    #         count_correct += 1
    #     if result != True:
    #         count_incorrect += 1
    # if count_correct/5 > 0.7:
    #     return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    # elif count_incorrect/5 >= 0.3:
    #     return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

    #Approach 1

    # results = [None,None,None,None,None]
    # count_correct = 0
    # count_incorrect = 0

    # for i in range(len(my_answers)):
    #     if answers[i] == my_answers[i]:
    #         results[i] = True
    #         count_correct += 1
    #     else:
    #         results[i] = False
    #         count_incorrect += 1

    # print(count_correct)
    # print(count_incorrect)

    # if count_correct/5 > 0.7:
    #     return print("Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5.")
    # elif count_incorrect/5 >= 0.3:
    #     return print("Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5.")


    # my_answers = [0,1,0,2,0]
    # answers = [0,0,0,0,0]

    #Approach 2

    
    check_answers(my_answers,answers)


    def check_answer(my_answer, answer):
        if my_answer == answer:
            return True
        else:
            return False

    def check_answers(my_answers,answers):
        #Checks the five answers provided to a multiple choice quiz and returns the results.
        results = []
        for i in range(len(my_answers)):
            results.append(check_answer(my_answers[i], answers[i]))
        count_correct = 0

        for result in results:
            if result:
                count_correct += 1

        if count_correct/len(results) > 0.7:
            return "Congratulations, you passed the test!"
        elif (len(results) - count_correct)/len(results) >= 0.3:
            return "Unfortunately, you did not pass."