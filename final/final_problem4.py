# MIT 6.00.1x Final Exam Problem 4
# solution incomplete or incorrect

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    if len(L) == 2:
        return sum(L)
    
    def run(L, compare = lambda x, y: x <= y):

        result = []
        longest = []
        for i in range(len(L) - 1):
            if compare(L[i], L[i+1]):
                result.append(L[i])
                if i == len(L) - 2:
                    result.append(L[i+1])
                    if len(result) > len(longest):
                        longest = result[:]
                    break
            else:
                if i == len(L) - 2:
                    result.append(L[i])
                    break
                if len(result) > len(longest):
                    result.append(L[i])
                    longest = result[:]
                result.clear()

        return sum(longest), len(longest)
    
    increasing = run(L)
    decreasing = run(L, compare = lambda x, y: x >= y)
    if increasing[1] >= decreasing[1]:
        return increasing[0]
    return decreasing[0]