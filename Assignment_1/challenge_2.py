def odds(n):
    od_list=[]
    if type(int(n)) == type(50):
        for i in range (0,n+1):
            if i % 2 != 0 :
                od_list.append(i)
        return od_list
    else:
        return None

b=odds(5) # input numbers here, only accept int number
print (b) # other type will return Non

#Another way to write code with user input
"""
def odds():
    od_list=[]
    n = int(input("Enter a number : "))
    for i in range (0,n+1):
        if i % 2 != 0 :
            od_list.append(i)
    return od_list

b=odds()
print (b)
"""
