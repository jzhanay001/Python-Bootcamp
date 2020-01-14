# Algorithm is step to do a task
def find_num(x,a):
    b=len(a)
    for i in range (0,b):
        if a[i]==x:
            index_num=i
            return index_num
    return None


f=find_num(10,[1,3,0,6])
print (f)
