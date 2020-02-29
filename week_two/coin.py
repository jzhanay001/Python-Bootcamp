import random
"""
"""

def flip_coin():

    """
    returns a coin flip- random integer between 0 and 1
    if 1 - the coin lands on head
    if 0 - the coin lands on tail
    """

    return random.randint(0,1) #equal chance of being on head or tails

def monte_carlo(n):

    """
    performs a monte_carlo simulation of a coin flip
    [Param]\t n (int)- number of samples
    [Return]\t None- prints out the results of the simulation
    """
    head_count=0
    tail_count=0
    exp_count=0
    while exp_count < n:
        result = flip_coin()
        if result == 1:
            head_count +=1
        else:
            tail_count +=1
        exp_count+=1
    print(f"There were {n} simulations performed.")
    msg=f"There were {(head_count/n) * 100} % heads"
    print(msg)
    msg=f"There were {(tail_count/n)*  100} % tails"
    print(msg)

# import the random module

help(random.choice)
monte_carlo(1000000)
'''if result ==1:
    print("head")
else:
    print("tail")'''
