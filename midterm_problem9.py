# MIT 6.00.1x Midterm Problem 9

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_list = []
    for elem in aList:
        if isinstance(elem, (str, int)):
            new_list.append(elem)
        else:
            for ele in elem:
                if isinstance(ele, (str, int)):
                    new_list.append(ele)
                else:
                    for el in ele:
                        if isinstance(ele, (str, int)):
                            new_list.append(el)
                        else:
                            for e in el:
                                if isinstance(e, (str, int)):
                                    new_list.append(e)
                                else:
                                    for ee in e:
                                        if isinstance(ee, (str, int)):
                                            new_list.append(ee)
                        
    return new_list
    

some_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(some_list))