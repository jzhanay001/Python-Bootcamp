#TODO:Make a Function that takes in 2 inputs: An lower limit
#an upper limit: The function should return a list of all mutiple of 5
#between lower and upper limit (inclusive)

def my_functions():
    mult_list=[]
    M=int(input("Enter your lower limit:"))
    N = int(input("Enter your upper limit: "))
    for num in range(M,N+1):
        if num % 5 == 0:
            mult_list.append(num)
    return mult_list

t=my_functions()
print(t)
