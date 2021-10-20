"""
python修改形参
"""


def swap(a, b):
    temp = a
    a = b
    b = temp


w = 1
e = 2
swap(w, e)
print(w, e)

a=1
def f(b):
    b=2
f(a)
print(a)

b=[1]
def m(c):
    c[0]+=1
m(b)
print(b)

a = 1
b = a
a = 2
print(a, b)
a = [1]
b = a
a[0] = 2
print(a, b)
