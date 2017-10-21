def remove_duplicates(source_list):
	"""
	This function takes in a list of entries and checks for the duplicates and removes them
	"""

	target_list = []

	for element in source_list:
		if element not in target_list:
			target_list.append(element)

	return print(target_list)


source_list = [1,2,3,4,1,2,2,2,3,3,3]

remove_duplicates(source_list)
	

# #Example Functions to deduplify
# def f1(seq):
#    # not order preserving
#    set = {}
#    map(set.__setitem__, seq, [])
#    return set.keys()

# def f2(seq): 
#    # order preserving
#    checked = []
#    for e in seq:
#        if e not in checked:
#            checked.append(e)
#    return checked

# def f3(seq):
#    # Not order preserving
#    keys = {}
#    for e in seq:
#        keys[e] = 1
#    return keys.keys()

# def f4(seq): 
#    # order preserving
#    noDupes = []
#    [noDupes.append(i) for i in seq if not noDupes.count(i)]
#    return noDupes

# def f5(seq, idfun=None): 
#    # order preserving
#    if idfun is None:
#        def idfun(x): return x
#    seen = {}
#    result = []
#    for item in seq:
#        marker = idfun(item)
#        # in old Python versions:
#        # if seen.has_key(marker)
#        # but in new ones:
#        if marker in seen: continue
#        seen[marker] = 1
#        result.append(item)
#    return result

# def f6(seq):
#    # Not order preserving    
#    set = Set(seq)
#    return list(set)