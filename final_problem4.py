# MIT 6.00.1x Final Exam Problem 4

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
        print(longest)
        return sum(longest), len(longest), longest
    
    increasing = run(L)
    decreasing = run(L, compare = lambda x, y: x >= y)
    if increasing[1] >= decreasing[1]:
        return increasing[0]
    return decreasing[0]

#a_list = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#b_list = [5, 4, 10]
#print(longest_run(a_list))
#print(longest_run(b_list))

test = [1, 2, 1, 2, 1, 2, 1, 2, -1, -2, -1, -2, 10, 20, 10, 20, 100, 200, 100, 0, 100, 0, 100, 0, 0, 100, 0, 0, 0, 100, 1500000, -1500000, 1, -150001]
print(longest_run(test))