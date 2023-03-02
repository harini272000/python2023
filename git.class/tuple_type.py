t=(1,2,3,4,5,6)
print(t)
type(t)

t=(1,2,3,5)
t1=dir(t)
print(t1)

t2=(1,2,3,4,5,6)
s=len(t2)
print(s)

a=(1,2,37,54,84,2)
t6=a[2]
print(t6)

b=[1,2,34,5,6,7,8,94,45]
g=b[0:5]
print(g)

e=[1,2,34,5,6,7,8,94,45]
h=e[::-1]
print(h)

#tuple() Constructor
s=tuple((2,3,4,5,6))
print(s)

#t convert to list

g=(1,2,"hello",67,89)
f=list(g)
print(f)
f[1]="hi"
print(f)

x=("apple","banana","cherry")
g=list(x)
d=g.append("orange")
t=tuple(g)
print(t)

#join()
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)

#methods
t=(1,2,3,4,1,2,34,5,6,7,5,5,6,7)
s=t.count(5)
print(s)

t6=(1,2,3,4,1,2,34,5,6,7,5,5,6,7)
r=t6.index(34)
print(r)







