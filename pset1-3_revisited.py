def longest_substring(s, i = 0):
    result = ''
    highest_result = ''

    if s[i] >= s[i-1]:
        result += s[i]
    else:
        return longest_substring(s, i+1)

    return result
        
print('Longest substring in alphabetical order is:', longest_substring(s))