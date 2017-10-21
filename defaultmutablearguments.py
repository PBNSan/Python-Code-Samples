# def todo_list(new_task, base_list=['wake up']):
#     base_list.append(new_task)
#     return print(base_list)


# todo_list(["Checkup","List"])

# todo_list("oribital transfer")

# this code returns a UnboundLocalError, Python doesn't allow functions to modify variables that aren't in the function's scope. 
# egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()

#The best way to rewrite this would be like this:
def buy_eggs(count):
    return count + 12  # purchase a dozen eggs
egg_count = 0
egg_count = buy_eggs(12)