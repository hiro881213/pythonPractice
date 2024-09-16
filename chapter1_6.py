s = 'My name is Mike. Hi Mike.'

print('##### StartsWith function ######')
is_start = s.startswith('My')
print(is_start)

is_start2 = s.startswith('X')
print(is_start2)

print('##### find method #####')
print(s.find('Mike'))

print('##### rfind method #####')
print(s.rfind('Mike'))

print('##### count method #####')
print(s.count('Mike'))
