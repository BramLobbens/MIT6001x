# MIT 6.00.1x Pset1-1
# Version 2

vowels = list('aiueo')

def count_vowels(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

print('Number of vowels: {0}'.format(count_vowels(s)))