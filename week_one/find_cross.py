def f(x):
    return 2*x+1

def find_root(a,b):
    c=(a+b)/2
    ans=f(c)
    while ans != 0:
        c=(a+b)/2
        ans=f(c)
        if ans>0:
            b=c
        elif ans<0:
            a=c
    return c

d=find_root(-5,0)
print(d)
