def sum1(list):
    length=len(list)

    if type(sum(list)) == type(50) or type(sum(list)) == type(5.0):

        if length != 0:
            b=sum(list)
            return b
        else:
            b=sum(list)
            return b
    else:
        return None

input_list=sum1([1,1]) # only will accept input numbers that are in int or float
                        # if a string is put in, an error will show up
print (input_list)

# Another way to write code with user inputs
"""

def sum1():

    a = []
    n = int(input("Enter number of elements for a : "))
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

print (input_list)
"""
