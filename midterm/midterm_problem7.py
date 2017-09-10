# MIT 6.00.1x Midterm Problem 7

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Set longest dict as d1
    if len(d1) < len(d2):
        d1, d2 = d2, d1

    first_dict = {}
    second_dict = {}

    for key in d1:
        if key in d2:
            first_dict[key] = f(d1[key], d2[key])

        else:
            second_dict[key] = d1[key]

    for key in d2:
        if key not in d1:
            second_dict[key] = d2[key]

    return (first_dict, second_dict)