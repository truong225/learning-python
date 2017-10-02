str1 = """Declare string
in multi
line"""


def foo():
    print 'foo function'


def _sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def new_sum(a, b):
    return a + b


print foo()
print _sum(1, 2, 3, 4)
print new_sum(b=1, a=2)

# Replace string
print str1
new_str = str1.replace('multi', 'multiple')
print new_str

# Find string
print str1.find('Declare')
print str1.rfind('Declare')

# Split string
print str1.split(' ')
print str1.splitlines()

print str1.strip(' ')
print str1.lstrip(' ')
print str1.rstrip(' ')

# String process
s = '123abcDe'
print s.isdigit()
print s.upper()
print s.lower()
