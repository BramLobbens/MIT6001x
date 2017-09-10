# MIT 6.00.1x pset1-2

count = 0
i = 0

for char in s:
    if s[i:i+3] == 'bob':
        count += 1
    i += 1

print('Number of times bob occurs is: ' + str(count))