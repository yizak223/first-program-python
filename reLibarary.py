

import re
string = "'I AM NOT YELLING',she said. Though we know it to not be true 123456"
print('original:', string)
new1 = re.sub('[A-Z]', '', string)
new2 = re.sub('[a-z]', '', string)
new3 = re.sub('[0-9]', '', string)
new4 = re.sub('[^a-z ]', '', string)
print('1:', new1)
print('2:', new2)
print('3: without numbers', new3)
print('4:', new4)
