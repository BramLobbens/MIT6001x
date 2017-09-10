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
            # Apply given function f to values in first_dict
            first_dict[key] = f(d1[key], d2[key])

        else:
            # Put d1 key-value pair in second_dict if key is unique
            second_dict[key] = d1[key]

    for key in d2:
        if key not in d1:
            # Put d2 key-value pair in second_dict if key is unique
            second_dict[key] = d2[key]

    return (first_dict, second_dict)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))