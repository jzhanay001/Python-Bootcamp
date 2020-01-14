def compare(a,b):
    if type(sum(a)) == type(50) and type(sum(b)) == type(50):
    if a != b:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))
    else:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))
    else:
        return

a=set([1, 2,3])    #input list # here for a
b=set([4, 5, 6])    #input list # here for b
Com=compare(a,b)    # only accept int values in both set or else an error will occur

print (Com)

# Another way to code with user input
"""

def compare():
    a = []
    b = []
    n = int(input("Enter number of elements for a : "))
    for i in range(0, n):
        ele_1 = int(input())
        a.append(ele_1) # adding the element

    m = int(input("Enter number of elements for b: "))
    for i in range(0, m):
        ele_2 = int(input())
        b.append(ele_2) # adding the element

    a=set(a)
    b=set(b)

    if a != b:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))
    else:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))

Com=compare()

print (Com)

"""
