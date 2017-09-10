# MIT 6.00.1x Pset1-3

len_s = int(len(s))
result = ''
highest_result = ''
 
for i in range(len_s):

    # check if current char is bigger than or equal to previous char
    if s[i] >= s[i-1]:
        result += s[i]
    else:
        # start at new substring, if longer than previous result, store as 
        # highest result
        if len(result) > len(highest_result):
            highest_result = result
        result = ''
        result += s[i]

# final check if last result is highest
if len(result) > len(highest_result):
        highest_result = result 
# if no new higher result was available => highest = result
if len(highest_result) == 0:
        highest_result = result
        
print('Longest substring in alphabetical order is:',highest_result)