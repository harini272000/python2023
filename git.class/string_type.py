s = "thunder soft"
print(s)
thunder
soft
type(s)
len(s)
12
res = s[0]
print(res)
t
s[0]
't'
s[0:12]
'thunder soft'
s[::]
'thunder soft'
s[:]
'thunder soft'
s[4:7]
'der'
s[0::2]
'tudrsf'
s[-1]
't'
s[-1:]
't'
s[:-1]
'thunder sof'
s[:-2]
'thunder so'
s[-5]:

SyntaxError: invalid
syntax
s[::-1]
'tfos rednuht'
dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
capitalize(s)
Traceback(most
recent
call
last):
File
"<pyshell#19>", line
1, in < module >
capitalize(s)
NameError: name
'capitalize' is not defined
s.capitalize()
'Thunder soft'
s = "HARINI"
s.casefold()
'harini
s = "python"
s.isidentifier()
True
s = "py thon"
s.isidentifier()
False
s = "Python is awesome"
s.center()
Traceback(most
recent
call
last):
File
"<pyshell#28>", line
1, in < module >
s.center()
TypeError: center
expected
at
least
1
argument, got
0
s = "Python is awesome"
s.center(24)
'   Python is awesome    '
s = "harini"
count(s)
Traceback(most
recent
call
last):
File
"<pyshell#32>", line
1, in < module >
count(s)
NameError: name
'count' is not defined.Did
you
mean: 'round'?
s = "harini"
s1 = "ri"
s.count(s1)
1
s = "harini"
s.encode()
b'harini'
`s = "harini narisetty"
SyntaxError: invalid
syntax
s = "harini narisetty"
s.endswith(narisetty)
Traceback(most
recent
call
last):
File
"<pyshell#40>", line
1, in < module >
s.endswith(narisetty)
NameError: name
'narisetty' is not defined
s = "harini is a good"
s.encode()
True
s = "harinilishithasrihitha"
s.expandtabs()
'harinilishithasrihitha'
s = "harini/tlishitha/tsrihitha
SyntaxError: unterminated
string
literal(detected
at
line
1)
s = harini / tlishitha / tsrihitha
"
SyntaxError: unterminated
string
literal(detected
at
line
1)
s = "harini/tlishitha/tsrihitha"
s.expandtabs()
'harini/tlishitha/tsrihitha'

s = 'hari\t1234\tlishi'
s.expandtabs()
'hari    1234    lishi'
s = "harini"
s.find("ri")
2
s = "harini"
s[2]
'r'
s = "ms234ghsgd"
s.isalnum()
True
s = harini
"
SyntaxError: unterminated
string
literal(detected
at
line
1)
s = "harini"
s.isalpha()
True
s = 1234
s.isdecimal()
Traceback(most
recent
call
last):
File
"<pyshell#62>", line
1, in < module >
s.isdecimal()
AttributeError: 'int'
object
has
no
attribute
'isdecimal'
s = "2345"
s.isdecimal()
True
s = "123"
s.isdigit()
True

