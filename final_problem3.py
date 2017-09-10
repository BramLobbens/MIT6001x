# MIT 6.00.1x Final Exam Problem 3

"""
# there are words for each of the digits from 0 to 10
# for numbers 11-19 the number is pronounced as "ten digit",
# e.g. 16: "ten six"
# for numbers between 20 and 99 the number is pronounced as "digit ten digit",
# e.g 37: "three ten seven"

# convert_to_mandarin('36') => 'san shi liu'
# convert_to_mandarin('20') => 'er shi'
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

# above is assumed in grader

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    text = ''

    # 1 - 10
    if us_num in trans:
        text = trans[us_num]
    # ending on zero
    elif int(us_num) % 10 == 0:
        text = trans[us_num[0]] + ' ' + trans['10']
    # 11 - 19
    elif int(us_num) < 20:
        text = trans['10'] + ' ' + trans[us_num[1]]
    # two-dgit > 20
    else:
        text = trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[1]]

    return text
    
print(convert_to_mandarin('5'))
#print('5 expected output => wu')
print(convert_to_mandarin('10'))
#print('10 expected output => shi')
print(convert_to_mandarin('16'))
#print('16 expected output => shi liu')
#print(convert_to_mandarin('20'))
#print('20 expected output => er shi')
#print(convert_to_mandarin('33'))
#print('33 expected output => san shi san')
