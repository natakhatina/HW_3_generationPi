import math

def foo(n):
    for x in range(n):
        x=x * math.pi / 180
        y=x*math.sin(x)
        yield y

Spisok=[y for y in foo(91)]
print(Spisok[90])

def bar(x):
    if math.sin(x)*math.cos(x)>0:
        yield math.sin(x)
    else:
        yield math.cos(x)

x=-60
x=x * math.pi / 180
res=bar(x)
print(next(res))
