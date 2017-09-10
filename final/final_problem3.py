# MIT 6.00.1x Final Exam Problem 3

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
    
    return mandarin
