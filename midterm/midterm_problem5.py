# MIT 6.00.1x Midterm Problem 5

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    listC = listA[:]
    for i, elem in enumerate(listB):
        listC[i] *= elem
    return sum(listC)