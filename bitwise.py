
print("bitwise operators")
#AND operator each bit to 1 if both bits are 1
def myand(a,b):
    c=a&b
    print(c)
myand(10,5)

#OR operator each bit to 1 if one of two bits is 1
def myor(a,b):
    c=a|b
    print(c)
myor(10,5)

#NOT operator one's complement of the number
def mynot(a,b):
    c=~a
    print(c)
mynot(10,5)

#XOR operator each bit to 1 if only one of two bits is 1
def myxor(a,b):
    c=a^b
    print(c)
myxor(10,5)