def evens(n):
    N=abs(n)
    if type(N) == type(50):
        answer=N*2
        return answer
    else:
        return
d=evens(19)  # input numbers here, only accept int number
print (d)       # other type will return None

# Another way to code with user input
"""
def evens():
    n = int(input("Enter a number : "))
    N=abs(n)
    answer=N*2
    return answer

d=evens()
print (d)
"""
