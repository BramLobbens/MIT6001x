# MIT 6.00.1x Midterm Problem 9
# Recursive solution

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_list = []
    for elem in aList:
        # Check if element is of type list
        if isinstance(elem, list):
            new_list.extend(flatten(elem))
        else:
            new_list.append(elem)
            
    return new_list

some_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(some_list))