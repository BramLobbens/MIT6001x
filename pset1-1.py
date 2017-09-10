# MIT 6.00.1x pset1

vowelCount = 0     # counts 'a', 'e', 'i', 'o', 'u'

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter =='u':
            vowelCount += 1
print ('Number of vowels: ' + str(vowelCount))