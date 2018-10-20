
import math
# x=range(91)
# x=math.radians(x)

# L=[math.cos(x*math.pi/180) for x in range(91)]
# print(L)
# print(L[90])

k=2
def foo(k):
    x=(k+0.5)*math.pi
    y=x*math.sin(x)
    yield [x, y]

# print(foo(1))

def bar(k):
    x=[]
    for i in range(0,k+1):
        el=(i+0.5)*math.pi
        yield el


L=[x*math.sin(x) for x in bar(k)]
print(L)

X=[(i+0.5)*math.pi for i in range(0,k)]
Y=[(i+0.5)*math.pi*math.sin((i+0.5)*math.pi) for i in range(0,k)]
print(X)
print(Y)