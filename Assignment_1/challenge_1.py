'''def sum1():

    a = []
    n = int(input("Enter number of elements for a : ")) # for float replace int with float()
    Type=input("Enter type of number,int or float= ")

    if Type=='int':
        for i in range(0, n):
            ele_1 = int(input())
            a.append(ele_1) # adding the element
    else:
        for i in range(0, n):
            ele_1 = float(input())
            a.append(ele_1) # adding the element

    A=len(a)
    if A != 0:
        b=sum(a)
        return b
    else:
        b=sum(a)
        return b

input_list=sum1()

print (input_list)'''
'''def odds(n):
    od_list=[]
    if type(n) == type(50):
        for i in range (0,n+1):
            if i % 2 != 0 :
                od_list.append(i)
        return od_list
    else:
        return

b=odds(0) # input numbers here, only accept int number
print (b) # other type will return Non'''

'''def odds():
    od_list=[]
    n = int(input("Enter a number : "))
    for i in range (0,n+1):
        if i % 2 != 0 :
            od_list.append(i)
    return od_list

b=odds()
print (b) '''

'''def evens():
    n = int(input("Enter a number : "))
    N=abs(n)
    answer=N*2
    return answer

d=evens()
print (d)'''
'''def evens(n):
    N=abs(n)
    if type(N) == type(50):
        answer=N*2
        return answer
    else:
        return
d=evens(19)  # input numbers here, only accept int number
print (d)       # other type will return None'''
'''def compare(a,b):
    #if type(sum(a)) == type(50) and type(sum(b)) == type(50):
    if a != b:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))
    else:
        x=a.difference(b)
        y=b.difference(a)
        return list(x.union(y))
    #else:
        #return

a=set([1, 2,3])    #input list # here for a
b=set([4, 5, 6])    #input list # here for b
Com=compare(a,b)    # only accept int values in both set or else an error will occur

print (Com)'''

'''def compare():
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

print (Com)'''

'''def find_diffs(a,b):
    differences=[]
    for i in a:
        if i not in b:
            differences.append(element)

    for i in b:
        if i not in a:
            differences.append(element)
    return differences'''
