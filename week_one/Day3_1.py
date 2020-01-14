#TODO Write a function that takes an integer and a list as the input.
# the function should return the index of where the integer was found
# on the lists

    #print(sorted(evens_list))
'''
def search (x, list):
    print(len(list))
    b=len(list)
    print("list", list)
    for i in range(0,b,1):
        if list[i] == x:
            index_of_x = i
    return (index_of_x)

    #print(sorted(evens_list))
a=search(5,[4,6,5,7,8])
print(a)
'''

'''
#Find MAx
def search_max (list):
    print(len(list))
    b=len(list)
    print("list", list)
    max=list[0]
    for i in range(0,b,1):
        if list[i] >= max:
            max=list[i]
            #index_of_x = i
    return max

    #print(sorted(evens_list))
a=search_max([4,6,5,7,8])
print(a)

'''

#Find MAx
def search_min (list):
    print(len(list))
    b=len(list)
    print("list", list)
    min=list[0]
    for i in range(0,b,1):
        if list[i] <= min:
            min=list[i]
            #index_of_x = i
    return min

    #print(sorted(evens_list))
a=search_min([4,6,5,7,8])
print(a)
