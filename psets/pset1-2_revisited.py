# MIT 6.00.1x Pset1-2
# Version 2.0

count = 0
value_to_check = 'bob'

for idx, char in enumerate(s):
    if s[idx:idx+len(value_to_check)] == value_to_check:
        count += 1

print ('Number of times {0} occurs is: {1}'.format(value_to_check, count))