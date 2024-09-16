s = 'a is {}'

print('##### format method #####')
print(s.format('a'))
print(s.format('test'))

print('##### format method(Del warnings) #####')
a = 'test'
print(f"a is {a}")

print('##### format method including index #####')
s2 = 'a is {0} {1} {2}'
print(s2.format(1, 2, 3))

s3 = 'a is {2} {1} {0}'
print(s3.format(1, 2, 3))

print('##### format method using variable names #####')
s4 = 'My name is {name} {family}. Watashi wa {family} {name}'
print(s4.format(name='Hiro', family='Frank'))
